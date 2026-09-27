from fastapi import FastAPI

from routers import users


app = FastAPI(
    title="TaskFlow API",
    description="Backend API for task management",
    version="0.1.0",
)


app.include_router(users.router)


@app.get("/health")
def health_check():
    return {"status": "healthy"}