from config import settings

from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

# limiter = Limiter(
#     key_func=get_remote_address,
#     storage_uri=f'redis://:{settings.REDIS_PASSWORD}@redis:{settings.REDIS_PORT}/0'
# )
