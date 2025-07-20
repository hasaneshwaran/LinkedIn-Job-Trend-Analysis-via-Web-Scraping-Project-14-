import pandas as pd
import matplotlib.pyplot as plt
import os
import warnings

warnings.filterwarnings("ignore")

csv_path = r"C:\Users\PREMAVATHY\Videos\Captures\data job posts.csv"
output_folder = r"C:\Users\PREMAVATHY\Videos\Captures"

output_excel = os.path.join(output_folder, "job_summary.xlsx")
output_companies = os.path.join(output_folder, "top_companies.png")
output_locations = os.path.join(output_folder, "top_locations.png")
output_titles = os.path.join(output_folder, "top_titles.png")

df = pd.read_csv(csv_path)
df = df.dropna(subset=['Title', 'Company', 'Location'])
df['Title'] = df['Title'].str.strip().str.title()
df['Company'] = df['Company'].str.strip().str.title()
df['Location'] = df['Location'].str.strip()

top_companies = df['Company'].value_counts().head(10)
top_locations = df['Location'].value_counts().head(10)
top_titles = df['Title'].value_counts().head(10)

summary = pd.DataFrame({
    'Top Companies': top_companies,
    'Top Locations': top_locations,
    'Top Job Titles': top_titles
}).fillna('')
summary.to_excel(output_excel, index=True)

plt.figure(figsize=(12,6))
top_companies.plot(kind='bar', title='Top 10 Hiring Companies', color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(output_companies)

plt.figure(figsize=(12,6))
top_locations.plot(kind='bar', color='orange', title='Top 10 Job Locations')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(output_locations)

plt.figure(figsize=(12,6))
top_titles.plot(kind='bar', color='green', title='Top 10 Job Titles')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig(output_titles)
