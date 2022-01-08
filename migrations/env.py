import os
import sys

from logging.config import fileConfig
from alembic import context


# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config
compare_type = True
# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR = os.path.join(CURRENT_DIR, '..')

sys.path.append(BASE_DIR)

from db.base import metadata, db_engine

# Import db models
from migrations.models import *
# 

target_metadata = metadata


# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        user_module_prefix='sa.'
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    connectable = db_engine

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
