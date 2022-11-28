from click.testing import CliRunner

from pgcheck.cli.interface import cli


def test_cli_basic(imagepath_wheel_mchannel):

    runner = CliRunner()
    # just make sure they don't raise errors
    result = runner.invoke(cli, ["--debug", "colorspaces"])
    assert result.exit_code == 0

    result = runner.invoke(cli, ["--debug", "blendmodes"])
    assert result.exit_code == 0

    result = runner.invoke(cli, ["--debug", "imageinfo", str(imagepath_wheel_mchannel)])
    assert result.exit_code == 0


def test_cli_check(imagepath_wheel_mchannel, imagepath_color_bars_alpha, tmp_path):

    runner = CliRunner()

    tmp_target_path = tmp_path / (imagepath_color_bars_alpha.stem + ".jpg")

    result = runner.invoke(
        cli,
        [
            "--debug",
            "check",
            str(imagepath_color_bars_alpha),
            str(tmp_target_path),
            "--colorspace",
            "sRGB:linear",
            "--target_colorspace",
            "sRGB",
        ],
    )
    assert result.exit_code == 0

    tmp_target_path = tmp_path / (imagepath_wheel_mchannel.stem + ".jpg")

    result = runner.invoke(
        cli,
        [
            "--debug",
            "check",
            str(imagepath_wheel_mchannel),
            str(tmp_target_path),
            "--colorspace",
            "sRGB",
            "--target_colorspace",
            "sRGB:linear",
            "--blend_mode",
            "invalid_replace",
            "--use_alpha_as_mask",
        ],
    )
    assert result.exit_code == 0
