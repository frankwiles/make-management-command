from click.testing import CliRunner

from make_management_command.cli import cli


def test_no_command():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            cli,
        )
        assert result.exit_code == 0
        assert result.output.startswith("Checking for ")


def test_one_new_command():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, "test1")
        assert result.exit_code == 0
        assert result.output.startswith("Checking for ")


def test_two_new_commands():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, "test1 test2")
        assert result.exit_code == 0
        assert result.output.startswith("Checking for ")
