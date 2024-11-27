import hashlib

from core.config import settings


def generate_hash_url(url: str) -> str:
    hash_object = hashlib.sha512(url.encode())
    hash_hex = hash_object.hexdigest()

    return hash_hex[0 : settings.hash_length]
