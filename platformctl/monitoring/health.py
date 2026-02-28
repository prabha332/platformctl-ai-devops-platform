import subprocess

def check_health(namespace):

    result = subprocess.run(
        ["kubectl", "get", "pods", "-n", namespace],
        capture_output=True,
        text=True
    )

    for line in result.stdout.split("\n"):
        if "CrashLoopBackOff" in line:
            print("Unhealthy Pod:", line)
