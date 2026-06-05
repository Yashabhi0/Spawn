import typer

from rich.panel import Panel

from spawn.cli.prompts import get_project_config
from spawn.generators.project_generator import ProjectGenerator
from spawn.utils.console import console

app = typer.Typer()


@app.command()
def create() -> None:

    console.print(
        Panel.fit(
            "Create development environments in seconds",
            title="🚀 Spawn",
        )
    )

    config = get_project_config()

    generator = ProjectGenerator()
    try:
     generator.generate(config)

    except Exception as e:
      console.print(
        f"[red]❌ {e}[/red]"
    )


@app.command()
def version():
    """Show application version."""
    typer.echo("Spawn v0.1.0")


def main():
    app()


if __name__ == "__main__":
    main()