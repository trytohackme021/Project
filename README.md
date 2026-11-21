# RIMS Central Library Strategic Turnaround Project
## Project 1: "The Empty Library" — Comprehensive Deliverables Package

**Institution:** Rajasthan Institute of Management & Sciences (RIMS)  
**Consultancy Mandate:** 1-Week Comprehensive Library Usage Audit, Collection Rationalization under a 30% Budget Reduction (Saving ₹5.40 Lakh), and Next-Semester Turnaround Roadmap.

---

## Deliverables Directory & File Index

### 1. Dataset & Data Dictionary (`/data`)
- **Dataset (CSV):** [`rims_library_data.csv`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/data/rims_library_data.csv)  
  *300 synthetic records with exact columns: record_id, department, resource_type, subject_category, publication_year, times_issued_last_year, downloads_last_year, annual_cost, visit_time_slot, student_year, satisfaction_score.*
- **Data Dictionary:** [`data_dictionary.md`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/data/data_dictionary.md)  
  *Complete specification of data types, descriptions, domain values, and analytical integrity notes.*
- **Generator Script:** [`generate_data.py`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/data/generate_data.py)

### 2. Julius-Style Usage Analytics & Graphs (`/analysis`)
- **Analysis Report & Insights:** [`analysis_insights.md`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/analysis/analysis_insights.md)  
  *Executive summary with 1–2 lines of actionable insight for each graph.*
- **Interactive Visual Dashboard:** [`analysis_dashboard.html`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/analysis/analysis_dashboard.html)  
  *Browser dashboard displaying KPIs and all 5 high-res charts.*
- **5 High-Resolution Charts (300 DPI):**
  1. [`graph_1_usage_by_department.png`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/analysis/graph_1_usage_by_department.png) — *Physical Checkouts vs. Digital Downloads by Department.*
  2. [`graph_2_issues_vs_publication_year.png`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/analysis/graph_2_issues_vs_publication_year.png) — *Regression analysis proving the pre-2015 "Currency Cliff".*
  3. [`graph_3_cost_vs_usage.png`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/analysis/graph_3_cost_vs_usage.png) — *Cost-Per-Use scatter plot highlighting ₹7.2L journal drain.*
  4. [`graph_4_visits_by_time_slot.png`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/analysis/graph_4_visits_by_time_slot.png) — *Operating hours analysis revealing 60% drop after 3 PM.*
  5. [`graph_5_satisfaction_by_year.png`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/analysis/graph_5_satisfaction_by_year.png) — *Satisfaction decay from UG-1st Year to PG-2nd Year.*
- **Chart Generation Script:** [`generate_charts.py`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/analysis/generate_charts.py)

### 3. Collection Decision Note (`/report`)
- **Executive Decision Memorandum:** [`collection_decision_note.md`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/report/collection_decision_note.md)  
  *Formal 1–2 page advisory memo answering all three core scenario questions:*
  - *Q1: Departmental, subject, and time-slot usage analysis & root cause breakdown.*
  - *Q2: Resource triage matrix (40 journals to drop, core texts to retain, ₹12.60L budget reallocation).*
  - *Q3: 3-pillar action plan (Night Owl Hours, Course Reserve Bank, Collaborative Commons) and measurable semester KPIs.*

### 4. Library Campaign Pack (`/campaign_pack`)
- **Design & Canva AI Prompt Specifications:** [`campaign_copy_and_design_specs.md`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/campaign_pack/campaign_copy_and_design_specs.md)
- **Visual Campaign Previewer:** [`campaign_preview.html`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/campaign_pack/campaign_preview.html)
- **Instagram Post (1080 × 1080 px):** [`instagram_post_1080x1080.svg`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/campaign_pack/instagram_post_1080x1080.svg)  
  *Theme: "No More 5 PM Curfew" | Data Point: 60% class schedule drop-off | CTA: Claim your desk.*
- **Campus Poster (A3 Portrait):** [`poster_A3.svg`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/campaign_pack/poster_A3.svg)  
  *Theme: "Tired of Outdated Textbooks?" | Data Point: 45% pre-2015 obsolete books | CTA: Scan QR code for 2024 Reserve texts.*

### 5. Gamma Presentation Deck (`/deck`)
- **Gamma Markdown Presentation Deck (10 Slides):** [`gamma_slide_deck.md`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/deck/gamma_slide_deck.md)  
  *Formatted for direct copy-paste into Gamma.app, including layout guides and conversational Speaker Notes.*
- **Interactive Browser Slide Deck:** [`gamma_presentation_deck.html`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/deck/gamma_presentation_deck.html)  
  *Ready-to-present web deck with keyboard arrow navigation.*

### 6. Prompt Log (`/prompts`)
- **Engineering Iteration Log:** [`prompt_log.md`](file:///C:/Users/Asus/.gemini/antigravity/scratch/project_1_empty_library/prompts/prompt_log.md)  
  *Detailed comparison of First Prompt vs. Improved Prompt and What Changed across all 5 project phases.*
