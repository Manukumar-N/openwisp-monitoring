# NetJSON DeviceMonitoring schema,
# https://github.com/netjson/netjson/blob/master/schema/device-monitoring.json
schema = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "https://raw.githubusercontent.com/netjson/netjson/master/schema/device-monitoring.json",
    "title": "NetJSON Device Monitoring",
    "description": "Monitoring information sent by a device.",
    "type": "object",
    "additionalProperties": True,
    "required": ["type"],
    "properties": {
        "type": {"type": "string", "enum": ["DeviceMonitoring"]},
        "general": {
            "type": "object",
            "title": "General",
            "additionalProperties": True,
            "properties": {
                "local_time": {"type": "integer"},
                "uptime": {"type": "integer"},
            },
        },
        "resources": {
            "type": "object",
            "title": "Resources",
            "additionalProperties": True,
            "properties": {
                "load": {
                    "type": "array",
                    "items": {"type": "number", "minItems": 3, "maxItems": 3},
                },
                "cpus": {"type": "integer"},
                "memory": {
                    "id": "memory",
                    "type": "object",
                    "properties": {
                        "total": {"type": "integer"},
                        "free": {"type": "integer"},
                        "buffered": {"type": "integer"},
                        "cached": {"type": "integer"},
                        "shared": {"type": "integer"},
                        "available": {"type": "integer"},
                    },
                    "required": ["total", "free", "buffered", "shared"],
                },
                "disk": {
                    "type": "array",
                    "additionalItems": False,
                    "title": "Disks",
                    "items": {
                        "type": "object",
                        "title": "Disk",
                        "additionalProperties": False,
                        "properties": {
                            "mount_point": {"type": "string"},
                            "filesystem": {"type": "string"},
                            "used_bytes": {"type": "integer"},
                            "available_bytes": {"type": "integer"},
                            "used_percent": {"type": "integer"},
                            "size_bytes": {"type": "integer"},
                        },
                        "required": [
                            "mount_point",
                            "filesystem",
                            "used_bytes",
                            "available_bytes",
                            "used_percent",
                            "size_bytes",
                        ],
                    },
                },
                "swap": {
                    "type": "object",
                    "properties": {
                        "total": {"type": "integer"},
                        "free": {"type": "integer"},
                    },
                },
                "connections": {
                    "type": "object",
                    "properties": {
                        "ipv4": {
                            "type": "object",
                            "properties": {
                                "tcp": {"type": "integer"},
                                "udp": {"type": "integer"},
                            },
                        },
                        "ipv6": {
                            "type": "object",
                            "properties": {
                                "tcp": {"type": "integer"},
                                "udp": {"type": "integer"},
                            },
                        },
                    },
                },
                "processes": {
                    "type": "object",
                    "properties": {
                        "running": {"type": "integer"},
                        "sleeping": {"type": "integer"},
                        "blocked": {"type": "integer"},
                        "zombie": {"type": "integer"},
                        "stopped": {"type": "integer"},
                        "paging": {"type": "integer"},
                    },
                },
                "cpu": {
                    "type": "object",
                    "properties": {
                        "frequency": {"type": "integer"},
                        "user": {"type": "integer"},
                        "system": {"type": "integer"},
                        "nice": {"type": "integer"},
                        "idle": {"type": "integer"},
                        "iowait": {"type": "integer"},
                        "irq": {"type": "integer"},
                        "softirq": {"type": "integer"},
                    },
                },
                "flash": {
                    "type": "object",
                    "properties": {
                        "total": {"type": "integer"},
                        "free": {"type": "integer"},
                    },
                },
                "storage": {
                    "type": "object",
                    "properties": {
                        "total": {"type": "integer"},
                        "free": {"type": "integer"},
                    },
                },
            },
        },
        "interfaces": {
            "type": "array",
            "title": "Interfaces",
            "uniqueItems": True,
            "additionalItems": False,
            "items": {
                "type": "object",
                "title": "Interface",
                "additionalProperties": True,
                "required": ["name"],
                "properties": {
                    "name": {"type": "string"},
                    "type": {"type": "string"},
                    "uptime": {"type": "integer"},
                    "up": {"type": "boolean"},
                    "mac": {"type": "string"},
                    "mtu": {"type": "integer"},
                    "txqueuelen": {"type": "integer"},
                    "speed": {"type": "string"},
                    "multicast": {"type": "boolean"},
                    "bridge_members": {
                        "type": "array",
                        "items": {"type": "string"},
                        "additionalItems": False,
                    },
                    "stp": {"type": "boolean"},
                    "statistics": {
                        "type": "object",
                        "properties": {
                            "collisions": {"type": "integer"},
                            "rx_frame_errors": {"type": "integer"},
                            "tx_compressed": {"type": "integer"},
                            "multicast": {"type": "integer"},
                            "rx_length_errors": {"type": "integer"},
                            "tx_dropped": {"type": "integer"},
                            "rx_bytes": {"type": "integer"},
                            "rx_missed_errors": {"type": "integer"},
                            "tx_errors": {"type": "integer"},
                            "rx_compressed": {"type": "integer"},
                            "rx_over_errors": {"type": "integer"},
                            "tx_fifo_errors": {"type": "integer"},
                            "rx_crc_errors": {"type": "integer"},
                            "rx_packets": {"type": "integer"},
                            "tx_heartbeat_errors": {"type": "integer"},
                            "rx_dropped": {"type": "integer"},
                            "tx_aborted_errors": {"type": "integer"},
                            "tx_packets": {"type": "integer"},
                            "rx_errors": {"type": "integer"},
                            "tx_bytes": {"type": "integer"},
                            "tx_window_errors": {"type": "integer"},
                            "rx_fifo_errors": {"type": "integer"},
                            "tx_carrier_errors": {"type": "integer"},
                        },
                    },
                    "wireless": {
                        "type": "object",
                        "additionalProperties": True,
                        "required": [
                            "channel",
                            "country",
                            "frequency",
                            "mode",
                            "noise",
                            "ssid",
                            "tx_power",
                        ],
                        "properties": {
                            "channel": {"type": "integer"},
                            "country": {"type": "string"},
                            "frequency": {"type": "integer"},
                            "mode": {"type": "string"},
                            "noise": {"type": "integer"},
                            "signal": {"type": "integer"},
                            "ssid": {"type": "string"},
                            "tx_power": {"type": "integer"},
                            "htmode": {"type": "string"},
                            "clients": {
                                "type": "array",
                                "title": "Wireless Clients",
                                "additionalItems": False,
                                "items": {
                                    "type": "object",
                                    "title": "Client",
                                    "additionalProperties": True,
                                    "required": [
                                        "auth",
                                        "authorized",
                                        "ht",
                                        "vht",
                                        "wmm",
                                        "mac",
                                        "mfp",
                                    ],
                                    "properties": {
                                        "aid": {"type": "integer"},
                                        "singal": {"type": "integer"},
                                        "noise": {"type": "integer"},
                                        "assoc": {"type": "boolean"},
                                        "auth": {"type": "boolean"},
                                        "authorized": {"type": "boolean"},
                                        "ht": {"type": "boolean"},
                                        "vht": {"type": "boolean"},
                                        "wds": {"type": "boolean"},
                                        "wmm": {"type": "boolean"},
                                        "wps": {"type": "boolean"},
                                        "mac": {"type": "string"},
                                        "vendor": {"type": "string"},
                                        "mfp": {"type": "boolean"},
                                        "preauth": {"type": "boolean"},
                                        "signature": {"type": "string"},
                                        "rrm": {
                                            "type": "array",
                                            "minItems": 5,
                                            "maxItems": 5,
                                            "items": {"type": "integer"},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "mobile": {
                        "type": "object",
                        "additionalProperties": True,
                        "required": [
                            "imei",
                            "operator_code",
                            "operator_name",
                            "connection_status",
                            "power_status",
                            "manufacturer",
                            "model",
                        ],
                        "properties": {
                            "imei": {
                                "type": "string",
                                "minLength": 15,
                                "maxLength": 17,
                                "pattern": "^[0-9]*$",
                            },
                            "operator_name": {"type": "string"},
                            "operator_code": {
                                "type": "string",
                                "minLength": 4,
                                "maxLength": 6,
                                "pattern": "^[0-9]*$",
                            },
                            "connection_status": {"type": "string"},
                            "power_status": {"type": "string"},
                            "manufacturer": {"type": "string"},
                            "model": {"type": "string"},
                            "signal": {
                                "type": "object",
                                "additionalProperties": True,
                                "properties": {
                                    "gsm": {
                                        "type": "object",
                                        "additionalProperties": True,
                                        "required": ["rssi"],
                                        "properties": {"rssi": {"type": "number"}},
                                    },
                                    "cdma1x": {
                                        "type": "object",
                                        "additionalProperties": True,
                                        "required": ["rssi", "ecio"],
                                        "properties": {
                                            "rssi": {"type": "number"},
                                            "ecio": {"type": "number"},
                                        },
                                    },
                                    "evdo": {
                                        "type": "object",
                                        "additionalProperties": True,
                                        "required": ["rssi", "ecio", "io", "sinr"],
                                        "properties": {
                                            "rssi": {"type": "number"},
                                            "ecio": {"type": "number"},
                                            "io": {"type": "number"},
                                            "sinr": {"type": "number"},
                                        },
                                    },
                                    "umts": {
                                        "type": "object",
                                        "additionalProperties": True,
                                        "required": ["ecio"],
                                        "properties": {
                                            "rssi": {"type": "number"},
                                            "rscp": {"type": "number"},
                                            "ecio": {"type": "number"},
                                        },
                                    },
                                    "lte": {
                                        "type": "object",
                                        "additionalProperties": True,
                                        "required": ["rssi", "rsrp", "rsrq", "snr"],
                                        "properties": {
                                            "rssi": {"type": "number"},
                                            "rsrp": {"type": "number"},
                                            "rsrq": {"type": "number"},
                                            "snr": {"type": "number"},
                                        },
                                    },
                                    "5g": {
                                        "type": "object",
                                        "additionalProperties": True,
                                        "required": ["rsrp", "rsrq", "snr"],
                                        "properties": {
                                            "rsrp": {"type": "number"},
                                            "rsrq": {"type": "number"},
                                            "snr": {"type": "number"},
                                        },
                                    },
                                },
                            },
                        },
                    },
                    "addresses": {
                        "type": "array",
                        "title": "Addresses",
                        "uniqueItems": True,
                        "additionalItems": False,
                        "items": {
                            "additionalProperties": True,
                            "title": "Address",
                            "type": "object",
                            "required": ["proto", "family", "address", "mask"],
                            "properties": {
                                "proto": {"type": "string"},
                                "family": {"type": "string"},
                                "address": {
                                    "type": "string",
                                    "anyOf": [{"format": "ipv4"}, {"format": "ipv6"}],
                                },
                                "mask": {"type": "integer"},
                            },
                        },
                    },
                },
            },
        },
        "dhcp_leases": {
            "type": "array",
            "title": "DHCP leases",
            "additionalItems": False,
            "items": {
                "type": "object",
                "title": "DHCP lease",
                "additionalProperties": False,
                "properties": {
                    "expiry": {"type": "number"},
                    "ip": {
                        "type": "string",
                        "anyOf": [{"format": "ipv4"}, {"format": "ipv6"}],
                    },
                    "mac": {"type": "string"},
                    "vendor": {"type": "string"},
                    "client_name": {"type": "string"},
                    "client_id": {"type": "string"},
                },
                "required": ["expiry", "ip", "mac", "client_name", "client_id"],
            },
        },
        "neighbors": {
            "type": "array",
            "title": "Neighbors",
            "additionalItems": False,
            "items": {
                "type": "object",
                "title": "Neighbor",
                "additionalProperties": False,
                "properties": {
                    "ip": {
                        "type": "string",
                        "anyOf": [{"format": "ipv4"}, {"format": "ipv6"}],
                    },
                    "mac": {"type": "string"},
                    "vendor": {"type": "string"},
                    "interface": {"type": "string"},
                    "state": {"type": "string"},
                },
                "required": ["ip", "interface"],
            },
        },
    },
}