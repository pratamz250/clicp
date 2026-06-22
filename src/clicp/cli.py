import typer
from clicp.commands.stats import stats
from clicp.commands.add_problem import add_problem_cli
from clicp.commands.init import init
from clicp.commands.delete_data_base import reset
from clicp.commands.add_platform import add_platform_cli

app = typer.Typer(no_args_is_help=True)

app.command()(stats)
app.command("add-problem")(add_problem_cli)
app.command()(init)
app.command()(reset)
app.command("add-platform")(add_platform_cli)

def main():
    app()

if __name__ == "__main__":
    main()