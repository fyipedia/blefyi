"""MCP server for blefyi -- Bluetooth Low Energy tools for AI assistants.

Requires the ``mcp`` extra: ``pip install blefyi[mcp]``

Run as a standalone server::

    python -m blefyi.mcp_server

Or configure in ``claude_desktop_config.json``::

    {
        "mcpServers": {
            "blefyi": {
                "command": "python",
                "args": ["-m", "blefyi.mcp_server"]
            }
        }
    }
"""

from __future__ import annotations

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("blefyi")


@mcp.tool()
def ble_search(query: str) -> str:
    """Search for BLE chips, GATT profiles, Bluetooth versions, and terminology on BLEFYI.

    Search across BLE chips (nRF52840, ESP32-C3, CC2640R2F), GATT profiles
    (Heart Rate, Blood Pressure, HID), Bluetooth versions (4.0-5.4),
    beacon protocols (iBeacon, Eddystone), and glossary terms.

    Args:
        query: Search term (e.g. "nordic", "heart rate", "ibeacon", "advertising").
    """
    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        results = api.search(query)

    items = results.get("results", [])
    if not items:
        return f"No results found for '{query}'."

    lines = [
        f"## BLE Search: {query}",
        "",
        f"Found {len(items)} result(s):",
        "",
        "| Type | Name | Slug |",
        "|------|------|------|",
    ]

    for item in items:
        t, n, s = item.get("type", ""), item.get("name", ""), item.get("slug", "")
        lines.append(f"| {t} | {n} | {s} |")

    return "\n".join(lines)


@mcp.tool()
def ble_lookup(slug: str) -> str:
    """Look up a specific BLE chip by slug.

    Returns full specifications including manufacturer, Bluetooth version,
    RAM, flash, TX power, supported profiles, and use cases.

    Args:
        slug: Chip slug (e.g. "nrf52840", "esp32-c3", "cc2640r2f", "da14695").
    """
    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        data = api.chip(slug)

    lines = [
        f"## {data.get('name', slug)}",
        "",
        data.get("description", ""),
        "",
        f"- **Manufacturer**: {data.get('manufacturer', 'N/A')}",
        f"- **Bluetooth Version**: {data.get('bluetooth_version', 'N/A')}",
        f"- **RAM**: {data.get('ram', 'N/A')}",
        f"- **Flash**: {data.get('flash', 'N/A')}",
        f"- **TX Power**: {data.get('tx_power', 'N/A')}",
        f"- **Range**: {data.get('range', 'N/A')}",
    ]

    profiles = data.get("profiles", [])
    if profiles:
        lines.append("")
        lines.append("### Supported Profiles")
        for p in profiles:
            lines.append(f"- {p.get('name', '')} ({p.get('slug', '')})")

    return "\n".join(lines)


@mcp.tool()
def ble_compare(slug_a: str, slug_b: str) -> str:
    """Compare two BLE chips side by side.

    Args:
        slug_a: First chip slug (e.g. "nrf52840").
        slug_b: Second chip slug (e.g. "esp32-c3").
    """
    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        data = api.compare(slug_a, slug_b)

    a = data.get("a", {})
    b = data.get("b", {})

    lines = [
        f"## {a.get('name', slug_a)} vs {b.get('name', slug_b)}",
        "",
        "| Property | " + a.get("name", slug_a) + " | " + b.get("name", slug_b) + " |",
        "|----------|"
        + "-" * len(a.get("name", slug_a))
        + "--|"
        + "-" * len(b.get("name", slug_b))
        + "--|",
    ]

    fields = [
        ("Manufacturer", "manufacturer"),
        ("Bluetooth Version", "bluetooth_version"),
        ("RAM", "ram"),
        ("Flash", "flash"),
        ("TX Power", "tx_power"),
        ("Range", "range"),
    ]
    for label, key in fields:
        lines.append(f"| {label} | {a.get(key, '-')} | {b.get(key, '-')} |")

    return "\n".join(lines)


if __name__ == "__main__":
    mcp.run()
