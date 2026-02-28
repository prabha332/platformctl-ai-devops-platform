import subprocess

def deploy_app(file):
    print("Deploying application...")

    subprocess.run(
        ["kubectl", "apply", "-f", file],
        check=True
    )

    print("Deployment successful")
