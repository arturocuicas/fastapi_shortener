from typing import List

from fastapi import APIRouter, HTTPException, status, Depends

from api.dependencies.collections import get_repository
from db.repositories.links import LinkRepository
from schemas.links import LinkCreate, LinkRead, LinkUpdate

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=LinkRead,
    name="Create Link",
)
async def create_link(
    link_create: LinkCreate,
    link_repository = Depends(get_repository(LinkRepository)),
) -> LinkRead:
    new_link = await link_repository.create_link(link_create)

    return LinkRead(
        id=str(new_link["_id"]),
        url=new_link["url"],
        hash_key=new_link["hash_key"],
    )


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=List[LinkRead],
    name="Links",
)
async def get_links(
    link_repository = Depends(get_repository(LinkRepository)),
) -> List[LinkRead]:

    return [
        LinkRead(
            id=str(link["_id"]),
            url=link["url"],
            hash_key=link["hash_key"],
        )
        for link in await link_repository.get_links()
    ]

@router.get(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=LinkRead,
    name="Link",
)
async def get_link(
    id: str,
    link_repository = Depends(get_repository(LinkRepository)),
) -> LinkRead:
    link = await link_repository.get_link(id)

    if not link:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")

    return LinkRead(
        id=str(link["_id"]),
        url=link["url"],
        hash_key=link["hash_key"],
    )

@router.put(
    "/{id}",
    status_code=status.HTTP_200_OK,
    response_model=LinkRead,
    name="Update Link",
)
async def update_link(
    id: str,
    link_update: LinkUpdate,
    link_repository = Depends(get_repository(LinkRepository)),
) -> LinkRead:
    link = await link_repository.update_link(id, link_update)

    if not link:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")

    return LinkRead(
        id=str(link["_id"]),
        url=link["url"],
        hash_key=link["hash_key"],
    )

@router.delete(
    "/{id}",
    status_code=status.HTTP_204_NO_CONTENT,
    response_model=None,
    name="Delete Link",
)
async def delete_link(
    id: str,
    link_repository = Depends(get_repository(LinkRepository)),
):
    link = await link_repository.delete_link(id)

    if not link:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Link not found")

    return None
