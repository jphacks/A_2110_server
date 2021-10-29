import uvicorn

from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
import routers.activity as activity
from routers import ranking, user

origins = [
    "https://a-2110.vercel.app",
    "http://a-2110.vercel.app",
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
]

app = FastAPI()
app.include_router(activity.router)
app.include_router(ranking.router)
app.include_router(user.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)