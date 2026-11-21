import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

records = []

departments = ["Management", "Computer Science", "Commerce", "Humanities", "Basic Sciences"]
dept_weights = [0.35, 0.30, 0.15, 0.10, 0.10]

dept_subjects = {
    "Management": ["Financial Management", "Marketing Strategy", "Supply Chain", "HR & Org Behavior", "Business Analytics", "Operations"],
    "Computer Science": ["Cloud Computing", "AI & Machine Learning", "Data Structures", "Web Development", "Cybersecurity", "Legacy Programming (COBOL/Fortran)"],
    "Commerce": ["Corporate Accounting", "Taxation Law", "Banking & Insurance", "Auditing", "Cost Accounting"],
    "Humanities": ["Modern History", "Philosophy", "English Literature", "Sociology", "Political Science"],
    "Basic Sciences": ["Applied Mathematics", "Engineering Physics", "Environmental Chemistry", "Statistics"]
}

resource_types = ["book", "journal", "e-resource"]
# 60% books, 25% journals, 15% e-resources
res_weights = [0.60, 0.25, 0.15]

time_slots = ["09:00-11:00", "11:00-13:00", "13:00-15:00", "15:00-17:00"]
# Afternoon hours drop off significantly as students have labs/classes or leave early
slot_weights = [0.32, 0.38, 0.20, 0.10]

student_years = ["UG-1st Year", "UG-2nd Year", "UG-3rd Year", "PG-1st Year", "PG-2nd Year"]
year_weights = [0.25, 0.25, 0.20, 0.15, 0.15]

for i in range(1, 301):
    rec_id = f"RIMS-{i:03d}"
    dept = np.random.choice(departments, p=dept_weights)
    res_type = np.random.choice(resource_types, p=res_weights)
    subject = random.choice(dept_subjects[dept])
    
    # Publication Year: Books span 1995 to 2024, Journals 2012 to 2024, E-resources 2018 to 2024
    if res_type == "book":
        # Introduce the "outdated book" problem noted in prompt (many older books)
        if random.random() < 0.45:
            pub_year = random.randint(1996, 2014) # Outdated collection
        else:
            pub_year = random.randint(2015, 2024)
        
        # Books are physically issued, downloads = 0
        downloads = 0
        
        # If book is outdated or legacy topic, issues are near 0
        if "Legacy" in subject or pub_year < 2012:
            issues = random.choices([0, 1, 2, 3], weights=[0.65, 0.20, 0.10, 0.05])[0]
        elif pub_year >= 2020:
            # Core newer textbooks issued 30 - 65 times
            issues = random.randint(25, 62)
        else:
            issues = random.randint(4, 28)
            
        # Annual cost: Books cost ₹400 to ₹3,500
        annual_cost = int(random.randint(450, 3200))
        
    elif res_type == "journal":
        pub_year = random.randint(2015, 2024)
        issues = 0 # Journals are accessed or downloaded
        
        # High cost, low download problem noted in scenario
        # "Many journals have fewer than 10 downloads a year"
        if random.random() < 0.60:
            downloads = random.randint(0, 9)
        else:
            downloads = random.randint(10, 45)
            
        # Journal annual subscription cost is very high: ₹25,000 to ₹85,000
        annual_cost = int(random.randint(24000, 85000))
        
    else: # e-resource (e-books, databases, IEEE/EBSCO packages)
        pub_year = random.randint(2018, 2024)
        issues = 0
        # E-resources have moderate to high downloads
        downloads = random.randint(18, 180)
        # Annual package cost: ₹12,000 to ₹50,000
        annual_cost = int(random.randint(12000, 48000))
        
    time_slot = np.random.choice(time_slots, p=slot_weights)
    student_yr = np.random.choice(student_years, p=year_weights)
    
    # Satisfaction score (1 to 5)
    # Correlated with resource currency and usefulness
    if res_type == "book" and pub_year < 2014:
        satisfaction = random.choices([1, 2, 3], weights=[0.55, 0.35, 0.10])[0]
    elif res_type == "journal" and downloads < 10:
        satisfaction = random.choices([1, 2, 3], weights=[0.40, 0.40, 0.20])[0]
    elif pub_year >= 2021:
        satisfaction = random.choices([3, 4, 5], weights=[0.15, 0.50, 0.35])[0]
    else:
        satisfaction = random.choices([2, 3, 4], weights=[0.30, 0.50, 0.20])[0]
        
    records.append({
        "record_id": rec_id,
        "department": dept,
        "resource_type": res_type,
        "subject_category": subject,
        "publication_year": pub_year,
        "times_issued_last_year": issues,
        "downloads_last_year": downloads,
        "annual_cost": annual_cost,
        "visit_time_slot": time_slot,
        "student_year": student_yr,
        "satisfaction_score": satisfaction
    })

df = pd.DataFrame(records)
output_path = r"C:\Users\Asus\.gemini\antigravity\scratch\project_1_empty_library\data\rims_library_data.csv"
df.to_csv(output_path, index=False)
print(f"Generated {len(df)} rows successfully.")
print(df.head())
print("\nSummary Statistics:")
print(f"Total Annual Cost represented: Rs. {df['annual_cost'].sum():,}")
print(f"Total Books: {(df['resource_type']=='book').sum()}, Journals: {(df['resource_type']=='journal').sum()}, E-resources: {(df['resource_type']=='e-resource').sum()}")
print(f"Journals with <10 downloads: {((df['resource_type']=='journal') & (df['downloads_last_year'] < 10)).sum()} / {(df['resource_type']=='journal').sum()}")
print(f"Books with 0-3 issues: {((df['resource_type']=='book') & (df['times_issued_last_year'] <= 3)).sum()} / {(df['resource_type']=='book').sum()}")
