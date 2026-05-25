import typer
from clicp.commands.hello import hello
from clicp.commands.stats import stats
from clicp.commands.add import add

app = typer.Typer(no_args_is_help=True)

app.command()(hello)
app.command()(stats)
app.command()(add)

def main():
    app()
