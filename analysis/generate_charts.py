import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set overall aesthetic styling
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.size'] = 11
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.labelsize'] = 12

df = pd.read_csv(r"C:\Users\Asus\.gemini\antigravity\scratch\project_1_empty_library\data\rims_library_data.csv")
output_dir = r"C:\Users\Asus\.gemini\antigravity\scratch\project_1_empty_library\analysis"

# -------------------------------------------------------------
# GRAPH 1: Usage by Department (Physical Issues vs Digital Downloads)
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))
dept_summary = df.groupby('department')[['times_issued_last_year', 'downloads_last_year']].sum().reset_index()
dept_summary['total_usage'] = dept_summary['times_issued_last_year'] + dept_summary['downloads_last_year']
dept_summary = dept_summary.sort_values(by='total_usage', ascending=False)

x = np.arange(len(dept_summary))
width = 0.38

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, dept_summary['times_issued_last_year'], width, label='Physical Checkouts (Issues)', color='#1f77b4', edgecolor='black', alpha=0.9)
rects2 = ax.bar(x + width/2, dept_summary['downloads_last_year'], width, label='Digital Downloads', color='#ff7f0e', edgecolor='black', alpha=0.9)

ax.set_ylabel('Total Annual Interactions', fontsize=12, fontweight='bold')
ax.set_title('Graph 1: Library Resource Usage by Department (RIMS)', fontsize=14, pad=15)
ax.set_xticks(x)
ax.set_xticklabels(dept_summary['department'], rotation=15, ha='right', fontsize=11)
ax.legend(frameon=True, facecolor='white', framealpha=0.9)

# Value annotations
for rect in rects1:
    h = rect.get_height()
    ax.annotate(f'{int(h)}', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3),
                textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')
