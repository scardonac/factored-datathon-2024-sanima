from fastapi import APIRouter
from datetime import datetime, UTC
from ..app_info import AppInfo

public_routers = APIRouter(tags=['Public'])


@public_routers.get('/')
def index():
    return {
        'status': "pass",
        'version': AppInfo.version,
        'timestamp': datetime.now(UTC).isoformat() + "Z"
    }


@public_routers.get('/app_info')
def app_info():
    return AppInfo()
