# ============================================================
# E-Commerce Sales Analysis | Python + Pandas + Matplotlib
# Author: Supritha | Business Analytics Portfolio
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import os

# ── Output folder ────────────────────────────────────────────
os.makedirs("outputs", exist_ok=True)

# ── 1. Load Data ─────────────────────────────────────────────
print("=" * 55)
print("   E-COMMERCE SALES ANALYSIS")
print("=" * 55)

df = pd.read_csv("data/ecommerce_sales.csv", parse_dates=["order_date"])
print(f"\n✅ Dataset loaded: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"\nColumns: {list(df.columns)}")

# ── 2. Basic Info ─────────────────────────────────────────────
print("\n── DATA OVERVIEW ──────────────────────────────────────")
print(df.head())
print(f"\nMissing values:\n{df.isnull().sum()}")
print(f"\nData types:\n{df.dtypes}")

# ── 3. Feature Engineering ────────────────────────────────────
df["revenue"]       = df["quantity"] * df["unit_price"]
df["month"]         = df["order_date"].dt.to_period("M")
df["month_name"]    = df["order_date"].dt.strftime("%b %Y")
df["day_of_week"]   = df["order_date"].dt.day_name()

# ── 4. KPIs ───────────────────────────────────────────────────
total_revenue   = df["revenue"].sum()
total_orders    = df["order_id"].nunique()
avg_order_value = total_revenue / total_orders
top_category    = df.groupby("category")["revenue"].sum().idxmax()

print("\n── KEY PERFORMANCE INDICATORS ─────────────────────────")
print(f"  Total Revenue      : ₹{total_revenue:,.0f}")
print(f"  Total Orders       : {total_orders:,}")
print(f"  Avg Order Value    : ₹{avg_order_value:,.0f}")
print(f"  Top Category       : {top_category}")

# ── 5. Analysis Tables ────────────────────────────────────────

# Revenue by Category
cat_rev = (df.groupby("category")["revenue"]
             .sum()
             .sort_values(ascending=False)
             .reset_index())
cat_rev.columns = ["Category", "Revenue (₹)"]

# Monthly Revenue Trend
monthly = (df.groupby("month")["revenue"]
             .sum()
             .reset_index())
monthly["month_str"] = monthly["month"].astype(str)

# Top 5 Products
top_products = (df.groupby("product_name")["revenue"]
                  .sum()
                  .sort_values(ascending=False)
                  .head(5)
                  .reset_index())
top_products.columns = ["Product", "Revenue (₹)"]

# City-wise Revenue
city_rev = (df.groupby("city")["revenue"]
              .sum()
              .sort_values(ascending=False)
              .head(8)
              .reset_index())
city_rev.columns = ["City", "Revenue (₹)"]

print("\n── REVENUE BY CATEGORY ────────────────────────────────")
print(cat_rev.to_string(index=False))

print("\n── TOP 5 PRODUCTS ─────────────────────────────────────")
print(top_products.to_string(index=False))

print("\n── TOP CITIES BY REVENUE ──────────────────────────────")
print(city_rev.to_string(index=False))

# ── 6. Save Summary CSV ───────────────────────────────────────
cat_rev.to_csv("outputs/category_revenue.csv", index=False)
top_products.to_csv("outputs/top_products.csv", index=False)
monthly.to_csv("outputs/monthly_trend.csv", index=False)
print("\n✅ Summary CSVs saved to outputs/")

# ── 7. Visualisations ─────────────────────────────────────────
COLORS = ["#2563EB", "#7C3AED", "#059669", "#DC2626",
          "#D97706", "#0891B2", "#9333EA", "#16A34A"]

fig, axes = plt.subplots(2, 2, figsize=(16, 11))
fig.suptitle("E-Commerce Sales Dashboard", fontsize=18, fontweight="bold",
             color="#1e293b", y=1.01)
fig.patch.set_facecolor("#f8fafc")
for ax in axes.flat:
    ax.set_facecolor("#ffffff")

# Chart 1 – Monthly Revenue Trend (line)
ax1 = axes[0, 0]
ax1.plot(monthly["month_str"], monthly["revenue"],
         marker="o", linewidth=2.5, color="#2563EB", markersize=6)
ax1.fill_between(monthly["month_str"], monthly["revenue"],
                 alpha=0.15, color="#2563EB")
ax1.set_title("Monthly Revenue Trend", fontsize=13, fontweight="bold", pad=10)
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue (₹)")
ax1.tick_params(axis="x", rotation=45)
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(
    lambda x, _: f"₹{x/1e5:.1f}L"))
ax1.grid(axis="y", linestyle="--", alpha=0.4)

# Chart 2 – Revenue by Category (horizontal bar)
ax2 = axes[0, 1]
bars = ax2.barh(cat_rev["Category"], cat_rev["Revenue (₹)"],
                color=COLORS[:len(cat_rev)], edgecolor="white")
ax2.set_title("Revenue by Category", fontsize=13, fontweight="bold", pad=10)
ax2.set_xlabel("Revenue (₹)")
ax2.xaxis.set_major_formatter(mticker.FuncFormatter(
    lambda x, _: f"₹{x/1e5:.1f}L"))
ax2.invert_yaxis()
for bar in bars:
    w = bar.get_width()
    ax2.text(w * 1.01, bar.get_y() + bar.get_height() / 2,
             f"₹{w/1e5:.1f}L", va="center", fontsize=9)

# Chart 3 – Top 5 Products (vertical bar)
ax3 = axes[1, 0]
ax3.bar(top_products["Product"], top_products["Revenue (₹)"],
        color=COLORS[:5], edgecolor="white", width=0.6)
ax3.set_title("Top 5 Products by Revenue", fontsize=13, fontweight="bold", pad=10)
ax3.set_ylabel("Revenue (₹)")
ax3.yaxis.set_major_formatter(mticker.FuncFormatter(
    lambda x, _: f"₹{x/1e5:.1f}L"))
ax3.tick_params(axis="x", rotation=30)
ax3.grid(axis="y", linestyle="--", alpha=0.4)

# Chart 4 – City Revenue (pie)
ax4 = axes[1, 1]
wedges, texts, autotexts = ax4.pie(
    city_rev["Revenue (₹)"], labels=city_rev["City"],
    autopct="%1.1f%%", colors=COLORS[:len(city_rev)],
    startangle=140, pctdistance=0.82,
    wedgeprops={"edgecolor": "white", "linewidth": 1.5})
for t in autotexts:
    t.set_fontsize(8)
ax4.set_title("Revenue Share by City", fontsize=13, fontweight="bold", pad=10)

plt.tight_layout()
plt.savefig("outputs/sales_dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Dashboard saved → outputs/sales_dashboard.png")
print("\n🎉 Analysis complete!")
