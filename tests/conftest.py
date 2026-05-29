import os
import pytest

from app.core.database import (
    Database,
    DatabaseInitializer,
)

TEST_DATABASE = "test.db"


@pytest.fixture
def test_database():

    if os.path.exists(TEST_DATABASE):
        os.remove(TEST_DATABASE)

    os.environ["DATABASE_NAME"] = (
        TEST_DATABASE
    )

    database = Database()

    initializer = DatabaseInitializer(
        database
    )

    initializer.initialize()

    yield database

    if os.path.exists(TEST_DATABASE):
        os.remove(TEST_DATABASE)