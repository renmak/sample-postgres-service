from postgresql_data_service.core.health import HealthStatus, build_health_report


def test_default_health_report() -> None:
    report = build_health_report(
        service="postgresql-data-service",
        environment="test",
    )

    assert report.status is HealthStatus.HEALTHY
    assert report.as_dict() == {
        "service": "postgresql-data-service",
        "environment": "test",
        "status": "healthy",
    }
