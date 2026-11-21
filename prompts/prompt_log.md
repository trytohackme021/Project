# Prompt Engineering & Iteration Log
## Project 1: The Empty Library (RIMS Central Library Turnaround)

This log records the prompt engineering methodology, comparative iterations, and architectural adjustments made across every major phase of this project.

---

### Phase 1: Synthetic Dataset & Data Dictionary Generation

#### First Prompt:
```text
Generate a CSV dataset of 300 rows for a university library with columns for department, 
resource type, issues, downloads, cost, and satisfaction. Also make a data dictionary.
```

#### Improved Prompt:
```text
Act as a Principal Academic Data Scientist specializing in higher education library operations. 
Generate a statistically coherent, realistic synthetic dataset of exactly 300 rows representing an 
audit sample for Rajasthan Institute of Management & Sciences (RIMS). 
Institutional parameters: 3,500 students, 45,000 volumes, 60 journals, ₹18 Lakh annual budget facing a 30% reduction.
Required Columns:
1. record_id: Unique string ('RIMS-001' to 'RIMS-300')
2. department: Weighted distribution across ['Management', 'Computer Science', 'Commerce', 'Humanities', 'Basic Sciences']
3. resource_type: ['book', 'journal', 'e-resource'] with ~60% books, 25% journals, 15% e-resources
4. subject_category: Realistic domain subjects per department
5. publication_year: Books spanning 1996–2024 to model the 'outdated book' issue; journals 2015–2024
6. times_issued_last_year: Highly correlated with publication currency (pre-2015 books have 0-3 checkouts; 2021-2024 editions have 30-65 checkouts)
7. downloads_last_year: Model the high-cost low-download dilemma (60% of journals must have <10 downloads)
8. annual_cost: INR values matching realistic procurement (Books: ₹450–₹3,200; Journals: ₹24,000–₹85,000; E-resources: ₹12,000–₹48,000)
9. visit_time_slot: ['09:00-11:00', '11:00-13:00', '13:00-15:00', '15:00-17:00'], showing a steep drop after 3:00 PM due to class schedules
10. student_year: ['UG-1st Year' to 'PG-2nd Year']
11. satisfaction_score: Integer Likert 1-5 correlated with resource currency and cohort level

Also provide a professional markdown Data Dictionary defining types, ranges, domains, and data integrity relationships.
```

#### What Changed & Why:
- **Root Cause Grounding:** The first prompt created generic random numbers that lacked domain logic. The improved prompt introduced explicit correlations matching the scenario: the "pre-2015 book cliff", the "60% journal dormancy rate (<10 downloads)", and the "afternoon lab timetable lockout".
- **Reproducibility:** Seeded pseudo-random generation ensured deterministic statistical distributions so that data totals match institutional fiscal targets (₹18L budget, ₹5.4L savings target).

---

### Phase 2: Julius-Style Data Analytics & Visualization

#### First Prompt:
```text
Make 5 graphs from this library dataset: usage by department, issues vs year, cost vs usage, 
visits by time, and satisfaction by year. Write some insights.
```

#### Improved Prompt:
```text
Act as a Senior Analytics Consultant using Python/Seaborn to generate 5 publication-grade 300 DPI 
charts for RIMS Central Library's executive board:
1. Graph 1 (Usage by Dept): Grouped bar chart comparing physical checkouts vs digital downloads across departments, sorted by total volume.
2. Graph 2 (Issues vs Pub Year): Polynomial regression scatter plot illustrating the 'currency cliff' before 2015, with callout annotations for the dead zone vs syllabus editions.
3. Graph 3 (Cost vs Usage): Cost-per-use efficiency scatter plot color-coded by resource type with quadrant overlays ('High Cost / Low Usage' journals vs 'Low Cost / High Usage' core texts).
4. Graph 4 (Visits by Time Slot): Bar chart showing percentage drop-off across 09:00-17:00, highlighting the 60% collapse after 15:00.
5. Graph 5 (Satisfaction by Year): Box plot and stripplot showing mean satisfaction decay from UG-1st Year to PG-2nd Year.

For every graph, write exactly 1–2 lines of crisp executive insight linking the visual evidence directly to the budget decision.
```

#### What Changed & Why:
- **Visual Clarity & Actionability:** Shifted from generic plotting to purposeful decision charts with visual callout boxes, regression lines, and quadrant overlays.
- **Executive Conciseness:** Formatted insights to follow the strict "1–2 lines of insight each" requirement, ensuring the Principal can digest them in 30 seconds.

