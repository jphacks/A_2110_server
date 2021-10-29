import uvicorn

from fastapi import FastAPI
from routers import activity , ranking, user;
app = FastAPI()

app.include_router(activity.router)
app.include_router(ranking.router)
app.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)