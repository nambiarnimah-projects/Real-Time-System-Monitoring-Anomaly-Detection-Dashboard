from fastapi import FastAPI
import random
app=FastAPI()
@app.get("/metrics")
def get_metrics():
    cpu=random.randint(10,90)
    memory=random.randint(20,95)
    disk=random.randint(10,80)
    network=random.randint(50,500)
    return{"cpu_usage":cpu,"memory_usage":memory,"disk_usage":disk,"network_traffic":network}
