#!/usr/bin/env python3

"""
A simple network diagnostic tool for IT support purposes.

Features:
- Displays local IP address
- Tests internet connectivity
- Resolves DNS for a given host
- Performs a ping test

Author: Gabriel
"""

import socket
import subprocess
import platform
from datetime import datetime


def get_local_ip():
    """Returns the local IP address."""
    try:
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        return local_ip
    except Exception as e:
        return f"Error getting local IP: {e}"


def test_internet_connectivity():
    """Tests connection to a well-known host (Google DNS)."""
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=5)
        return "Internet connectivity: OK"
    except OSError:
        return "Internet connectivity: FAILED"


def resolve_dns(host="google.com"):
    """Resolves DNS for a given hostname."""
    try:
        resolved_ip = socket.gethostbyname(host)
        return f"{host} resolved to {resolved_ip}"
    except Exception as e:
        return f"DNS resolution failed for {host}: {e}"


def ping_host(host="8.8.8.8"):
    """Pings a host depending on OS."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "4", host]

    try:
        output = subprocess.run(
            command,
            capture_output=True,
            text=True
        )
        return output.stdout
    except Exception as e:
        return f"Ping failed: {e}"


def main():
    print("=" * 50)
    print("Network Diagnostics Tool")
    print(f"Run at: {datetime.now()}")
    print("=" * 50)

    print("\n[1] Local IP Address:")
    print(get_local_ip())

    print("\n[2] Internet Connectivity Test:")
    print(test_internet_connectivity())

    print("\n[3] DNS Resolution Test:")
    print(resolve_dns())

    print("\n[4] Ping Test:")
    print(ping_host())

    print("\nDiagnostics completed.")


if __name__ == "__main__":
    main()
