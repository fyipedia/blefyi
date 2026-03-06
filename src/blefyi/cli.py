"""Command-line interface for blefyi.

Requires the ``cli`` extra: ``pip install blefyi[cli]``

Usage::

    blefyi search "nordic"
    blefyi chip nrf52840
    blefyi compare nrf52840 esp32-c3
    blefyi random
"""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(
    name="blefyi",
    help="Bluetooth Low Energy encyclopedia — look up BLE chips, profiles, and specs from BLEFYI.",
    no_args_is_help=True,
)
console = Console()


@app.command()
def search(
    query: str = typer.Argument(help="Search term (e.g. 'nordic', 'heart rate', 'ibeacon')"),
) -> None:
    """Search across chips, profiles, versions, beacons, and glossary."""
    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        results = api.search(query)

    table = Table(title=f"Search: {query}")
    table.add_column("Type", style="cyan", no_wrap=True)
    table.add_column("Name")
    table.add_column("Slug")

    items = results.get("results", [])
    if not items:
        console.print(f"[yellow]No results found for '{query}'[/yellow]")
        return

    for item in items:
        table.add_row(item.get("type", ""), item.get("name", ""), item.get("slug", ""))

    console.print(table)


@app.command()
def chip(
    slug: str = typer.Argument(help="Chip slug (e.g. 'nrf52840', 'esp32-c3')"),
) -> None:
    """Look up a BLE chip with full specifications."""
    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        data = api.chip(slug)

    console.print(f"\n[bold]{data.get('name', slug)}[/bold]")
    if data.get("description"):
        console.print(f"  {data['description'][:200]}")
    console.print()

    table = Table(title="Specifications")
    table.add_column("Property", style="cyan")
    table.add_column("Value")

    specs = [
        ("Manufacturer", data.get("manufacturer")),
        ("Bluetooth Version", data.get("bluetooth_version")),
        ("RAM", data.get("ram")),
        ("Flash", data.get("flash")),
        ("TX Power", data.get("tx_power")),
        ("Range", data.get("range")),
        ("Protocols", data.get("protocols")),
        ("Use Cases", data.get("use_cases")),
    ]
    for label, value in specs:
        if value is not None:
            table.add_row(label, str(value))

    console.print(table)


@app.command()
def compare(
    slug_a: str = typer.Argument(help="First chip slug"),
    slug_b: str = typer.Argument(help="Second chip slug"),
) -> None:
    """Compare two BLE chips side by side."""
    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        data = api.compare(slug_a, slug_b)

    a = data.get("a", {})
    b = data.get("b", {})

    table = Table(title=f"{a.get('name', slug_a)} vs {b.get('name', slug_b)}")
    table.add_column("Property", style="cyan")
    table.add_column(a.get("name", slug_a), style="green")
    table.add_column(b.get("name", slug_b), style="yellow")

    fields = [
        ("Manufacturer", "manufacturer"),
        ("Bluetooth Version", "bluetooth_version"),
        ("RAM", "ram"),
        ("Flash", "flash"),
        ("TX Power", "tx_power"),
        ("Range", "range"),
    ]
    for label, key in fields:
        table.add_row(label, str(a.get(key, "-")), str(b.get(key, "-")))

    console.print(table)


@app.command()
def random() -> None:
    """Discover a random BLE chip."""
    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        data = api.random()

    console.print(f"\n[bold]{data.get('name', 'Unknown')}[/bold]")
    if data.get("description"):
        console.print(f"  {data['description'][:200]}")
    console.print(f"  Manufacturer: {data.get('manufacturer', 'N/A')}")
    console.print(f"  Bluetooth: {data.get('bluetooth_version', 'N/A')}")
    console.print(f"  RAM: {data.get('ram', 'N/A')}")
    console.print()


if __name__ == "__main__":
    app()
