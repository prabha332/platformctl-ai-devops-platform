import subprocess

def auto_heal(namespace):

    pods = subprocess.run(
        ["kubectl", "get", "pods", "-n", namespace],
        capture_output=True,
        text=True
    )

    for line in pods.stdout.split("\n"):
        if "CrashLoopBackOff" in line:
            pod = line.split()[0]

            print(f"Restarting {pod}")

            subprocess.run(
                ["kubectl", "delete", "pod", pod, "-n", namespace]
            )
