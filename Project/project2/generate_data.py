import pandas as pd
import numpy as np

np.random.seed(42)

n = 5000

products = [
    "Laptop",
    "Smartphone",
    "Headphones",
    "Keyboard",
    "Mouse",
    "Monitor",
    "Tablet",
    "Smartwatch",
    "Backpack",
    "Shoes"
]

categories = {
    "Laptop": "Electronics",
    "Smartphone": "Electronics",
    "Headphones": "Electronics",
    "Keyboard": "Electronics",
    "Mouse": "Electronics",
    "Monitor": "Electronics",
    "Tablet": "Electronics",
    "Smartwatch": "Electronics",
    "Backpack": "Accessories",
    "Shoes": "Fashion"
}

cities = [
    "Chennai",
    "Coimbatore",
    "Bengaluru",
    "Hyderabad",
    "Mumbai",
    "Delhi",
    "Pune",
    "Kochi"
]

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking"
]

product = np.random.choice(products, n)

df = pd.DataFrame({
    "order_id": [f"ORD{100001+i}" for i in range(n)],

    "order_date": pd.to_datetime(
        np.random.choice(
            pd.date_range("2025-01-01", "2025-12-31"),
            n
        )
    ).strftime("%Y-%m-%d"),

    "customer_id": [
        f"CUST{1001+i%1000}"
        for i in range(n)
    ],

    "product": product,

    "category": [
        categories[p]
        for p in product
    ],

    "quantity": np.random.randint(1, 6, n),

    "unit_price": np.round(
        np.random.uniform(10, 1500, n),
        2
    ),

    "city": np.random.choice(cities, n),

    "payment_method": np.random.choice(
        payment_methods,
        n
    )
})

df["total_amount"] = (
    df["quantity"] *
    df["unit_price"]
).round(2)

df.to_csv(
    "ecommerce_sales.csv",
    index=False
)

print("Dataset created successfully!")
print("Total records:", len(df))
print(df.head())