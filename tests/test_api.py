"""Tests for blefyi API client."""

from __future__ import annotations

from blefyi.api import BLEFYI


def test_client_init() -> None:
    client = BLEFYI()
    assert client._client.base_url == "https://blefyi.com"
    client.close()


def test_client_custom_base_url() -> None:
    client = BLEFYI(base_url="https://test.example.com")
    assert client._client.base_url == "https://test.example.com"
    client.close()


def test_client_context_manager() -> None:
    with BLEFYI() as api:
        assert api._client.base_url == "https://blefyi.com"


def test_version() -> None:
    from blefyi import __version__

    assert __version__ == "0.1.0"
