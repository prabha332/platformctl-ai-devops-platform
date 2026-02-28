import subprocess
from utils.logger import log


def scan_image(image_name: str):
    """
    Scan container image using Trivy
    """

    log(f"Starting security scan for image: {image_name}")

    try:
        subprocess.run(
            ["trivy", "image", image_name],
            check=True
        )

        log("Image scan completed successfully")

    except subprocess.CalledProcessError:
        log("Image scan failed")


def scan_cluster():
    """
    Kubernetes security benchmark scan
    """

    log("Running Kubernetes security scan")

    try:
        subprocess.run(
            ["kubectl", "get", "pods", "-A"],
            check=True
        )

        subprocess.run(
            ["kube-bench"],
            check=True
        )

        log("Cluster security scan completed")

    except Exception as e:
        log(f"Security scan error: {e}")
