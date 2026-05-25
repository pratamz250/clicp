import typer
from clicp.commands.hello import hello
from clicp.commands.stats import stats
from clicp.commands.add import add
from clicp.commands.init import init

app = typer.Typer(no_args_is_help=True)

app.command()(hello)
app.command()(stats)
app.command()(add)
app.command()(init)

def main():
    app()
