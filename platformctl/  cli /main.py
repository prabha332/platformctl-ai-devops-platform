import typer
from deployment.deploy import deploy_app
from monitoring.health import check_health
from healing.autoheal import auto_heal
from ai.troubleshoot import ai_debug

app = typer.Typer()

@app.command()
def deploy(file: str):
    deploy_app(file)

@app.command()
def health(namespace: str = "default"):
    check_health(namespace)

@app.command()
def heal(namespace: str = "default"):
    auto_heal(namespace)

@app.command()
def ai(issue: str):
    ai_debug(issue)

if __name__ == "__main__":
    app()
