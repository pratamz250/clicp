import typer
from clicp.commands.hello import hello
from clicp.commands.stats import stats
from clicp.commands.add import add
from clicp.commands.init import init
from clicp.commands.deleteDataBase import reset

app = typer.Typer(no_args_is_help=True)

app.command()(hello)
app.command()(stats)
app.command()(add)
app.command()(init)
app.command()(reset)

def main():
    app()

if __name__ == "__main__":
    main()