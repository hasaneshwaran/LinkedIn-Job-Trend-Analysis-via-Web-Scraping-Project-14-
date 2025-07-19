import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"C:\vel\data\job_industries.csv", nrows=10)
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())

df = pd.read_csv(r"C:\vel\data\job_industries.csv")

print("Columns:", df.columns.tolist())
print("Sample:\n", df.head(3))

industry_col = 'industry'
location_col = 'location'
count_col = 'job_id'

output_dir = r"C:\vel\data\analysis_industries"
os.makedirs(output_dir, exist_ok=True)

if industry_col in df.columns:
    top_industries = df[industry_col].value_counts().head(10)
    print("\nTop 10 Industries:\n", top_industries)

    plt.figure(figsize=(8,4))
    top_industries.plot(kind='barh', color='purple')
    plt.title("Top 10 Industries")
    plt.xlabel("Job Count")
    plt.ylabel("Industry")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "top_industries.png"))
    plt.close()

if location_col in df.columns:
    top_locations = df[location_col].value_counts().head(10)
    print("\nTop 10 Locations:\n", top_locations)

    plt.figure(figsize=(8,4))
    top_locations.plot(kind='barh', color='orange')
    plt.title("Top 10 Locations (Industries)")
    plt.xlabel("Job Count")
    plt.ylabel("Location")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "top_industry_locations.png"))
    plt.close()

excel_path = os.path.join(output_dir, "job_industries_summary.xlsx")
with pd.ExcelWriter(excel_path) as writer:
    if industry_col in df.columns:
        top_industries.to_frame("Count").to_excel(writer, sheet_name="Top Industries")
    if location_col in df.columns:
        top_locations.to_frame("Count").to_excel(writer, sheet_name="Top Locations")

print(f"\nAnalysis complete! Check: {output_dir}")
