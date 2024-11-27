from api.dependencies.collections import get_repository
from db.repositories.links import LinkRepository

from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import RedirectResponse

router = APIRouter()


@router.get(
    "/{hash_key}",
    status_code=status.HTTP_302_FOUND,
    response_model=None,
    name="Redirect",
)
async def redirect(
    hash_key: str,
    link_repository=Depends(get_repository(LinkRepository))
) -> RedirectResponse:
    link = await link_repository.get_link_by_hash_key(hash_key)

    if not link:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")

    return RedirectResponse(url=link["url"])
