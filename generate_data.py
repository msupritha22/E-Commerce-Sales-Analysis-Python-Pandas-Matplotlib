# generate_data.py — Run this FIRST to create the dataset
import pandas as pd
import numpy as np
import os

np.random.seed(42)
os.makedirs("data", exist_ok=True)

n = 1000

products = {
    "Electronics":  ["Samsung Galaxy S23", "boAt Earbuds", "Realme Watch", "HP Laptop", "JBL Speaker"],
    "Fashion":      ["Men's Kurta", "Women's Saree", "Levi's Jeans", "Nike Sneakers", "Fastrack Watch"],
    "Grocery":      ["Tata Salt 1kg", "Aashirvaad Atta 5kg", "Maggi Noodles 12pk", "Amul Butter 500g", "Fortune Oil 1L"],
    "Home & Kitchen": ["Prestige Cooker", "Milton Water Bottle", "Cello Fan", "Pigeon Mixer", "Bajaj Iron"],
    "Beauty":       ["Lakme Foundation", "Mamaearth Serum", "Biotique Shampoo", "WOW Body Lotion", "Lotus Sunscreen"],
}

cities = ["Bengaluru", "Mumbai", "Delhi", "Hyderabad",
          "Chennai", "Pune", "Kolkata", "Ahmedabad"]

price_map = {
    "Electronics": (800, 55000), "Fashion": (300, 4000),
    "Grocery": (50, 800), "Home & Kitchen": (400, 6000), "Beauty": (150, 2500),
}

records = []
for i in range(1, n + 1):
    category = np.random.choice(list(products.keys()),
                                p=[0.30, 0.25, 0.20, 0.15, 0.10])
    product  = np.random.choice(products[category])
    lo, hi   = price_map[category]
    price    = round(np.random.uniform(lo, hi), 2)
    qty      = np.random.choice([1, 1, 1, 2, 2, 3], p=[0.4, 0.2, 0.15, 0.1, 0.1, 0.05])
    status   = np.random.choice(["Delivered", "Delivered", "Delivered",
                                 "Returned", "Cancelled"],
                                p=[0.75, 0.1, 0.05, 0.06, 0.04])
    records.append({
        "order_id":    f"ORD{i:05d}",
        "order_date":  pd.Timestamp("2024-01-01") + pd.Timedelta(days=int(np.random.randint(0, 365))),
        "product_name": product,
        "category":    category,
        "quantity":    qty,
        "unit_price":  price,
        "city":        np.random.choice(cities),
        "order_status": status,
    })

df = pd.DataFrame(records)
df.to_csv("data/ecommerce_sales.csv", index=False)
print(f"✅ Dataset created: data/ecommerce_sales.csv  ({len(df)} rows)")
