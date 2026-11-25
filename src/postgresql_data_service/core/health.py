from dataclasses import dataclass
from enum import StrEnum


class HealthStatus(StrEnum):
    """Framework-neutral service health states."""

    HEALTHY = "healthy"
    DEGRADED = "degraded"
    UNHEALTHY = "unhealthy"


@dataclass(frozen=True, slots=True)
class HealthReport:
    """Serializable health information owned by the core."""

    service: str
    environment: str
    status: HealthStatus = HealthStatus.HEALTHY

    def as_dict(self) -> dict[str, str]:
        """Return a transport-neutral representation."""

        return {
            "service": self.service,
            "environment": self.environment,
            "status": self.status.value,
        }


def build_health_report(*, service: str, environment: str) -> HealthReport:
    """Build the default process-level health report."""

    return HealthReport(
        service=service,
        environment=environment,
    )
