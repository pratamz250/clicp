import typer
from clicp.commands.stats import stats
from clicp.commands.add_problem import add_problem_cli
from clicp.commands.init import init
from clicp.commands.delete_data_base import reset
from clicp.commands.add_platform import add_platform_cli

app = typer.Typer(
    no_args_is_help=True,
    help="CLI tool for managing problems, training, reviews, and statistics in competitive programming."
    )

app.command(help="Show statistics of solved problems")(stats)
app.command("addpr", help="Add a new problem to the system")(add_problem_cli)
app.command(help="Initialize the system")(init)
app.command(help="Reset the system")(reset)
app.command("addpl", help="Add a new platform to the system")(add_platform_cli)

def main():
    app()

if __name__ == "__main__":
    main()