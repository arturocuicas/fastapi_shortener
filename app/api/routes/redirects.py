import pickle

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse

from api.dependencies.collections import get_repository
from api.dependencies.redis import cache
from db.repositories.links import LinkRepository

router = APIRouter()


@router.get(
    "/{hash_key}",
    status_code=status.HTTP_302_FOUND,
    response_model=None,
    name="Redirect",
)
async def redirect(
    hash_key: str,
    redis_client: cache = Depends(cache),
    link_repository=Depends(get_repository(LinkRepository)),
) -> RedirectResponse:
    if (cached_link := redis_client.get(hash_key)) is not None:
        link = pickle.loads(cached_link)

        return RedirectResponse(url=link["url"])

    link = await link_repository.get_link_by_hash_key(hash_key)

    if not link:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Link not found"
        )

    redis_client.set(link["hash_key"], pickle.dumps(link), ex=3600)

    return RedirectResponse(url=link["url"])
