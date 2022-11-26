__all__ = (
    "getCurrentDependencies",
    "getSysContext",
)

import json

import pkg_resources
import platform

import pgcheck


def getCurrentDependencies() -> list[tuple[str, str]]:
    """
    Get all the installed packages/library in the current python environment.

    If we are in a frozen application context, the dependencies must come from
    an environement variable.

    Returns:
        list of [packageName, version]
    """
    if pgcheck.c.is_frozen:
        dependencies_str = pgcheck.c.Env.get(pgcheck.c.Env.dependencies_list)
        if not dependencies_str:
            return [
                (f"Missing env variable {pgcheck.c.Env.dependencies_list.value}", "ERROR")
            ]
        dependencies_list = dependencies_str.split(";")
        dependencies = [
            tuple(dependency.split(":", 1)) for dependency in dependencies_list
        ]
        return dependencies

    dependencies = list()
    for pkg in pkg_resources.working_set:
        dependencies.append((pkg.project_name, pkg.version))

    dependencies.append(("python", platform.python_version()))
    return dependencies


def getSysContext() -> str:
    """
    Return the execution context to help at troubleshooting.

    This is a human readble string.
    """
    env = [f"{vardata[0]}={vardata[1]}" for vardata in pgcheck.c.Env.__asdict__().items()]
    out = (
        f"coco: {pgcheck.__version__}\n"
        f"platform: {platform.platform()}\n"
        f"frozen: {pgcheck.c.is_frozen}\n"
        f"env: {json.dumps(env, indent=4, default=str)}\n"
    )
    return out