---

### Phase 3: Collection Decision Note (Executive Briefing)

#### First Prompt:
```text
Write a 1-2 page note answering which books to drop, which departments have low usage, 
and 3 actions to get students back to the library.
```

#### Improved Prompt:
```text
Draft a formal executive memorandum (1–2 pages) from the External Library Consulting Task Force 
to Prof. Arvind Sharma, Principal of RIMS, and the Library Steering Committee.
Structure the briefing around the three mandatory questions:
1. Department, Category & Time Slot Low Usage Analysis: Cite exact percentages and root causes (syllabus obsolescence, timetable lockout).
2. Resource Rationalization Matrix: Formulate a balanced budget sheet taking the current ₹18.00 Lakh expenditure down to exactly ₹12.60 Lakh (-30% cut), specifying which 40 journals to cancel, which textbooks to fund (+₹30k), and digital e-resource expansion.
3. 3-Pillar Turnaround Plan: (Pillar 1: 8:30 PM Night Owl Hours; Pillar 2: Course Reserve Bank; Pillar 3: Collaborative Co-Working Commons).
Conclude with a quantitative accountability scorecard listing baseline vs target metrics for next semester.
```

#### What Changed & Why:
- **Managerial Tone & Financial Precision:** Transitioned from general suggestions to an official memorandum with a reconciled budget balance sheet accounting for every single rupee of the ₹5.40 Lakh cut.
- **Root Cause Problem-Solving:** Solved the faculty vs student blame game by proving both parties were reacting to a broken system (obsolete books + 5 PM closing time).

---

### Phase 4: Canva AI Library Campaign Pack

#### First Prompt:
```text
Create an Instagram post and a poster to tell students to visit the library.
```

#### Improved Prompt:
```text
Design a cohesive, multi-channel marketing campaign pack for RIMS Central Library:
1. Deliverable A: 1080×1080 Instagram Square Post.
   - Message: 'No More 5 PM Curfew.'
   - Analysis Data Point: 'Visits plunged by 60% after 3 PM because labs run till 4:30 PM. We are now open until 8:30 PM!'
   - CTA: 'Claim your evening study desk tonight.'
2. Deliverable B: A3 Campus Noticeboard Poster (1:1.41 aspect ratio).
   - Message: 'Tired of Outdated Textbooks? So Were We.'
   - Analysis Data Point: '45% of books were over 10 years old with 0 checkouts. We restocked 2024 syllabus editions for every major!'
   - CTA: 'Scan QR code to borrow 2024 semester textbooks from the 1st Floor Reserve Bank.'

Provide:
- Complete Canva AI text prompts for photorealistic/graphic generation
- Pure SVG vector master layouts with full color styling and typography
- Interactive HTML previewer
```

#### What Changed & Why:
- **Requirement Verification:** Added the required "clear message, a CTA, and one data point from your analysis" to both deliverables.
- **Production Readiness:** Delivered both conceptual Canva AI prompts and production-ready vector SVG files so the user has immediate visual assets.

---

### Phase 5: Gamma Slide Deck for the Principal

#### First Prompt:
```text
Make 8 to 10 slides summarizing the report for the principal.
```

#### Improved Prompt:
```text
Create an executive slide deck (exactly 10 slides) tailored for presentation to RIMS Principal Prof. Arvind Sharma.
Format the deck in clean, structured Markdown optimized for direct 1-click import into Gamma.app.
Include:
- Slide 1: Executive Title & Scope
- Slide 2: The Core Problem (30% cut vs footfall decline)
- Slide 3: Currency Cliff & Departmental Disparity
- Slide 4: The Journal Leakage (₹7.2L savings opportunity)
- Slide 5: The Timetable Lockout (09:00-17:00 analysis)
- Slide 6: Reconciled Budget Matrix (₹18L ➔ ₹12.60L)
- Slide 7: The 3-Pillar Turnaround Plan
- Slide 8: Multi-Channel Marketing Campaign Rollout
- Slide 9: Next-Semester Target Scorecard (Measurable KPIs)
- Slide 10: Immediate Action Plan & Call for Approval

For every slide, include slide category, visual layout advice, data callouts, and conversational, persuasive Speaker Notes.
Also build an interactive browser-based slide deck with arrow key navigation.
```

#### What Changed & Why:
- **Executive Delivery:** Built-in speaker notes allow the user to rehearse or speak directly from the deck.
- **Format Flexibility:** Provided both Gamma-compatible markdown and an interactive browser-ready presentation deck.
