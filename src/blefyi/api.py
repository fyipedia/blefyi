"""HTTP API client for blefyi.com REST endpoints.

Requires the ``api`` extra: ``pip install blefyi[api]``

Usage::

    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        results = api.search("nordic")
        chip = api.chip("nrf52840")
        comparison = api.compare("nrf52840", "esp32-c3")
"""

from __future__ import annotations

from typing import Any

import httpx


class BLEFYI:
    """API client for the blefyi.com REST API.

    Provides access to 11 endpoints covering BLE chips, GATT profiles,
    Bluetooth versions, beacon protocols, use cases, manufacturers,
    glossary terms, search, comparison, and random discovery.

    Args:
        base_url: API base URL. Defaults to ``https://blefyi.com``.
        timeout: Request timeout in seconds. Defaults to ``10.0``.
    """

    def __init__(
        self,
        base_url: str = "https://blefyi.com",
        timeout: float = 10.0,
    ) -> None:
        self._client = httpx.Client(base_url=base_url, timeout=timeout)

    # -- HTTP helpers ----------------------------------------------------------

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(path, params={k: v for k, v in params.items() if v is not None})
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -------------------------------------------------------------

    def chip(self, slug: str) -> dict[str, Any]:
        """Get BLE chip detail with specs, profiles, and manufacturer.

        Args:
            slug: Chip URL slug (e.g. ``"nrf52840"``, ``"esp32-c3"``, ``"cc2640r2f"``).
        """
        return self._get(f"/api/chip/{slug}/")

    def profile(self, slug: str) -> dict[str, Any]:
        """Get GATT profile detail with characteristics and services.

        Args:
            slug: Profile URL slug (e.g. ``"heart-rate"``, ``"blood-pressure"``, ``"hid"``).
        """
        return self._get(f"/api/profile/{slug}/")

    def version(self, slug: str) -> dict[str, Any]:
        """Get Bluetooth version detail with features and changelog.

        Args:
            slug: Version URL slug (e.g. ``"4-0"``, ``"5-0"``, ``"5-4"``).
        """
        return self._get(f"/api/version/{slug}/")

    def beacon(self, slug: str) -> dict[str, Any]:
        """Get beacon protocol detail with advertising format and use cases.

        Args:
            slug: Beacon URL slug (e.g. ``"ibeacon"``, ``"eddystone"``, ``"altbeacon"``).
        """
        return self._get(f"/api/beacon/{slug}/")

    def usecase(self, slug: str) -> dict[str, Any]:
        """Get BLE use case detail with related chips and profiles.

        Args:
            slug: Use case URL slug (e.g. ``"asset-tracking"``, ``"wearable-fitness"``).
        """
        return self._get(f"/api/usecase/{slug}/")

    def manufacturer(self, slug: str) -> dict[str, Any]:
        """Get manufacturer detail with BLE chip lineup.

        Args:
            slug: Manufacturer URL slug (e.g. ``"nordic-semiconductor"``, ``"espressif"``).
        """
        return self._get(f"/api/manufacturer/{slug}/")

    def glossary_term(self, slug: str) -> dict[str, Any]:
        """Get glossary term definition for tooltips and reference.

        Args:
            slug: Term URL slug (e.g. ``"gatt"``, ``"advertising"``, ``"connection-interval"``).
        """
        return self._get(f"/api/term/{slug}/")

    def search(self, query: str) -> dict[str, Any]:
        """Search across chips, profiles, versions, beacons, and glossary terms.

        Args:
            query: Search term (minimum 2 characters).
        """
        return self._get("/api/search/", q=query)

    def compare(self, slug_a: str, slug_b: str) -> dict[str, Any]:
        """Compare two BLE chips side by side.

        Args:
            slug_a: First chip slug (e.g. ``"nrf52840"``).
            slug_b: Second chip slug (e.g. ``"esp32-c3"``).
        """
        return self._get("/api/compare/", a=slug_a, b=slug_b)

    def random(self) -> dict[str, Any]:
        """Get a random BLE chip with full detail."""
        return self._get("/api/random/")

    def openapi(self) -> dict[str, Any]:
        """Get the OpenAPI 3.1.0 specification."""
        return self._get("/api/openapi.json")

    # -- Context manager -------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP connection."""
        self._client.close()

    def __enter__(self) -> BLEFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
