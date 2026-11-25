from postgresql_data_service.core.settings import Settings


def test_default_database_driver_is_asyncpg() -> None:
    settings = Settings(_env_file=None)

    assert settings.service_environment == "local"
    assert settings.database_url.scheme == "postgresql+asyncpg"
