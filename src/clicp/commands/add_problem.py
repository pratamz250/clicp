import typer
from clicp.database import add_problem_db

def add_problem_cli(
        name: str,
        platform_name: str | None = typer.Option(
            ...,
            "--platform",
            help="Platform name"
        ),
        rating: int | None = typer.Option(
            None,
            "--rating"
        ),
        contest_name: str | None = typer.Option(
            None,
            "--contest"
        )
        ):
    
    try:
        add_problem_db(name, platform_name, rating, contest_name)
        print("Problem added.")
    except ValueError as e:
        print(e)