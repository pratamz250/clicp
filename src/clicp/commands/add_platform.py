import typer
from clicp.database import add_platform_db

def add_platform_cli(
        name: str = typer.Option(
            ...,
            "--platform"
        )
        ):
    
    try:
        add_platform_db(name)
        print("Platform added.")
    except ValueError as e:
        print(e)