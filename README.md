# blefyi

[![PyPI version](https://agentgif.com/badge/pypi/blefyi/version.svg)](https://pypi.org/project/blefyi/)
[![Python](https://img.shields.io/pypi/pyversions/blefyi)](https://pypi.org/project/blefyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Bluetooth Low Energy encyclopedia API client for Python. Look up BLE chips from Nordic, Espressif, TI, Dialog, Silicon Labs, Qualcomm, and STMicroelectronics, GATT profiles and services, Bluetooth versions 4.0-5.4, beacon protocols (iBeacon, Eddystone, AltBeacon), and IoT specifications from [BLEFYI](https://blefyi.com) -- the comprehensive BLE reference with 261 records covering every major BLE system-on-chip in commercial and industrial use.

Extracted from [BLEFYI](https://blefyi.com), a Bluetooth Low Energy platform with 261 records spanning chip specifications, GATT profile definitions, version history, beacon protocol details, and IoT deployment guides used by embedded firmware engineers, IoT architects, and wearable device developers worldwide.

> **Explore BLE at [blefyi.com](https://blefyi.com)** -- [Chip Explorer](https://blefyi.com/chip/) | [Profile Reference](https://blefyi.com/profile/) | [Version History](https://blefyi.com/version/) | [Beacon Protocols](https://blefyi.com/beacon/)

<p align="center">
  <img src="https://raw.githubusercontent.com/fyipedia/blefyi/main/demo.gif" alt="blefyi demo -- BLE chip lookup, GATT profile reference, and chip comparison in Python" width="800">
</p>

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [What You'll Find on BLEFYI](#what-youll-find-on-blefyi)
  - [BLE Chips and System-on-Chip (SoC)](#ble-chips-and-system-on-chip-soc)
  - [GATT Profiles and Services](#gatt-profiles-and-services)
  - [Bluetooth Versions (4.0-5.4)](#bluetooth-versions-40-54)
  - [Beacon Protocols](#beacon-protocols)
  - [BLE vs Bluetooth Classic](#ble-vs-bluetooth-classic)
  - [Advertising Modes](#advertising-modes)
  - [BLE Mesh Networking](#ble-mesh-networking)
- [API Endpoints](#api-endpoints)
- [Command-Line Interface](#command-line-interface)
- [MCP Server (Claude, Cursor, Windsurf)](#mcp-server-claude-cursor-windsurf)
- [REST API Client](#rest-api-client)
- [Learn More About BLE](#learn-more-about-ble)
- [Also Available](#also-available)
- [Tag FYI Family](#tag-fyi-family)
- [FYIPedia Developer Tools](#fyipedia-developer-tools)
- [License](#license)

## Install

```bash
pip install blefyi[api]     # API client (httpx)
pip install blefyi[cli]     # + CLI (typer, rich)
pip install blefyi[mcp]     # + MCP server
pip install blefyi[all]     # Everything
```

## Quick Start

```python
from blefyi.api import BLEFYI

with BLEFYI() as api:
    # Search chips, profiles, versions, beacons, glossary
    results = api.search("nordic")
    print(results)

    # Look up a specific BLE chip
    nrf = api.chip("nrf52840")
    print(nrf["name"], nrf["manufacturer"])  # nRF52840 Nordic Semiconductor

    # Compare two BLE chips side-by-side
    diff = api.compare("nrf52840", "esp32-c3")
    print(diff)

    # Discover a random BLE chip
    surprise = api.random()
    print(surprise["name"])
```

## What You'll Find on BLEFYI

BLEFYI is a comprehensive Bluetooth Low Energy encyclopedia covering BLE chips, GATT profiles, Bluetooth versions, beacon protocols, manufacturers, and IoT use cases. Bluetooth Low Energy (BLE), introduced as part of the Bluetooth 4.0 Core Specification in 2010, is a wireless personal area network technology designed for short-range, low-power communication -- the foundation of wearable fitness trackers, medical devices, asset tracking, smart home automation, and industrial IoT worldwide.

### BLE Chips and System-on-Chip (SoC)

BLE chips are the silicon at the heart of every Bluetooth Low Energy device. Each SoC integrates a radio transceiver, ARM Cortex-M processor, RAM, flash memory, and peripheral interfaces into a single package. Key selection criteria include Bluetooth version support, TX power range (dBm), receiver sensitivity, RAM/flash capacity, GPIO count, and multi-protocol support (BLE, Zigbee, Thread, Matter).

| Manufacturer | Key Chips | Bluetooth | Core | Notable Feature |
|-------------|-----------|-----------|------|-----------------|
| Nordic Semiconductor | nRF52840, nRF52832, nRF5340 | 5.0-5.3 | Cortex-M4F / M33+M16 | Best-in-class SDK (nRF Connect), Zephyr RTOS |
| Espressif | ESP32-C3, ESP32-C6, ESP32-H2 | 5.0-5.3 | RISC-V | Wi-Fi + BLE combo, open-source IDF |
| Texas Instruments | CC2640R2F, CC2652R | 5.0-5.1 | Cortex-M4F | Ultra-low power, medical-grade (IEC 60601) |
| Dialog Semiconductor | DA14695, DA14531 | 5.1-5.2 | Cortex-M33 / M0+ | Smallest BLE SoC (DA14531: 2.0x1.7mm) |
| Silicon Labs | EFR32BG22, EFR32BG24 | 5.2-5.3 | Cortex-M33 | Direction Finding (AoA/AoD), Bluetooth Mesh |
| Qualcomm | QCC5144, QCC3056 | 5.2-5.3 | Cortex-M4F | LE Audio, LC3 codec, active noise cancellation |
| STMicroelectronics | STM32WB55, BlueNRG-2 | 5.0-5.3 | Cortex-M4+M0 | STM32 ecosystem integration, dual-core |

**Nordic nRF52840** is the most widely used BLE 5.0 SoC, powering devices from Fitbit trackers to industrial sensors. It features a 64 MHz Cortex-M4F with FPU, 1 MB flash, 256 KB RAM, USB 2.0, NFC-A tag emulation, and support for BLE, Zigbee, Thread, and ANT protocols on a single chip.

Learn more: [Chip Explorer](https://blefyi.com/chip/) | [Glossary](https://blefyi.com/glossary/)

### GATT Profiles and Services

The Generic Attribute Profile (GATT) defines how BLE devices expose structured data through a hierarchy of services, characteristics, and descriptors. The Bluetooth SIG maintains adopted profiles that ensure interoperability across manufacturers.

| Profile Category | Examples | UUID Range |
|-----------------|----------|------------|
| Health & Fitness | Heart Rate (0x180D), Blood Pressure (0x1810), Glucose (0x1808) | 0x180D-0x181F |
| HID & Input | Human Interface Device (0x1812), Scan Parameters (0x1813) | 0x1812-0x1813 |
| Proximity & Location | Immediate Alert (0x1802), Link Loss (0x1803), Indoor Positioning (0x1821) | 0x1802-0x1821 |
| Device Information | Device Information (0x180A), Battery Service (0x180F) | 0x180A-0x180F |
| Automation | Automation IO (0x1815), Environmental Sensing (0x181A) | 0x1815-0x181A |
| Audio (LE Audio) | Common Audio, Media Control, Telephony and Media Audio | Bluetooth 5.2+ |

**GATT hierarchy**: A GATT server exposes Services (collections of related data), each containing Characteristics (individual data values with read/write/notify properties), which may have Descriptors (metadata like format, range, or presentation). A heart rate monitor's Heart Rate Service (0x180D) contains a Heart Rate Measurement characteristic (0x2A37) that sends notifications at each heartbeat.

Learn more: [Profile Reference](https://blefyi.com/profile/) | [Use Cases](https://blefyi.com/use-case/)

### Bluetooth Versions (4.0-5.4)

Each Bluetooth version introduces significant protocol enhancements. Understanding version differences is critical for chip selection and firmware development:

| Version | Year | Key Features | Impact |
|---------|------|-------------|--------|
| 4.0 | 2010 | BLE introduction, GATT/ATT, 1 Mbps PHY | Created the IoT ecosystem |
| 4.1 | 2013 | Dual-mode topology, L2CAP CoC, LTE coexistence | Hub/spoke + mesh topologies |
| 4.2 | 2014 | LE Data Length Extension (251B), LE Secure Connections, IPv6 | 2.5x throughput, stronger encryption |
| 5.0 | 2016 | 2 Mbps LE 2M PHY, LE Coded PHY (long range), 8x advertising | Double speed or 4x range |
| 5.1 | 2019 | Direction Finding (AoA/AoD), GATT Caching | Sub-meter indoor positioning |
| 5.2 | 2020 | LE Audio (LC3 codec), Isochronous Channels, EATT | Hearing aids, Auracast broadcast |
| 5.3 | 2021 | Connection Subrating, Channel Classification Enhancement | Dynamic power optimization |
| 5.4 | 2023 | PAwR (Periodic Advertising with Responses), Encrypted Advertising | Electronic shelf labels |

**LE Coded PHY (Bluetooth 5.0)**: Trades data rate (125 kbps or 500 kbps) for dramatically increased range through Forward Error Correction (FEC). In open-air tests, LE Coded PHY achieves reliable communication at 1 km+ versus ~100 m for LE 1M PHY -- enabling agricultural sensors, campus-wide asset tracking, and rural IoT deployments.

Learn more: [Version History](https://blefyi.com/version/) | [Glossary](https://blefyi.com/glossary/)

### Beacon Protocols

Beacons are BLE devices that broadcast advertising packets at regular intervals for proximity detection, indoor positioning, and context-aware applications:

| Protocol | Creator | Advertising Format | Identifier | Range |
|----------|---------|-------------------|------------|-------|
| iBeacon | Apple | Manufacturer-specific (0x004C) | UUID + Major + Minor | ~70m |
| Eddystone | Google | 4 frame types (UID, URL, TLM, EID) | 10B namespace + 6B instance | ~70m |
| AltBeacon | Radius Networks | Open specification | 20-byte beacon ID | ~70m |

**iBeacon** dominates retail proximity marketing with a simple UUID/Major/Minor addressing scheme. A single UUID identifies the organization, Major identifies the store location, and Minor identifies the specific shelf or zone. iOS apps receive beacon region entry/exit events even when backgrounded.

### BLE vs Bluetooth Classic

| Feature | Bluetooth Low Energy | Bluetooth Classic |
|---------|---------------------|-------------------|
| Power Consumption | ~0.01-0.5W (coin cell for years) | ~1W (regular charging) |
| Data Rate | 1-2 Mbps (LE 1M/2M PHY) | 1-3 Mbps (EDR) |
| Range | 100m+ (Coded PHY: 1km+) | ~100m |
| Latency | ~3ms connection | ~100ms connection |
| Topology | Point-to-point, broadcast, mesh | Point-to-point, piconet (7 active) |
| Audio | LE Audio (LC3, Auracast broadcast) | A2DP (SBC, AAC, aptX) |
| Use Cases | Sensors, wearables, beacons, IoT | Audio streaming, file transfer |

### Advertising Modes

BLE devices communicate their presence through advertising packets on three dedicated channels (37, 38, 39 at 2402, 2426, 2480 MHz):

| Mode | Connectable | Scannable | Use Case |
|------|------------|-----------|----------|
| ADV_IND | Yes | Yes | Default -- discoverable and connectable |
| ADV_DIRECT_IND | Yes (directed) | No | Fast reconnection to known central |
| ADV_NONCONN_IND | No | No | Beacons, broadcast-only |
| ADV_SCAN_IND | No | Yes | Additional data via scan response |
| Extended (BT 5.0+) | Configurable | Configurable | 255 bytes/PDU, secondary channels |

### BLE Mesh Networking

Bluetooth Mesh (adopted 2017) enables many-to-many device communication using a managed flood relay architecture. Nodes publish/subscribe to addresses, relay nodes forward messages across the network, and proxy nodes bridge BLE Mesh to standard GATT clients. Key applications include commercial lighting control (up to 32,000 nodes), building automation, and industrial sensor networks.

| Mesh Feature | Specification |
|-------------|---------------|
| Max Nodes | 32,767 per network |
| Topology | Managed flood relay |
| Security | Network key + Application key + Device key (AES-CCM) |
| Provisioning | PB-ADV (advertising) or PB-GATT (connection) |
| Models | Generic OnOff, Level, Lighting, Sensor |

Learn more: [Beacon Protocols](https://blefyi.com/beacon/) | [Use Cases](https://blefyi.com/use-case/)

## API Endpoints

Free, no authentication required. JSON responses with CORS enabled.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/chip/{slug}/` | BLE chip detail with specs |
| GET | `/api/profile/{slug}/` | GATT profile with characteristics |
| GET | `/api/version/{slug}/` | Bluetooth version detail |
| GET | `/api/beacon/{slug}/` | Beacon protocol detail |
| GET | `/api/usecase/{slug}/` | Use case with related chips |
| GET | `/api/manufacturer/{slug}/` | Manufacturer with chip lineup |
| GET | `/api/term/{slug}/` | Glossary term definition |
| GET | `/api/search/?q={query}` | Search across all content types |
| GET | `/api/compare/?a={slug}&b={slug}` | Compare two chips |
| GET | `/api/random/` | Random chip discovery |
| GET | `/api/openapi.json` | OpenAPI 3.1.0 specification |

### Example

```bash
# Search for Nordic BLE chips
curl -s "https://blefyi.com/api/search/?q=nordic" | python -m json.tool
```

Full API documentation at [blefyi.com/api/](https://blefyi.com/api/).
OpenAPI 3.1.0 spec: [blefyi.com/api/openapi.json](https://blefyi.com/api/openapi.json).

## Command-Line Interface

```bash
blefyi search "nrf52"                 # Search all content
blefyi chip nrf52840                  # Chip detail
blefyi compare nrf52840 esp32-c3      # Side-by-side comparison
blefyi random                         # Discover a random chip
```

## MCP Server (Claude, Cursor, Windsurf)

```json
{
    "mcpServers": {
        "blefyi": {
            "command": "uvx",
            "args": ["--from", "blefyi[mcp]", "python", "-m", "blefyi.mcp_server"]
        }
    }
}
```

Tools: `ble_search`, `ble_lookup`, `ble_compare`

## REST API Client

```python
from blefyi.api import BLEFYI

with BLEFYI() as api:
    api.search("nordic")                       # Full-text search
    api.chip("nrf52840")                       # Chip detail
    api.profile("heart-rate")                  # GATT profile
    api.version("5-0")                         # Bluetooth version
    api.beacon("ibeacon")                      # Beacon protocol
    api.usecase("asset-tracking")              # Use case
    api.manufacturer("nordic-semiconductor")   # Manufacturer
    api.glossary_term("gatt")                  # Glossary term
    api.compare("nrf52840", "esp32-c3")        # Compare two chips
    api.random()                               # Random discovery
    api.openapi()                              # OpenAPI 3.1.0 spec
```

## Learn More About BLE

- **Browse**: [Chip Explorer](https://blefyi.com/chip/) · [Profile Reference](https://blefyi.com/profile/) · [Beacon Protocols](https://blefyi.com/beacon/)
- **Reference**: [Version History](https://blefyi.com/version/) · [Use Cases](https://blefyi.com/use-case/) · [Glossary](https://blefyi.com/glossary/)
- **API**: [REST API Docs](https://blefyi.com/api/) · [OpenAPI Spec](https://blefyi.com/api/openapi.json)

## Also Available

| Platform | Install | Link |
|----------|---------|------|
| **npm** | `npm install blefyi` | [npm](https://www.npmjs.com/package/blefyi) |
| **Go** | `go get github.com/fyipedia/blefyi-go` | [pkg.go.dev](https://pkg.go.dev/github.com/fyipedia/blefyi-go) |
| **Rust** | `cargo add blefyi` | [crates.io](https://crates.io/crates/blefyi) |
| **Ruby** | `gem install blefyi` | [rubygems.org](https://rubygems.org/gems/blefyi) |
| **MCP** | `uvx --from "blefyi[mcp]" python -m blefyi.mcp_server` | [Config](#mcp-server-claude-cursor-windsurf) |

## Tag FYI Family

Part of the [FYIPedia](https://fyipedia.com) open-source developer tools ecosystem -- automatic identification and data capture technologies.

| Site | Domain | Focus |
|------|--------|-------|
| BarcodeFYI | [barcodefyi.com](https://barcodefyi.com) | 518 records -- barcode symbologies, standards, GS1 prefixes |
| QRCodeFYI | [qrcodefyi.com](https://qrcodefyi.com) | 425 records -- QR code types, versions, encoding modes |
| NFCFYI | [nfcfyi.com](https://nfcfyi.com) | 288 records -- NFC chips, NDEF records, standards |
| **BLEFYI** | [blefyi.com](https://blefyi.com) | **261 records -- BLE chips, GATT profiles, beacons** |
| RFIDFYI | [rfidfyi.com](https://rfidfyi.com) | 318 records -- RFID tags, frequency bands, EPC schemes |
| SmartCardFYI | [smartcardfyi.com](https://smartcardfyi.com) | 280 records -- smart cards, EMV, Java Card, platforms |

## FYIPedia Developer Tools

| Package | PyPI | npm | Description |
|---------|------|-----|-------------|
| barcodefyi | [PyPI](https://pypi.org/project/barcodefyi/) | [npm](https://www.npmjs.com/package/barcodefyi) | Barcode symbologies, standards -- [barcodefyi.com](https://barcodefyi.com) |
| qrcodefyi | [PyPI](https://pypi.org/project/qrcodefyi/) | [npm](https://www.npmjs.com/package/qrcodefyi) | QR code types, versions, encoding -- [qrcodefyi.com](https://qrcodefyi.com) |
| nfcfyi | [PyPI](https://pypi.org/project/nfcfyi/) | [npm](https://www.npmjs.com/package/nfcfyi) | NFC chips, NDEF, standards -- [nfcfyi.com](https://nfcfyi.com) |
| **blefyi** | [PyPI](https://pypi.org/project/blefyi/) | [npm](https://www.npmjs.com/package/blefyi) | **BLE profiles, beacons, chips -- [blefyi.com](https://blefyi.com)** |
| rfidfyi | [PyPI](https://pypi.org/project/rfidfyi/) | [npm](https://www.npmjs.com/package/rfidfyi) | RFID tags, readers, frequencies -- [rfidfyi.com](https://rfidfyi.com) |
| smartcardfyi | [PyPI](https://pypi.org/project/smartcardfyi/) | [npm](https://www.npmjs.com/package/smartcardfyi) | Smart cards, EMV, platforms -- [smartcardfyi.com](https://smartcardfyi.com) |

## Embed Widget

Embed [BLEFYI](https://blefyi.com) widgets on any website with [blefyi-embed](https://widget.blefyi.com):

```html
<script src="https://cdn.jsdelivr.net/npm/blefyi-embed@1/dist/embed.min.js"></script>
<div data-blefyi="entity" data-slug="example"></div>
```

Zero dependencies · Shadow DOM · 4 themes (light/dark/sepia/auto) · [Widget docs](https://widget.blefyi.com)

## License

MIT
