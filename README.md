---

# CMS Healthcare Efficiency Analysis: NC vs. US Benchmark

## **Project Purpose**

Automated the extraction and transformation of multi-sheet CMS Medicare data using Python to benchmark North Carolina’s healthcare outcomes against national averages. This project establishes a high-integrity dataset for identifying cost-efficiency gaps, quality improvement targets, and future visual modeling in Power BI.

---

## **Project Highlights (2021 Data)**

| Metric | United States (Avg) | North Carolina | Variance |
| --- | --- | --- | --- |
| **Total Discharges** | 7,361,070 | 230,418 | -- |
| **Avg. Payment / Discharge** | $15,324 | $14,429 | **-5.8% (Cost Savings)** |
| **ER Dependency Rate** | 79.33% | 79.49% | **+0.16%** |
| **Mortality Rate** | 4.71% | 5.04% | **+0.33%** |
| **Avg. Length of Stay** | 5.51 Days | 5.62 Days | **+0.11 Days** |

---

## **Strategic Insights**

* **Cost Efficiency:** North Carolina demonstrates measurable cost-effectiveness, spending nearly **6% less per discharge** than the national US average.
* **Quality Improvement:** The slight positive variance in **Mortality** and **Length of Stay (LOS)** suggests a strategic opportunity for targeted quality improvement initiatives.
* **Predictive Value:** This dataset provides the baseline for a future predictive model aimed at optimizing LOS without compromising patient outcomes.

---

## **Technical Challenges and Solutions**

### **1. Structural Data Traps**

* **Challenge:** CMS datasets utilize multi-line headers and metadata rows that break standard dataframe imports.
* **Solution:** Developed a **Discovery Loop** that scans every tab and row to dynamically locate the header anchor ("Area of Residence") regardless of sheet position or index.

### **2. Version Compatibility (Pandas 2.2+)**

* **Challenge:** Addressed the deprecation of `.applymap()` which caused script failures in modern Python environments.
* **Solution:** Implemented a version-agnostic cleaning function using a conditional attribute check (`hasattr(df, 'map')`) to ensure cross-environment stability.

### **3. Data Normalization & Integrity**

* **Challenge:** Overcame inconsistent string formatting, including hidden newlines (`\n`), currency symbols, and commas that interfere with numeric analysis.
* **Solution:** Built a **Regex-based cleaning pipeline** to force high-integrity numeric conversion, ensuring the data is "model-ready" for Power BI.

---

## **File Structure**

* `python_cleaning_script.py`: The core automation engine.
* `requirements.txt`: Environment configuration for reproducibility.
* `NC_vs_US_Healthcare_Final_Consolidated.xlsx`: The final cleaned and modeled dataset.

---
