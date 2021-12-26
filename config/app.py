from config import env_config

HOST: str = env_config('HOST', cast=str, default='localhost')
PORT: int = env_config('PORT', cast=int, default=8000)
RELOAD: bool = env_config('RELOAD', cast=bool, default=False)


__all__ = (
    'HOST',
    'PORT',
    'RELOAD',
)

