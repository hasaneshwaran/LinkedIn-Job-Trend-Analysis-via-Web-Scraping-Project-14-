# LinkedIn Job Data Analysis - Project Guide

## Overview
This project analyzes LinkedIn job postings data (from Kaggle) to extract useful insights such as:
- Most in-demand job titles
- Top hiring locations
- Most requested skills
- Top industries (from job_industries.csv)
- Basic salary and job type summaries (if available)

The analysis generates:
1. Summary tables (Excel)
2. Bar charts (PNG images)
3. Data formatted for Pivot Tables (for interactive reporting)

---

## Project Files
The Kaggle dataset includes:
- `postings.csv`: Core job postings data (titles, skills, locations, salaries, etc.)
- `job_industries.csv`: Job industry classification data (job_id and industries)
- Other supporting folders (`companies`, `jobs`, `mappings`) not directly needed here.

---

## Setup
1. Install dependencies:
   ```bash
   pip install pandas matplotlib openpyxl
