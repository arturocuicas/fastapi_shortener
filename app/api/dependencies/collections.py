from fastapi import Depends
from motor.motor_asyncio import AsyncIOMotorClient

from db.sessions import database


def get_db():
    return database


def get_repository(repository):
    def _get_repository(session: AsyncIOMotorClient = Depends(get_db)):
        return repository(session)

    return _get_repository
