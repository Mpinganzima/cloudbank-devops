import psutil
import json
from datetime import datetime
from pathlib import Path

print("=" * 60)
print("CloudBank Enterprise System Monitor")
print("=" * 60)

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory()
disk = psutil.disk_usage("/")

report = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "cpu_percent": cpu,
    "memory_percent": memory.percent,
    "disk_percent": disk.percent
}

print(f"CPU Usage     : {cpu}%")
print(f"Memory Usage  : {memory.percent}%")
print(f"Disk Usage    : {disk.percent}%")

logs_dir = Path("python/logs")
logs_dir.mkdir(parents=True, exist_ok=True)

with open(logs_dir / "system_report.json", "w") as f:
    json.dump(report, f, indent=4)

print("\nSystem report saved successfully.")