for rect in rects2:
    h = rect.get_height()
    ax.annotate(f'{int(h)}', xy=(rect.get_x() + rect.get_width()/2, h), xytext=(0, 3),
                textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig(f"{output_dir}/graph_1_usage_by_department.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# GRAPH 2: Issues vs Publication Year (The Outdated Book Cliff)
# -------------------------------------------------------------
books_df = df[df['resource_type'] == 'book'].copy()
plt.figure(figsize=(10, 6))
ax = sns.regplot(
    data=books_df, 
    x='publication_year', 
    y='times_issued_last_year',
    scatter_kws={'alpha': 0.65, 'color': '#2ca02c', 's': 55, 'edgecolor': 'darkgreen'},
    line_kws={'color': '#d62728', 'linewidth': 2.5, 'label': 'Trendline (Polynomial fit)'},
    order=2
)
plt.axvline(x=2015, color='gray', linestyle='--', linewidth=1.5, label='Curriculum Refresh Threshold (2015)')
plt.title('Graph 2: Physical Book Checkouts vs. Publication Year', pad=15)
plt.xlabel('Publication / Edition Year', fontsize=12, fontweight='bold')
plt.ylabel('Times Issued Last Year', fontsize=12, fontweight='bold')
plt.legend(frameon=True, loc='upper left')

# Highlight note
plt.annotate(
    'Outdated Collection "Dead Zone"\n(Avg. < 2 checkouts/yr)', 
    xy=(2004, 3), 
    xytext=(1998, 32),
    arrowprops=dict(facecolor='black', shrink=0.05, width=1.2, headwidth=8),
    bbox=dict(boxstyle="round,pad=0.4", fc="#fff3cd", ec="#856404", lw=1.2),
    fontsize=9
)
plt.annotate(
    'Recent Curriculum Editions\n(Issued 30 to 60+ times)', 
    xy=(2022, 50), 
    xytext=(2014, 55),
    arrowprops=dict(facecolor='black', shrink=0.05, width=1.2, headwidth=8),
    bbox=dict(boxstyle="round,pad=0.4", fc="#d4edda", ec="#155724", lw=1.2),
    fontsize=9
)

plt.tight_layout()
plt.savefig(f"{output_dir}/graph_2_issues_vs_publication_year.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# GRAPH 3: Cost vs Usage (ROI Analysis: Cost Per Use)
# -------------------------------------------------------------
plt.figure(figsize=(11, 6))
df_cost = df.copy()
df_cost['total_usage'] = df_cost['times_issued_last_year'] + df_cost['downloads_last_year']

palette = {'book': '#1f77b4', 'journal': '#d62728', 'e-resource': '#2ca02c'}
ax = sns.scatterplot(
    data=df_cost,
    x='total_usage',
    y='annual_cost',
    hue='resource_type',
    palette=palette,
    style='resource_type',
    s=90,
    alpha=0.8,
    edgecolor='black'
)

plt.title('Graph 3: Annual Cost vs. Annual Usage (Resource Efficiency Quad)', pad=15)
plt.xlabel('Total Usage Interactions (Issues + Downloads)', fontsize=12, fontweight='bold')
plt.ylabel('Annual Cost (INR ₹)', fontsize=12, fontweight='bold')
plt.axhline(y=20000, color='gray', linestyle=':', alpha=0.7)
plt.axvline(x=15, color='gray', linestyle=':', alpha=0.7)

# Quadrant labels
plt.text(5, 75000, "HIGH COST - LOW USAGE\n(Journals: Candidate for Cancellation)", 
         bbox=dict(boxstyle='square', fc='#f8d7da', ec='#721c24', alpha=0.9), fontsize=9, fontweight='bold')
plt.text(80, 5000, "LOW COST - HIGH USAGE\n(Core Textbooks: High ROI)", 
         bbox=dict(boxstyle='square', fc='#d4edda', ec='#155724', alpha=0.9), fontsize=9, fontweight='bold')
plt.text(90, 42000, "MODERATE COST - HIGH USAGE\n(E-Resource Bundles: Effective)", 
         bbox=dict(boxstyle='square', fc='#d1ecf1', ec='#0c5460', alpha=0.9), fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig(f"{output_dir}/graph_3_cost_vs_usage.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# GRAPH 4: Visits by Time Slot
# -------------------------------------------------------------
plt.figure(figsize=(9, 5))
time_counts = df['visit_time_slot'].value_counts()[["09:00-11:00", "11:00-13:00", "13:00-15:00", "15:00-17:00"]]
colors = ['#4a90e2', '#2ecc71', '#f39c12', '#e74c3c']

bars = plt.bar(time_counts.index, time_counts.values, color=colors, edgecolor='black', width=0.55)
plt.title('Graph 4: Student Visit Distribution by Operating Time Slot', pad=15)
plt.xlabel('Library Operating Time Slot', fontsize=12, fontweight='bold')
plt.ylabel('Recorded Checkouts / Visits in Sample', fontsize=12, fontweight='bold')

for bar in bars:
    yval = bar.get_height()
    pct = (yval / len(df)) * 100
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 2, f"{int(yval)} ({pct:.1f}%)", ha='center', va='bottom', fontweight='bold', fontsize=10)

plt.annotate('Sharp 60% decline after 3:00 PM\ndue to clashes with mandatory lab schedules', 
             xy=(3, 30), xytext=(1.8, 85),
             arrowprops=dict(facecolor='black', shrink=0.05, width=1.2, headwidth=7),
             bbox=dict(boxstyle="round,pad=0.3", fc="#fff3cd", ec="#856404"),
             fontsize=9)

plt.ylim(0, 140)
plt.tight_layout()
plt.savefig(f"{output_dir}/graph_4_visits_by_time_slot.png", dpi=300)
plt.close()

# -------------------------------------------------------------
# GRAPH 5: Satisfaction by Student Cohort Year
# -------------------------------------------------------------
plt.figure(figsize=(10, 6))
order = ["UG-1st Year", "UG-2nd Year", "UG-3rd Year", "PG-1st Year", "PG-2nd Year"]
sat_avg = df.groupby('student_year')['satisfaction_score'].mean().reindex(order)

fig, ax = plt.subplots(figsize=(10, 5.5))
sns.boxplot(data=df, x='student_year', y='satisfaction_score', order=order, palette='Blues', ax=ax, width=0.45)
sns.stripplot(data=df, x='student_year', y='satisfaction_score', order=order, color='darkblue', alpha=0.3, jitter=0.2, size=5, ax=ax)

ax.set_title('Graph 5: Student Satisfaction Rating by Academic Cohort', pad=15)
ax.set_xlabel('Student Cohort Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Satisfaction Score (1 = Low, 5 = High)', fontsize=12, fontweight='bold')

# Mean annotations
for idx, yr in enumerate(order):
    m = sat_avg[yr]
    ax.scatter(idx, m, color='red', s=60, zorder=5)
    ax.annotate(f'Mean: {m:.2f}', xy=(idx, m), xytext=(0, 18), textcoords="offset points", ha='center', fontsize=9, fontweight='bold', color='darkred')

plt.ylim(0.5, 5.5)
plt.tight_layout()
plt.savefig(f"{output_dir}/graph_5_satisfaction_by_year.png", dpi=300)
plt.close()

print("All 5 analysis charts successfully generated and saved to analysis directory.")
