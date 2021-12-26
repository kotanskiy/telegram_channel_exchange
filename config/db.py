from config import env_config


DB_HOST = env_config('DB_HOST', cast=str, default='localhost')
DB_PORT = env_config('DB_PORT', cast=int, default=5432)
DB_USER = env_config('DB_USER', cast=str, default='postgres')
DB_PASSWORD = env_config('DB_PASSWORD', cast=str, default='')
DB_NAME = env_config('DB_NAME', cast=str, default='telegram_channel_exchange')


__all__ = (
    'DB_HOST',
    'DB_PORT',
    'DB_USER',
    'DB_PASSWORD',
    'DB_NAME',
)
