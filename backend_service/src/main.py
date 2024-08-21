from fastapi import FastAPI

from .config import get_settings
from .app_info import AppInfo
from .public.routers import public_routers

app_info = AppInfo()
settings = get_settings()


def register_routers(app):
    app.include_router(public_routers)
    # app.include_router(auth_routers)


def create_app() -> FastAPI:
    # Creating APP
    app = FastAPI(
        title=app_info.title,
        description=app_info.description,
        version=app_info.version,
        docs_url=settings.DOCS_URL
    )
    # include routers
    register_routers(app)
    return app

# APP creation
app = create_app()