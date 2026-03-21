"""MCP server for blefyi — AI assistant tools for blefyi.com.

Run: uvx --from "blefyi[mcp]" python -m blefyi.mcp_server
"""
from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("BLEFYI")


@mcp.tool()
def list_profiles(limit: int = 20, offset: int = 0) -> str:
    """List profiles from blefyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        data = api.list_profiles(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No profiles found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def get_profile(slug: str) -> str:
    """Get detailed information about a specific profile.

    Args:
        slug: URL slug identifier for the profile.
    """
    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        data = api.get_profile(slug)
        return str(data)


@mcp.tool()
def list_beacons(limit: int = 20, offset: int = 0) -> str:
    """List beacons from blefyi.com.

    Args:
        limit: Maximum number of results. Default 20.
        offset: Number of results to skip. Default 0.
    """
    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        data = api.list_beacons(limit=limit, offset=offset)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return "No beacons found."
        items = results[:limit] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


@mcp.tool()
def search_ble(query: str) -> str:
    """Search blefyi.com for BLE profiles, beacons, GATT services, and chips.

    Args:
        query: Search query string.
    """
    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        data = api.search(query)
        results = data.get("results", data) if isinstance(data, dict) else data
        if not results:
            return f"No results found for \"{query}\"."
        items = results[:10] if isinstance(results, list) else []
        return "\n".join(f"- {item.get('name', item.get('slug', '?'))}" for item in items)


def main() -> None:
    """Run the MCP server."""
    mcp.run()


if __name__ == "__main__":
    main()
