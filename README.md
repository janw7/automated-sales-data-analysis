# E-commerce ETL Pipeline 

A lightweight ETL (Extract, Transform, Load) pipeline built in Python, designed to automate data extraction and perform basic business analysis.

## Overview
This project demonstrates a fully automated pipeline that:
1. **Extracts** raw product data from a REST API ([FakeStore API](https://fakestoreapi.com/)).
2. **Transforms** the JSON data into a structured format.
3. **Loads** the cleaned data into a local relational database (`SQLite`).
4. Performs basic business analytics using `pandas` (e.g., calculating average prices per category).

## Technologies Used
* **Python 3.x**
* **SQLite3** (Database & SQL queries)
* **Requests** (API integration)
* **Pandas** (Data analysis & grouping)

## How to Run
1. Install required packages: `pip install requests pandas`
2. Run the script: `python etl.py`
