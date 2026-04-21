import streamlit as st
import requests
import datetime
import time
from streamlit_autorefresh import st_autorefresh
from monitor import cpu_status
st_autorefresh(interval=2000, key="refresh")
st.title("server monitoring dashboard")
data=cpu_status()
placeholder=st.empty() #to create a reusable container,else a new row will be created for a new value=messy output
try:
        history=requests.get("http://127.0.0.1:8000/history").json()
        cpu_values=[rows["cpu"] for rows in history]
        memory_values=[rows["memory"] for rows in history]
        disk_values=[rows["disk"] for rows in history]
        network_values=[rows["network"] for rows in history]
        
        if any(status == "CRITICAL" for status in data.values()):
         st.error("SYSTEM CRITICAL ALERT")
        elif any(status == "WARNING" for status in data.values()):
         st.warning("SYSTEM WARNING")
        col1, col2 = st.columns(2)

        with col1:
            st.metric("CPU", data["cpu"]["value"])
            if data["cpu"]["status"] == "CRITICAL":
                st.error("CPU Critical")
            elif data["cpu"]["status"] == "WARNING":
                st.warning("CPU Warning")
            else:
                st.success("CPU Normal")

            st.metric("Memory", data["memory"]["value"])
            if data["memory"]["status"] == "CRITICAL":
                st.error("Memory Critical")
            elif data["memory"]["status"] == "WARNING":
                st.warning("Memory Warning")
            else:
                st.success("Memory Normal")

        with col2:
            st.metric("Disk", data["disk"]["value"])
            if data["disk"]["status"] == "CRITICAL":
                st.error("Disk Critical")
            elif data["disk"]["status"] == "WARNING":
                st.warning("Disk Warning")
            else:
                st.success("Disk Normal")

            st.metric("Network", data["network"]["value"])
            if data["network"]["status"] == "CRITICAL":
                st.error("Network Critical")
            elif data["network"]["status"] == "WARNING":
                st.warning("Network Warning")
            else:
                st.success("Network Normal")
        st.subheader("System Metrics Over Time")

        col1, col2 = st.columns(2)

        with col1:
            st.write("CPU Usage")
            st.line_chart(cpu_values)

            st.write("Memory Usage")
            st.line_chart(memory_values)

        with col2:
            st.write("Disk Usage")
            st.line_chart(disk_values)

            st.write("Network Usage")
            st.line_chart(network_values)


    


    
except Exception as e:    st.error(f"Error fetching data: {e}")     
