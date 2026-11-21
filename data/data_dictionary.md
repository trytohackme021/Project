# Rajasthan Institute of Management & Sciences (RIMS)
## Central Library Usage & Collection Dataset: Data Dictionary

**Dataset File:** `rims_library_data.csv`  
**Total Records:** 300 rows  
**Scope:** Sample audit of 300 representative physical books, subscribed print/electronic journals, and e-resources across academic departments, cross-referenced with patron visit logs and satisfaction metrics.  
**Currency:** Indian Rupee (₹ / INR)

---

### Variable Specifications

| Field Name | Data Type | Description | Allowed / Observed Values | Example |
| :--- | :--- | :--- | :--- | :--- |
| `record_id` | String (Unique ID) | Primary identifier for each library resource record in the audit. | `RIMS-001` through `RIMS-300` | `RIMS-042` |
| `department` | Categorical | Academic department responsible for curriculum requiring the resource. | `Management`, `Computer Science`, `Commerce`, `Humanities`, `Basic Sciences` | `Management` |
| `resource_type` | Categorical | Medium and procurement classification of the resource. | `book` (Physical book/monograph), `journal` (Periodical subscription), `e-resource` (Digital database / e-book package) | `book` |
| `subject_category` | Categorical | Sub-disciplinary classification or course domain of the title. | 25 distinct subjects across 5 departments (e.g., *Financial Management*, *AI & Machine Learning*, *Taxation Law*, *Modern History*, *Applied Mathematics*) | `AI & Machine Learning` |
| `publication_year` | Integer | Year of publication / edition year for books, or current subscription start year for journals. | Range: `1996` to `2024` | `2011` |
| `times_issued_last_year` | Integer | Total number of times a physical book was checked out by students or faculty in the past academic year. | Range: `0` to `62` (Applies to `book`; `0` for digital resources) | `38` |
| `downloads_last_year` | Integer | Number of full-text article or chapter downloads recorded via library IP proxy. | Range: `0` to `180` (Applies to `journal` and `e-resource`; `0` for physical books) | `6` |
| `annual_cost` | Integer (INR) | Annual procurement or subscription recurring cost in Indian Rupees. | Books: ₹450 – ₹3,200<br>Journals: ₹24,000 – ₹85,000<br>E-resources: ₹12,000 – ₹48,000 | `₹52,000` |
| `visit_time_slot` | Categorical | Most frequent student transaction or checkout time slot for this category during library operating hours (09:00 - 17:00). | `09:00-11:00`, `11:00-13:00`, `13:00-15:00`, `15:00-17:00` | `11:00-13:00` |
| `student_year` | Categorical | Primary user academic cohort accessing or associated with the record. | `UG-1st Year`, `UG-2nd Year`, `UG-3rd Year`, `PG-1st Year`, `PG-2nd Year` | `UG-2nd Year` |
| `satisfaction_score` | Integer (Likert) | Student satisfaction rating on a 5-point Likert scale (from library survey exit slips & LMS feedback). | `1` (Very Dissatisfied) to `5` (Very Satisfied) | `2` |

---

### Contextual Data Integrity Notes
1. **The "Outdated Book" Dynamic:** 36.6% (67 of 183) of physical book holdings in the audit sample have publication dates prior to 2014 and recorded 3 or fewer checkouts last year. Conversely, books published in 2020 or later had an average checkout frequency of 43.8 times.
2. **The Journal Utilization Deficit:** 60.6% (40 of 66) of subscribed journals recorded fewer than 10 downloads over the entire year, despite high average costs (₹51,400/journal), creating massive cost-per-download inefficiencies.
3. **Time Slot Drop-off:** Visits peak between 11:00 AM and 1:00 PM (38%), with steep drops after 3:00 PM (10%), aligning with student feedback that classes run until 4:30 PM, leaving no time to visit before the 5:00 PM library closure.
