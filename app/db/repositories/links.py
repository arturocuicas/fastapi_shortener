from typing import Dict, List, Optional

from bson.objectid import ObjectId

from schemas.links import LinkCreate, LinkRead, LinkUpdate
from utils.shortener import generate_hash_url


class LinkRepository:
    def __init__(self, session):
        self.session = session

    async def _get_link(self, id: ObjectId) -> Optional[Dict]:
        return await self.session["links"].find_one({"_id": id})

    async def get_links(self) -> List[Optional[Dict]]:
        return [
            link
            async for link
            in self.session["links"].find()
        ]

    async def create_link(self, link_create: LinkCreate) -> Dict:
        link = await self.session["links"].insert_one(
            {
                "url": str(link_create.url),
                "hash_key": generate_hash_url(str(link_create.url)),
            }
        )

        return await self._get_link(link.inserted_id)

    async def get_link(self, id: str) -> Optional[Dict]:
        return await self._get_link(ObjectId(id))

    async def update_link(self, id: str, link_update: LinkUpdate) -> Optional[Dict]:
        link = await self._get_link(ObjectId(id))

        if not link:
            return None

        await self.session["links"].update_one(
            {"_id": ObjectId(id)},
            {"$set": {
                "url": str(link_update.url),
                "hash_key": generate_hash_url(str(link_update.url))
            }},
        )

        return await self._get_link(ObjectId(id))

    async def delete_link(self, id: str):
        link = await self._get_link(ObjectId(id))

        if not link:
            return False

        return await self.session["links"].delete_one({"_id": ObjectId(id)})

    async def get_link_by_hash_key(self, hash_key: str) -> Optional[Dict]:
        return await self.session["links"].find_one({"hash_key": hash_key})
