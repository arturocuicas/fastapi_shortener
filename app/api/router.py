from fastapi import APIRouter

from api.routes.links import router as links_router
from api.routes.redirects import router as redirects_router

router = APIRouter()

router.include_router(links_router, tags=["Links"], prefix="/links")
router.include_router(redirects_router, tags=["Redirects"], prefix="/s")
