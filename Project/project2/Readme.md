# E-Commerce Data Engineering Pipeline

## 📌 Project Overview

This project is an end-to-end data engineering pipeline built using
Python, PySpark, Databricks, Delta Lake, and SQL.

The project simulates an e-commerce sales system where raw sales data
is ingested, validated, cleaned, transformed, and stored as analytics-ready
Delta tables.

The main goal is to understand how a Data Engineer builds a simple
ETL pipeline from raw data to structured data for analytics.

---

## 🎯 Project Objective

The objectives of this project are:

- Generate a realistic e-commerce sales dataset
- Ingest CSV data into Databricks
- Validate the raw data
- Clean and transform the data using PySpark
- Calculate sales amounts
- Store processed data as Delta tables
- Create Gold-level aggregated data
- Perform SQL analytics on the processed data

---

## 🏗️ Data Pipeline Architecture

```text
E-Commerce CSV
      ↓
   Ingestion
      ↓
 Bronze / Raw Data
      ↓
 Data Validation
      ↓
 Data Cleaning
      ↓
 Silver Delta Table
      ↓
 Aggregation
      ↓
 Gold Delta Table
      ↓
 SQL Analytics
