# Python-Skript für Systemressourcen (CPU, RAM, Disk.)

### psutil & datetime importieren:
```python
import psutil
import datetime
```
### CPU-Auslastung in Prozent
```python
def get_system_metrics():
    cpu_usage = psutil.cpu_percent(interval=1)
