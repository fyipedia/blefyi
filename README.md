# blefyi

[![PyPI](https://img.shields.io/pypi/v/blefyi)](https://pypi.org/project/blefyi/)
[![Python](https://img.shields.io/pypi/pyversions/blefyi)](https://pypi.org/project/blefyi/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Bluetooth Low Energy encyclopedia API client for Python. Look up BLE chips, GATT profiles, Bluetooth versions 4.0-5.4, beacon protocols, and IoT specifications from [BLEFYI](https://blefyi.com) -- the comprehensive BLE reference covering Nordic nRF, Espressif ESP32, Texas Instruments CC26xx, Dialog DA14xxx, Silicon Labs EFR32, and every major BLE system-on-chip in commercial and industrial use.

> **Explore BLE at [blefyi.com](https://blefyi.com)** -- [Chip Explorer](https://blefyi.com/chip/) | [Profile Reference](https://blefyi.com/profile/) | [Version History](https://blefyi.com/version/) | [Beacon Protocols](https://blefyi.com/beacon/)

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
    print(nrf["name"], nrf["manufacturer"])

    # Compare two BLE chips
    diff = api.compare("nrf52840", "esp32-c3")
    print(diff)

    # Discover a random BLE chip
    surprise = api.random()
    print(surprise["name"])
```

## What You'll Find on BLEFYI

BLEFYI is a comprehensive Bluetooth Low Energy encyclopedia covering BLE chips, GATT profiles, Bluetooth versions, beacon protocols, manufacturers, and IoT use cases. Bluetooth Low Energy (BLE), introduced as part of the Bluetooth 4.0 Core Specification in 2010, is a wireless personal area network technology designed for short-range, low-power communication -- the foundation of wearable fitness trackers, medical devices, asset tracking, smart home automation, and industrial IoT worldwide.

### BLE Chips & System-on-Chip (SoC)

BLE chips are the silicon at the heart of every Bluetooth Low Energy device. Each SoC integrates a radio transceiver, ARM Cortex-M processor, RAM, flash memory, and peripheral interfaces into a single package. Key specifications include Bluetooth version support, TX power (dBm), receiver sensitivity, RAM/flash capacity, GPIO count, and supported protocols (BLE, Zigbee, Thread, Matter).

| Manufacturer | Key Chips | Bluetooth | Notable Feature |
|-------------|-----------|-----------|-----------------|
| Nordic Semiconductor | nRF52840, nRF52832, nRF5340 | 5.0-5.3 | Best-in-class SDK (nRF Connect) |
| Espressif | ESP32-C3, ESP32-C6, ESP32-H2 | 5.0-5.3 | Wi-Fi + BLE combo, open-source |
| Texas Instruments | CC2640R2F, CC2652R | 5.0-5.1 | Ultra-low power, medical-grade |
| Dialog Semiconductor | DA14695, DA14531 | 5.1-5.2 | Smallest BLE SoC (DA14531) |
| Silicon Labs | EFR32BG22, EFR32BG24 | 5.2-5.3 | Direction Finding, Bluetooth Mesh |
| Qualcomm | QCC5144, QCC3056 | 5.2-5.3 | LE Audio, LC3 codec |
| STMicroelectronics | STM32WB55, BlueNRG-2 | 5.0-5.3 | STM32 ecosystem integration |

### GATT Profiles & Services

The Generic Attribute Profile (GATT) defines how BLE devices expose structured data through a hierarchy of services, characteristics, and descriptors. The Bluetooth SIG maintains adopted profiles that ensure interoperability across manufacturers -- any BLE heart rate monitor speaks the same GATT language regardless of chipset.

| Profile Category | Examples | UUID Range |
|-----------------|----------|------------|
| Health & Fitness | Heart Rate, Blood Pressure, Glucose, Body Composition | 0x180D-0x181F |
| HID & Input | Human Interface Device, Scan Parameters | 0x1812, 0x1813 |
| Proximity & Location | Immediate Alert, Tx Power, Link Loss, Indoor Positioning | 0x1802-0x1821 |
| Device Information | Device Information, Battery Service | 0x180A, 0x180F |
| Automation | Automation IO, Environmental Sensing | 0x1815, 0x181A |
| Audio (LE Audio) | Common Audio, Media Control, Telephony | Bluetooth 5.2+ |

### Bluetooth Versions (4.0 - 5.4)

Each Bluetooth version introduces significant protocol enhancements. Understanding version differences is critical for chip selection and firmware development.

| Version | Year | Key Features |
|---------|------|-------------|
| 4.0 | 2010 | BLE introduction, GATT/ATT, 1 Mbps PHY, 2.4 GHz ISM band |
| 4.1 | 2013 | Dual-mode topology, L2CAP CoC, coexistence with LTE |
| 4.2 | 2014 | LE Data Length Extension (251 bytes), LE Secure Connections, IPv6/6LoWPAN |
| 5.0 | 2016 | 2 Mbps LE PHY, LE Coded PHY (long range), 8x advertising capacity |
| 5.1 | 2019 | Direction Finding (AoA/AoD), GATT Caching, periodic advertising sync |
| 5.2 | 2020 | LE Audio (LC3 codec), Isochronous Channels, Enhanced ATT |
| 5.3 | 2021 | Connection Subrating, Channel Classification Enhancement, periodic advertising enhancement |
| 5.4 | 2023 | PAwR (Periodic Advertising with Responses), Encrypted Advertising Data |

### Beacon Protocols

Beacons are BLE devices that broadcast advertising packets at regular intervals for proximity detection, indoor positioning, and context-aware applications.

| Protocol | Creator | Advertising Format | UUID/Namespace | Range |
|----------|---------|-------------------|----------------|-------|
| iBeacon | Apple | Manufacturer-specific (0x004C) | UUID + Major + Minor | ~70m |
| Eddystone | Google | 4 frame types (UID, URL, TLM, EID) | 10-byte namespace + 6-byte instance | ~70m |
| AltBeacon | Radius Networks | Open specification | 20-byte beacon ID | ~70m |

### BLE vs Bluetooth Classic

| Feature | Bluetooth Low Energy | Bluetooth Classic |
|---------|---------------------|-------------------|
| Power Consumption | ~0.01-0.5W (coin cell for years) | ~1W (regular charging) |
| Data Rate | 1-2 Mbps (LE 1M/2M PHY) | 1-3 Mbps (EDR) |
| Range | 100m+ (Coded PHY: 1km+) | ~100m |
| Latency | ~3ms connection | ~100ms connection |
| Topology | Point-to-point, broadcast, mesh | Point-to-point, piconet |
| Audio | LE Audio (LC3, Auracast) | A2DP (SBC, AAC, aptX) |
| Use Cases | Sensors, wearables, beacons, IoT | Audio streaming, file transfer |

### Advertising Modes

BLE devices communicate their presence through advertising packets broadcast on three dedicated channels (37, 38, 39). Understanding advertising modes is essential for optimizing discovery latency, power consumption, and data throughput.

- **Connectable Undirected**: Default mode -- device is discoverable and accepts connections from any central
- **Connectable Directed**: Fast reconnection to a known central (1.28s timeout)
- **Non-connectable Undirected**: Broadcast-only (beacons), no connections accepted
- **Scannable Undirected**: Allows scan requests for additional data (scan response)
- **Extended Advertising** (Bluetooth 5.0+): Up to 255 bytes per PDU, secondary channels, chained PDUs

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

```bash
# Example: search for Nordic BLE chips
curl -s "https://blefyi.com/api/search/?q=nordic" | python -m json.tool
```

## Command-Line Interface

```bash
blefyi search "nrf52"
blefyi chip nrf52840
blefyi compare nrf52840 esp32-c3
blefyi random
```

## MCP Server (Claude, Cursor, Windsurf)

```json
{
    "mcpServers": {
        "blefyi": {
            "command": "python",
            "args": ["-m", "blefyi.mcp_server"]
        }
    }
}
```

Tools: `ble_search`, `ble_lookup`, `ble_compare`

## API Client

```python
from blefyi.api import BLEFYI

with BLEFYI() as api:
    # All 11 endpoints
    api.search("nordic")
    api.chip("nrf52840")
    api.profile("heart-rate")
    api.version("5-0")
    api.beacon("ibeacon")
    api.usecase("asset-tracking")
    api.manufacturer("nordic-semiconductor")
    api.glossary_term("gatt")
    api.compare("nrf52840", "esp32-c3")
    api.random()
    api.openapi()
```

## Also Available

| Language | Package | Install |
|----------|---------|---------|
| Python | [blefyi](https://pypi.org/project/blefyi/) | `pip install blefyi` |
| TypeScript | [blefyi](https://www.npmjs.com/package/blefyi) | `npm install blefyi` |
| Go | [blefyi-go](https://pkg.go.dev/github.com/fyipedia/blefyi-go) | `go get github.com/fyipedia/blefyi-go` |
| Rust | [blefyi](https://crates.io/crates/blefyi) | `cargo add blefyi` |
| Ruby | [blefyi](https://rubygems.org/gems/blefyi) | `gem install blefyi` |

## Code FYI Family

| Site | Domain | Focus |
|------|--------|-------|
| BarcodeFYI | [barcodefyi.com](https://barcodefyi.com) | Barcode symbologies & standards |
| QRCodeFYI | [qrcodefyi.com](https://qrcodefyi.com) | QR code types & encoding |
| NFCFYI | [nfcfyi.com](https://nfcfyi.com) | NFC tags & NDEF records |
| BLEFYI | [blefyi.com](https://blefyi.com) | Bluetooth Low Energy profiles |
| RFIDFYI | [rfidfyi.com](https://rfidfyi.com) | RFID tags & frequency bands |
| SmartCardFYI | [smartcardfyi.com](https://smartcardfyi.com) | Smart card types & platforms |

## License

MIT
