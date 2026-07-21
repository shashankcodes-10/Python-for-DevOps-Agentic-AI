# using psutl library

import psutil

CPU = psutil.cpu_percent(interval=1)
Memory = psutil.virtual_memory().percent
Disk = psutil.disk_usage("/").percent

print(f"the CPU Usage is {CPU}")
print(f"the Memory Usage is {Memory}")
print(f"the Disk Usage is {Disk}")