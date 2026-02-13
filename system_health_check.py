#!/usr/bin/env python3

import platform
import psutil
from datetime import datetime


def get_system_info():
    return {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor()
    }


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    memory = psutil.virtual_memory()
    return {
        "Total": round(memory.total / (1024 ** 3), 2),
        "Used": round(memory.used / (1024 ** 3), 2),
        "Percentage": memory.percent
    }


def get_disk_usage():
    disk = psutil.disk_usage('/')
    return {
        "Total": round(disk.total / (1024 ** 3), 2),
        "Used": round(disk.used / (1024 ** 3), 2),
        "Percentage": disk.percent
    }


def get_top_processes(limit=5):
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            processes.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    processes = sorted(processes, key=lambda x: x['cpu_percent'], reverse=True)
    return processes[:limit]


def generate_report():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report_lines = []
    report_lines.append(f"System Health Report - {now}")
    report_lines.append("=" * 50)

    # System Info
    system_info = get_system_info()
    report_lines.append("\n[System Information]")
    for key, value in system_info.items():
        report_lines.append(f"{key}: {value}")

    # CPU
    report_lines.append("\n[CPU Usage]")
    report_lines.append(f"CPU Usage: {get_cpu_usage()}%")

    # Memory
    memory = get_memory_usage()
    report_lines.append("\n[Memory Usage]")
    report_lines.append(f"Total: {memory['Total']} GB")
    report_lines.append(f"Used: {memory['Used']} GB")
    report_lines.append(f"Usage: {memory['Percentage']}%")

    # Disk
    disk = get_disk_usage()
    report_lines.append("\n[Disk Usage]")
    report_lines.append(f"Total: {disk['Total']} GB")
    report_lines.append(f"Used: {disk['Used']} GB")
    report_lines.append(f"Usage: {disk['Percentage']}%")

    # Top Processes
    report_lines.append("\n[Top Processes by CPU Usage]")
    top_processes = get_top_processes()
    for proc in top_processes:
        report_lines.append(
            f"PID: {proc['pid']} | Name: {proc['name']} | CPU: {proc['cpu_percent']}%"
        )

    return "\n".join(report_lines)


def save_report(report, filename="system_health_report.txt"):
    with open(filename, "w") as file:
        file.write(report)


if __name__ == "__main__":
    report = generate_report()
    print(report)
    save_report(report)
