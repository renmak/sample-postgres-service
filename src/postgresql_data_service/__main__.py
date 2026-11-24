from postgresql_data_service.core.settings import get_settings


def main() -> None:
    """Show configuration without opening a database connection."""
    settings = get_settings()
    print("PostgreSQL Data Service")
    print(f"Database driver: {settings.database_url.scheme}")
    print(f"SQL echo enabled: {settings.database_echo}")


if __name__ == "__main__":
    main()

