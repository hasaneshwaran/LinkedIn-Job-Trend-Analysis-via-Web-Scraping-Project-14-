import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv(r"C:\vel\data\postings.csv", nrows=1000)

print("Columns in dataset:", df.columns.tolist())
print("Sample rows:\n", df.head(3))

def get_column(name_options):
    for name in name_options:
        if name in df.columns:
            return name
    return None

job_col = get_column(['job_title', 'title', 'position', 'Job Title'])
location_col = get_column(['location', 'Location', 'job_location'])
skills_col = get_column(['skills', 'key_skills', 'Skills'])
salary_col = get_column(['salary', 'Salary'])
type_col = get_column(['job_type', 'Job Type', 'employment_type'])

output_dir = r"C:\vel\data\analysis_output"
os.makedirs(output_dir, exist_ok=True)

if job_col:
    top_titles = df[job_col].value_counts().head(10)
    print("\nTop 10 Job Titles:\n", top_titles)
    
    plt.figure(figsize=(8,4))
    top_titles.plot(kind='barh', color='skyblue')
    plt.title("Top 10 Job Titles")
    plt.xlabel("Count")
    plt.ylabel("Job Title")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "top_job_titles.png"))
    plt.close()

if location_col:
    top_locations = df[location_col].value_counts().head(10)
    print("\nTop 10 Locations:\n", top_locations)
    
    plt.figure(figsize=(8,4))
    top_locations.plot(kind='barh', color='salmon')
    plt.title("Top 10 Locations")
    plt.xlabel("Count")
    plt.ylabel("Location")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "top_locations.png"))
    plt.close()

if skills_col:
    all_skills = df[skills_col].dropna().str.split(',')
    skills_flat = [skill.strip() for sublist in all_skills for skill in sublist]
    skill_series = pd.Series(skills_flat)
    top_skills = skill_series.value_counts().head(15)
    print("\nTop 15 Skills:\n", top_skills)
    
    plt.figure(figsize=(8,5))
    top_skills.plot(kind='barh', color='green')
    plt.title("Top 15 Skills")
    plt.xlabel("Count")
    plt.ylabel("Skill")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "top_skills.png"))
    plt.close()

if salary_col:
    print("\nSalary Summary:\n", df[salary_col].describe())

if type_col:
    print("\nJob Type Counts:\n", df[type_col].value_counts())

excel_path = os.path.join(output_dir, "linkedin_job_summary.xlsx")
with pd.ExcelWriter(excel_path) as writer:
    if job_col:
        top_titles.to_frame("Count").to_excel(writer, sheet_name="Top Job Titles")
    if location_col:
        top_locations.to_frame("Count").to_excel(writer, sheet_name="Top Locations")
    if skills_col:
        top_skills.to_frame("Count").to_excel(writer, sheet_name="Top Skills")
    if salary_col:
        df[salary_col].describe().to_frame().to_excel(writer, sheet_name="Salary Summary")
    if type_col:
        df[type_col].value_counts().to_frame("Count").to_excel(writer, sheet_name="Job Types")

print(f"\nAnalysis complete! Check results in: {output_dir}")
