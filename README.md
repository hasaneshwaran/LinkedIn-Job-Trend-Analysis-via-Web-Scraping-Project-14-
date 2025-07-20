# Job Posts Data Analysis

This mini-project processes a dataset of job posts and generates summarized insights for presentation.  
The script cleans the dataset, extracts the most common companies, job titles, and locations, and exports both tabular and visual results for use in reports or presentations.

## Files

- **Model.py**  
  Python script that processes the job posts CSV file and produces outputs.

- **data job posts.csv**  
  The dataset containing job titles, companies, and locations.
2. Cleans the dataset by:
- Removing rows missing job title, company, or location.
- Standardizing capitalization and whitespace.

3. Calculates:
- Top 10 most frequent companies.
- Top 10 most frequent job titles.
- Top 10 most frequent job locations.

4. Saves:
- Summary table as `job_summary.xlsx`.
- Three visual bar charts as PNG files.3. Open Command Prompt and run:
```bash
E:
cd hasan
python Model.py


## How to Run

1. Ensure Python and the required libraries (`pandas`, `matplotlib`, `openpyxl`) are installed.
2. Place `Model.py` in:


- **job_summary.xlsx**  
  Excel file with the top 10 companies, job titles, and locations.

- **top_companies.png**  
  Bar chart showing the top 10 companies hiring.

- **top_locations.png**  
  Bar chart showing the top 10 job locations.

- **top_titles.png**  
  Bar chart showing the top 10 job titles.

## How It Works

1. Reads the CSV file from:
