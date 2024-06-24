import psutil
import datetime
import os

def get_system_metrics():
    # CPU-Auslastung in Prozent
    cpu_usage = psutil.cpu_percent(interval=1)
    
    # RAM-Nutzung
    memory = psutil.virtual_memory()
    ram_total = memory.total
    ram_used = memory.used
    ram_free =  memory.free
    
    # Festplattennutzung
    disk =  psutil.disk_usage('/')
    disk_total = disk.total
    disk_used = disk.used
    disk_free = disk.free
    
    # Aktuelles Datum und Uhrzeit
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Formatieren der Daten
    data = (f"{now}, CPU Usage: {cpu_usage}%, "
            f"RAM - Total: {ram_total}, Used: {ram_used}, Free: {ram_free}, "
            f"Disk - Total: {disk_total}, Used: {disk_used}, Free: {disk_free}\n")
    return data

def write_to_file(data, '~/3python/logfile.log'):
    with open('~/3python/logfile.log', 'a') as file:
        file.write(data)

if __name__ == "__main__":
    metrics = get_system_metrics()
    write_to_file(metrics, '~/3python/logfile.log')