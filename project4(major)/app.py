from fastapi import FastAPI
import mysql.connector
import datetime
import random
app=FastAPI()
@app.get("/metrics")
def get_metrics():
    cpu=random.randint(10,90)
    memory=random.randint(20,95)
    disk=random.randint(10,80)
    network=random.randint(50,500)
    return{"cpu_usage":cpu,"memory_usage":memory,"disk_usage":disk,"network_traffic":network}

def get_database_connection():
    return mysql.connector.connect(host="localhost",user="root",password="sql@sql7171",database="p4_monitoring")
@app.get("/")
def home():
    return{"message":"API is working"}
@app.get("/health")
def health():
    return{"status":"running"}
@app.get("/latest")
def get_latest():
    try:
        db=mysql.connector.connect(host="localhost",user="root",password="sql@sql7171",database="p4_monitoring")
        cursor=db.cursor()
        query="select * from server_metrics order by timestamps desc limit 1"
        cursor.execute(query)
        result=cursor.fetchone()
       # return result
        cursor.close()
        db.close()
        if result:
            return{
                "id": result[0],
                "timestamp": result[1],
                "cpu": result[2],
                "memory":result[3],
                "disk":result[4],
                "network":result[5]
            }
        else:
            return{"message":"no data found"}
    except Exception as e:
        return {"error":str(e)}
@app.get("/history")
def get_history():
    try:
        db=get_database_connection()
        cursor=db.cursor()
        query="select * from server_metrics order by timestamps desc limit 10"
        cursor.execute(query)
        result=cursor.fetchall()
        if result:
            return [{"id":row[0],"timestamp":row[1],"cpu":row[2],"memory":row[3],"disk":row[4],"network":row[5]} for row in result]
        else:
            return{"message":"no data found"}
    except Exception as e:
        return {"error":str(e)}