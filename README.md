# Real-Time System Monitoring & Anomaly Detection Dashboard

## Overview

I built this project to understand how real-world monitoring systems work and how system metrics can be analyzed in real time.

This is a real-time system monitoring and anomaly detection dashboard that tracks metrics such as CPU, memory, disk, and network usage. Instead of just displaying values, the system analyzes the data to detect unusual behavior and helps identify potential issues early.

The system simulates real-time data using a mock server, processes it through APIs, stores it in a database, and continuously monitors it. A live dashboard is built on top of this pipeline to visualize system performance with automatically updating graphs and status indicators.

---

## How It Works

The project follows a simple pipeline:

**Collector → API → Database → Monitoring → Dashboard**

- A data collector generates system metrics continuously (simulated)
- FastAPI is used to expose endpoints to access the data
- The data is stored in a MySQL database for tracking history
- A monitoring layer analyzes the data and detects anomalies
- A Streamlit dashboard displays everything in real time

---

## Key Features

- Real-time simulation of system metrics  
- FastAPI backend with working API endpoints  
- Historical data storage using MySQL  
- Statistical anomaly detection (mean & standard deviation)  
- Live dashboard with auto-refresh  
- Status indicators: **Normal / Warning / Critical**  
- Graph-based visualization for trends and spikes  

---

## Anomaly Detection Logic

Instead of using fixed thresholds, this project uses a dynamic statistical approach.

- The average (mean) of historical data is calculated  
- Standard deviation is used to measure variation  
- If value > mean + std → **Warning**  
- If value > mean + 2 × std → **Critical**

This makes the system adaptive to changing patterns rather than relying on hardcoded limits.

---

## API Endpoints

- `/latest` → Returns latest system metrics  
- `/history` → Returns historical data  
- `/health` → System health check  

---

## Dashboard

The Streamlit dashboard provides:

- Live system metrics  
- Real-time status updates  
- Graphs that refresh automatically  
- Easy visualization of performance trends  

The goal was to make system behavior easy to understand at a glance rather than reading raw numbers.

---

## Tech Stack

- Python  
- FastAPI  
- Streamlit  
- MySQL  
- Requests  
- Statistics  

---

## What I Learned

- How to build an end-to-end data pipeline  
- Designing APIs using FastAPI  
- Working with real-time data flow  
- Applying statistical concepts to real problems  
- Building interactive dashboards  

---

## Future Improvements

- Advanced anomaly detection (time-series / ML-based models)  
- Alert system (email or notifications)  
- Logging system for tracking anomalies  
- Improved UI and advanced visualizations  

---
