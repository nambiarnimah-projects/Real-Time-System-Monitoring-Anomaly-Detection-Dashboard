from matplotlib.pylab import std
import requests
import statistics
from streamlit import status
#FIND AVERAGE CPU USAGE AND COMPARE WITH CURRENT VALUE
def cpu_status():
    history=requests.get("http://127.0.0.1:8000/history").json()
    latest=requests.get("http://127.0.0.1:8000/latest").json()
    cpu_values = [row["cpu"] for row in history]
    memory_values = [row["memory"] for row in history]
    disk_values = [row["disk"] for row in history]
    network_values = [row["network"] for row in history]
    def detect(values,current):
        if len(values)<2:
            return "NORMAL"
        avg=statistics.mean(values)
        std=statistics.stdev(values)
        if current>avg+2*std:
            return "CRITICAL"
        elif current>avg+std:
            return "WARNING"
        else:
            return "NORMAL"
    return {
        "cpu": {
            "value": latest["cpu"],
            "status": detect(cpu_values, latest["cpu"])
        },
        "memory": {
            "value": latest["memory"],
            "status": detect(memory_values, latest["memory"])
        },
        "disk": {
            "value": latest["disk"],
            "status": detect(disk_values, latest["disk"])
        },
        "network": {
            "value": latest["network"],
            "status": detect(network_values, latest["network"])
        }
    }

    
    