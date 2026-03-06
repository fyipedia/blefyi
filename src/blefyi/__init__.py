"""blefyi -- Bluetooth Low Energy encyclopedia API client for developers.

Look up BLE chips, GATT profiles, Bluetooth versions, beacon protocols, and IoT specs from BLEFYI.

Usage::

    from blefyi.api import BLEFYI

    with BLEFYI() as api:
        results = api.search("nordic")
        print(results)
"""

__version__ = "0.1.0"
