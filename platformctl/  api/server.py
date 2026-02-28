from fastapi import FastAPI
from deployment.deploy import deploy_app

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "PlatformCTL running"}

@app.post("/deploy")
def deploy(file: str):
    deploy_app(file)
    return {"message": "Deployment triggered"}
