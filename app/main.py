from fastapi import FastAPI

app = FastAPI(
    title="TaskFlow API",
    description="Backend API for task management",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }