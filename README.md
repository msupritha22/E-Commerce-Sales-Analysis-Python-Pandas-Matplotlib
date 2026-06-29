#  E-Commerce Sales Analysis - Python + Pandas

> A beginner-friendly Python data analytics project analysing 1,000 e-commerce orders across Indian cities, product categories, and months.

---

##  Project Overview

This project simulates a real-world e-commerce dataset (Flipkart / Amazon style) and performs end-to-end sales analysis using Python and Pandas. It covers data generation, cleaning, KPI extraction, and dashboard visualisation.

---

##  Key Insights Generated

| KPI | Description |
|-----|-------------|
|  Total Revenue | Sum of all order revenues |
|  Total Orders | Count of unique orders |
|  Avg Order Value | Revenue ÷ Orders |
|  Top Category | Highest revenue category |

**Charts Produced:**
-  Monthly Revenue Trend (line chart)
-  Revenue by Category (horizontal bar)
-  Top 5 Products (bar chart)
-  City Revenue Share (pie chart)

---

##  Project Structure

```
ecommerce_sales_analysis/
│
├── data/
│   └── ecommerce_sales.csv      # Auto-generated dataset (1,000 rows)
│
├── outputs/
│   ├── sales_dashboard.png      # 2×2 chart dashboard
│   ├── category_revenue.csv     # Revenue by category
│   ├── top_products.csv         # Top 5 products
│   └── monthly_trend.csv        # Monthly revenue trend
│
├── generate_data.py             # Step 1 — Creates the dataset
├── sales_analysis.py            # Step 2 — Runs full analysis
├── requirements.txt
└── README.md
```

---

##  How to Run

```bash
# 1. Clone the repo
git clone https://github.com/<your-username>/ecommerce-sales-analysis.git
cd ecommerce-sales-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Generate dataset
python generate_data.py

# 4. Run analysis
python sales_analysis.py
```

---

##  Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| Pandas | Data manipulation |
| Matplotlib | Visualisation |
| NumPy | Data generation |

---

##  Dataset Columns

| Column | Description |
|--------|-------------|
| `order_id` | Unique order identifier |
| `order_date` | Date of purchase (2024) |
| `product_name` | Product name |
| `category` | Electronics, Fashion, Grocery, etc. |
| `quantity` | Units ordered |
| `unit_price` | Price per unit (₹) |
| `city` | Delivery city |
| `order_status` | Delivered / Returned / Cancelled



**Supritha** — MBA (Business Analytics) | IFIM Business School, Bengaluru  
🔗 [LinkedIn](#) | 💻 [GitHub](#)
