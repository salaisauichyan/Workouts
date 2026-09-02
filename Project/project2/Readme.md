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

## 🛠️ Technologies Used

* Python
* PySpark
* Databricks
* Apache Spark
* Delta Lake
* SQL
* Pandas
* NumPy
* ETL

---

## 📊 Dataset

The project uses an e-commerce sales dataset containing **5,000 records**.

### Dataset Columns

| Column           | Description                         |
| ---------------- | ----------------------------------- |
| `order_id`       | Unique order identifier             |
| `order_date`     | Date of the order                   |
| `customer_id`    | Customer identifier                 |
| `product`        | Product purchased                   |
| `category`       | Product category                    |
| `quantity`       | Number of items purchased           |
| `unit_price`     | Price per item                      |
| `city`           | Customer city                       |
| `payment_method` | Payment method used                 |
| `total_amount`   | Transaction amount from source data |

---

## 🔄 ETL Process

### 1. Extract

The raw CSV file is uploaded to Databricks.

**File path:**

```text
/FileStore/tables/ecommerce_sales.csv
```

The CSV data is read using PySpark.

```python
df_raw = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("delimiter", ",") \
    .csv("/FileStore/tables/ecommerce_sales.csv")
```

---

### 2. Validate

The raw data is checked for:

* Total number of records
* Column names
* Data types
* Null values
* Duplicate orders
* Unique order IDs

Example:

```python
print("Total rows:", df_raw.count())
print(df_raw.columns)
df_raw.printSchema()
```

---

### 3. Transform

The data is cleaned using PySpark.

Transformation steps include:

* Removing duplicate orders
* Removing records with missing important fields
* Trimming unwanted spaces
* Standardizing text columns
* Calculating transaction amounts

Example:

```python
from pyspark.sql.functions import col, trim

df_clean = (
    df_raw
    .dropDuplicates(["order_id"])
    .dropna(subset=["order_id", "customer_id", "product"])
    .withColumn("product", trim(col("product")))
    .withColumn("category", trim(col("category")))
    .withColumn("city", trim(col("city")))
    .withColumn("payment_method", trim(col("payment_method")))
)
```

---

## 💰 Sales Calculation

The pipeline calculates the transaction amount using:

```text
quantity × unit_price
```

Example:

```python
from pyspark.sql.functions import round

df_clean = df_clean.withColumn(
    "calculated_amount",
    round(
        col("quantity") * col("unit_price"),
        2
    )
)
```

The calculated value can be compared with the source `total_amount` to perform a basic data quality check.

---

## 🥈 Silver Layer

The cleaned and transformed data is stored as a Delta table.

```python
df_clean.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("ecommerce_sales_silver")
```

The Silver table contains cleaned, validated, and transformed transaction-level data.

---

## 🥇 Gold Layer

The Gold layer contains aggregated data for analytics.

The data is grouped by product and category.

Example:

```python
from pyspark.sql.functions import count, sum, avg

df_gold = (
    df_clean
    .groupBy("product", "category")
    .agg(
        count("order_id").alias("total_orders"),
        sum("quantity").alias("total_quantity"),
        round(sum("calculated_amount"), 2).alias("total_sales"),
        round(avg("calculated_amount"), 2).alias("average_order_value")
    )
    .orderBy(col("total_sales").desc())
)
```

The Gold data is stored as a Delta table:

```python
df_gold.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("ecommerce_sales_gold")
```

---

## 🔎 SQL Analytics

The Gold and Silver tables can be queried using SQL.

### Top Products by Sales

```sql
SELECT
    product,
    category,
    total_orders,
    total_quantity,
    total_sales,
    average_order_value
FROM ecommerce_sales_gold
ORDER BY total_sales DESC;
```

### Sales by City

```sql
SELECT
    city,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(calculated_amount), 2) AS total_sales
FROM ecommerce_sales_silver
GROUP BY city
ORDER BY total_sales DESC;
```

### Sales by Payment Method

```sql
SELECT
    payment_method,
    COUNT(order_id) AS total_orders,
    ROUND(SUM(calculated_amount), 2) AS total_sales
FROM ecommerce_sales_silver
GROUP BY payment_method
ORDER BY total_sales DESC;
```

### Sales by Category

```sql
SELECT
    category,
    COUNT(order_id) AS total_orders,
    SUM(quantity) AS total_quantity,
    ROUND(SUM(calculated_amount), 2) AS total_sales
FROM ecommerce_sales_silver
GROUP BY category
ORDER BY total_sales DESC;
```

---

## 📁 Project Structure

```text
ecommerce-data-engineering-pipeline/
│
├── data/
│   └── ecommerce_sales.csv
│
├── notebooks/
│   └── ecommerce_etl.py
│
├── sql/
│   └── analytics.sql
│
├── generate_data.py
│
└── README.md
```

---

## 📈 Data Engineering Concepts Demonstrated

This project demonstrates the following concepts:

* ETL pipeline development
* Data ingestion
* Data validation
* Data cleaning
* Duplicate handling
* Null value handling
* PySpark DataFrame transformations
* Aggregations
* Delta Lake
* Bronze / Silver / Gold architecture
* SQL analytics
* Databricks
* Analytics-ready data preparation

---

## 🚀 Future Improvements

Possible improvements for this project include:

* Add Azure Data Lake Storage
* Add Azure Data Factory
* Add Databricks Workflows
* Add incremental data loading
* Add partitioning
* Add data quality rules
* Add Slowly Changing Dimensions (SCD)
* Add real-time streaming using Kafka
* Add automated pipeline monitoring

---

## 🎓 What I Learned

Through this project, I learned how to:

* Build an ETL pipeline using PySpark
* Work with data in Databricks
* Clean and validate raw datasets
* Transform data using Spark DataFrames
* Store data using Delta Lake
* Create Silver and Gold data layers
* Use SQL for analytical queries
* Structure a data engineering project for GitHub

---

## 📌 Project Status

**Completed – Learning Project**

This project was created to demonstrate practical Data Engineering skills as a fresher.

---

## 👨‍💻 Author

**Salai Sauichyan**

**Aspiring Data Engineer**

### Skills

* Python
* SQL
* PySpark
* Databricks
* Azure Basics
* GCP Basics
* ETL / ELT
* Delta Lake
