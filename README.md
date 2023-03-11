# gamut'in

Determine if the colors of a given source are inside the gamut of the target colorspace.

A tool specialized for one task but that does it well (well you judge it).
Available as CLI, GUI and Python API.

> **Warning** IN DEVELOPMENT, do not use. Breaking changes every day !

# Development

## PyCharm

### File-watchers

#### black

- File Type: Python
- Scope : Project Files
- Program : `$PyInterpreterDirectory$\black`
- Arguments : `$FilePath$`
- Output paths to refresh : `$FilePath$`
- Working Directory : `$ProjectFileDir$`
- Advanced Options : all unchecked

#### ruff

- File Type: Python
- Scope : Project Files
- Program : `$PyInterpreterDirectory$\ruff`
- Arguments : `$FilePath$ --fix-only`
- Output paths to refresh : `$FilePath$`
- Working Directory : `$ProjectFileDir$`
- Advanced Options : all unchecked

