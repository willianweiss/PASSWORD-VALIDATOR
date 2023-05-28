from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.routes.password_validator import router


def get_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app


app = get_app()
