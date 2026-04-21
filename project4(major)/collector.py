import mysql.connector
import requests
import datetime
import time
db=mysql.connector.connect(host="localhost",user="root",password="sql@sql7171",database="p4_monitoring")
cursor=db.cursor()
print("connected to mySQL")
#to show if the databse is actually conneceted to to the python code
# cursor.execute("SHOW TABLES")
# tables = cursor.fetchall()
# print(tables)/
while True:
    try:
        response=requests.get("http://127.0.0.1:8000/metrics",timeout=5)
        data=response.json()
        print(data)
        cpu = data["cpu_usage"]
        memory = data["memory_usage"]
        disk = data["disk_usage"]
        network = data["network_traffic"]
        timestamp = datetime.datetime.now()
        query="insert into server_metrics(timestamps,cpu_usage,memory_usage,disk_usage,network_traffic) values(%s,%s,%s,%s,%s)"
        cursor.execute(query,(timestamp,cpu,memory,disk,network))
        #to save changes in db
        db.commit()
        time.sleep(10)
        print("data inserted successfully")
    except Exception as e:
        print("error:",e)
    time.sleep(10)






