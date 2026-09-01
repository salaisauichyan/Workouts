# Retail Sales End-to-End Data Engineering Pipeline

## 📌 Project Overview

This project demonstrates an end-to-end data engineering pipeline using **Databricks, PySpark, SQL, and Delta Lake**.

The pipeline takes raw retail sales data from a CSV file, performs data validation and cleaning, transforms the data, and creates structured datasets for analytics.

The project was built as a hands-on learning project to understand the fundamentals of **ETL, data transformation, data quality, and the Bronze-Silver-Gold architecture**.

---

## 🎯 Project Objective

Raw sales data can contain inconsistent values, duplicate records, missing information, and data that is not directly suitable for analysis.

The objective of this project is to:

* Ingest raw retail sales data
* Validate the incoming data
* Remove duplicate records
* Handle missing values
* Clean string columns
* Transform the data using PySpark
* Calculate sales metrics
* Store processed data using Delta Lake
* Create analytical Gold datasets
* Perform SQL-based analysis

---

## 🏗️ Data Pipeline Architecture

```text
                 Retail Sales CSV
                        │
                        ▼
                 Bronze Layer
                  Raw Data
                        │
                        ▼
              Data Validation
                        │
                        ▼
                 Silver Layer
                Cleaned Data
                        │
                        ▼
                Transformations
                        │
                        ▼
                  Gold Layer
             Analytical Dataset
                        │
                        ▼
                  SQL Analytics
```

---

## 🛠️ Technologies Used

| Technology | Purpose                                   |
| ---------- | ----------------------------------------- |
| Python     | Data processing and scripting             |
| PySpark    | Data transformation                       |
| Databricks | Data engineering platform                 |
| SQL        | Data analysis                             |
| Delta Lake | Reliable data storage                     |
| CSV        | Source data format                        |
| GitHub     | Version control and project documentation |

---

## 📊 Dataset

The project uses a synthetic retail sales dataset containing **5,000 records**.

### Dataset Columns

| Column             | Description               |
| ------------------ | ------------------------- |
| `order_id`         | Unique order identifier   |
| `order_date`       | Date of the order         |
| `customer_id`      | Customer identifier       |
| `product`          | Product purchased         |
| `category`         | Product category          |
| `quantity`         | Number of items purchased |
| `unit_price`       | Price per item            |
| `discount_pct`     | Discount percentage       |
| `total_amount`     | Original sales amount     |
| `city`             | Customer city             |
| `payment_method`   | Payment method used       |
| `customer_segment` | Customer segment          |

---

## 🔄 ETL Process

### 1. Extract

The raw CSV file is loaded into Databricks using PySpark.

```python
df_raw = spark.read \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("delimiter", "\t") \
    .csv("/FileStore/tables/retail_sales.csv")
```

### 2. Transform

The data is cleaned and transformed by:

* Removing duplicate orders
* Removing records with required fields missing
* Trimming unnecessary spaces
* Calculating sales values
* Grouping data for analytical reporting

Example:

```python
df_silver = (
    df_raw
    .dropDuplicates(["order_id"])
    .dropna(subset=["order_id", "customer_id", "product"])
)
```

Sales calculation:

```python
df_silver = df_silver.withColumn(
    "calculated_sales",
    round(
        col("quantity") *
        col("unit_price") *
        (1 - col("discount_pct")),
        2
    )
)
```

### 3. Load

The processed datasets are stored as Delta tables.

```text
Bronze → Raw Data
Silver → Cleaned Data
Gold → Analytical Data
```

---

## 🥉 Bronze Layer

The Bronze layer contains the raw data ingested from the CSV source.

```text
retail_sales.csv
        ↓
    Bronze Layer
```

Purpose:

* Store raw data
* Preserve the original source
* Provide a starting point for processing

---

## 🥈 Silver Layer

The Silver layer contains cleaned and validated data.

Processing includes:

* Duplicate removal
* Null handling
* String cleaning
* Data transformation
* Sales calculation

Stored as:

```text
retail_sales_silver
```

---

## 🥇 Gold Layer

The Gold layer contains business-ready analytical data.

Example metrics:

* Total orders
* Total quantity
* Total sales
* Average order value
* Sales by category

Stored as:

```text
retail_sales_gold
```

---

## 📈 SQL Analytics

Example SQL query used to analyze sales by category:

```sql
SELECT
    category,
    total_orders,
    total_quantity,
    total_sales,
    average_order_value
FROM retail_sales_gold
ORDER BY total_sales DESC;
```

Other analysis performed:

* Top-selling products
* Sales by city
* Sales by payment method
* Sales by product category

---

## 📁 Project Structure

```text
retail-sales-etl-pipeline/
│
├── README.md
│
├── data/
│   └── retail_sales.csv
│
├── notebooks/
│   └── retail_sales_etl.py
│
└── sql/
    └── analytics.sql
```

> Note: The actual Databricks Delta tables are stored in Databricks rather than committed to GitHub.

---

## 🚀 Key Learnings

Through this project, I learned:

* How to ingest CSV data using PySpark
* How to work with DataFrames in Databricks
* How to perform data validation
* How to remove duplicates and handle missing values
* How to perform transformations using PySpark
* How to calculate derived metrics
* How to use Delta Lake
* How to implement Bronze-Silver-Gold architecture
* How to perform SQL analytics
* How to structure a basic data engineering project

---

## 🔮 Future Improvements

Planned improvements for future versions:

* Add Azure Data Factory
* Add Azure Data Lake Storage Gen2
* Add Azure Synapse Analytics
* Add Databricks Workflows
* Add automated data quality checks
* Add incremental data processing
* Add real-time streaming
* Add CI/CD using GitHub

---

## 👨‍💻 Author

**Salai Sauichyan**

Aspiring Data Engineer

### Skills

`Python` `SQL` `PySpark` `Databricks` `Delta Lake` `ETL/ELT` `Azure`

---

## ⭐ Project Status

**Completed — Learning Project**

This project was created to develop practical data engineering skills and build an end-to-end ETL pipeline using Databricks and PySpark.
