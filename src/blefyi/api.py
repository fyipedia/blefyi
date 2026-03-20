"""HTTP API client for blefyi.com REST endpoints.

Requires the ``api`` extra: ``pip install blefyi[api]``

Usage::

    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        items = api.list_beacons()
        detail = api.get_beacon("example-slug")
        results = api.search("query")
"""

from __future__ import annotations

from typing import Any

import httpx


class BLEFYI:
    """API client for the blefyi.com REST API.

    Provides typed access to all blefyi.com endpoints including
    list, detail, and search operations.

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

    def _get(self, path: str, **params: Any) -> dict[str, Any]:
        resp = self._client.get(
            path,
            params={k: v for k, v in params.items() if v is not None},
        )
        resp.raise_for_status()
        result: dict[str, Any] = resp.json()
        return result

    # -- Endpoints -----------------------------------------------------------

    def list_beacons(self, **params: Any) -> dict[str, Any]:
        """List all beacons."""
        return self._get("/api/v1/beacons/", **params)

    def get_beacon(self, slug: str) -> dict[str, Any]:
        """Get beacon by slug."""
        return self._get(f"/api/v1/beacons/" + slug + "/")

    def list_chips(self, **params: Any) -> dict[str, Any]:
        """List all chips."""
        return self._get("/api/v1/chips/", **params)

    def get_chip(self, slug: str) -> dict[str, Any]:
        """Get chip by slug."""
        return self._get(f"/api/v1/chips/" + slug + "/")

    def list_faqs(self, **params: Any) -> dict[str, Any]:
        """List all faqs."""
        return self._get("/api/v1/faqs/", **params)

    def get_faq(self, slug: str) -> dict[str, Any]:
        """Get faq by slug."""
        return self._get(f"/api/v1/faqs/" + slug + "/")

    def list_glossary(self, **params: Any) -> dict[str, Any]:
        """List all glossary."""
        return self._get("/api/v1/glossary/", **params)

    def get_term(self, slug: str) -> dict[str, Any]:
        """Get term by slug."""
        return self._get(f"/api/v1/glossary/" + slug + "/")

    def list_guides(self, **params: Any) -> dict[str, Any]:
        """List all guides."""
        return self._get("/api/v1/guides/", **params)

    def get_guide(self, slug: str) -> dict[str, Any]:
        """Get guide by slug."""
        return self._get(f"/api/v1/guides/" + slug + "/")

    def list_manufacturers(self, **params: Any) -> dict[str, Any]:
        """List all manufacturers."""
        return self._get("/api/v1/manufacturers/", **params)

    def get_manufacturer(self, slug: str) -> dict[str, Any]:
        """Get manufacturer by slug."""
        return self._get(f"/api/v1/manufacturers/" + slug + "/")

    def list_mesh(self, **params: Any) -> dict[str, Any]:
        """List all mesh."""
        return self._get("/api/v1/mesh/", **params)

    def get_mesh(self, slug: str) -> dict[str, Any]:
        """Get mesh by slug."""
        return self._get(f"/api/v1/mesh/" + slug + "/")

    def list_profiles(self, **params: Any) -> dict[str, Any]:
        """List all profiles."""
        return self._get("/api/v1/profiles/", **params)

    def get_profile(self, slug: str) -> dict[str, Any]:
        """Get profile by slug."""
        return self._get(f"/api/v1/profiles/" + slug + "/")

    def list_tools(self, **params: Any) -> dict[str, Any]:
        """List all tools."""
        return self._get("/api/v1/tools/", **params)

    def get_tool(self, slug: str) -> dict[str, Any]:
        """Get tool by slug."""
        return self._get(f"/api/v1/tools/" + slug + "/")

    def list_use_cases(self, **params: Any) -> dict[str, Any]:
        """List all use cases."""
        return self._get("/api/v1/use-cases/", **params)

    def get_use_case(self, slug: str) -> dict[str, Any]:
        """Get use case by slug."""
        return self._get(f"/api/v1/use-cases/" + slug + "/")

    def list_versions(self, **params: Any) -> dict[str, Any]:
        """List all versions."""
        return self._get("/api/v1/versions/", **params)

    def get_version(self, slug: str) -> dict[str, Any]:
        """Get version by slug."""
        return self._get(f"/api/v1/versions/" + slug + "/")

    def search(self, query: str, **params: Any) -> dict[str, Any]:
        """Search across all content."""
        return self._get(f"/api/v1/search/", q=query, **params)

    # -- Lifecycle -----------------------------------------------------------

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> BLEFYI:
        return self

    def __exit__(self, *_: object) -> None:
        self.close()
