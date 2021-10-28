import uvicorn

from fastapi import FastAPI
from routers import activity, ranking, user;
api = FastAPI()

api.include_router(activity.router)
api.include_router(ranking.router)
api.include_router(user.router)


if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8000)