# **CMS Healthcare Efficiency Analysis: NC vs. US Benchmark**

## **Project Purpose**

I developed an analytical pipeline to investigate healthcare cost and efficiency disparities between North Carolina and the United States. This project began with the **automated extraction and transformation** of multi-sheet CMS data using **Python** and concluded with the design of a **complete Power BI dashboard**. The goal was to establish a high-integrity dataset to identify cost-efficiency gaps and quality improvement targets.

## **Project Highlights**

The following metrics reflect the data processed via Python and modeled using custom measures:

| Metric | United States (Avg) | North Carolina | Variance (NC vs. US) |
| --- | --- | --- | --- |
| **Avg. Payment / Discharge** | **$15,172** | **$14,603** | **-$569 (3.7% Savings)** |
| **Avg. Length of Stay (LOS)** | **6.35 Days** | **6.58 Days** | **+0.23 Days** |
| **Mortality Rate %** | **4.45%** | **4.78%** | **+0.33%** |

## **Strategic Insights**

I’ve identified several key statewide implications:

* **Cost Efficiency Paradox:** North Carolina demonstrates measurable cost-effectiveness, spending **3.7% less** per discharge than the national average.
* **Operational Bottleneck:** The **0.23-day higher stay variance** suggests an opportunity for operational optimization within NC facilities to improve patient throughput.
* **Quality Benchmarking:** The slightly higher **Mortality Rate (4.78%)** relative to the national baseline (4.45%) identifies a strategic target for quality improvement initiatives.

## **Technical Execution**

### **1. Data Engineering (Python)**

* **Discovery Loop:** Developed a script to scan multi-sheet CMS files and dynamically locate header anchors to handle structural data.
* **Data Integrity:** Built a **regex-based pipeline** to force numeric conversion, stripping inconsistent currency symbols, commas, and hidden newlines.

### **2. Analytical Modeling**

* **DAX:** Authored measures like `Payment Variance` and `Stay Variance` using `CALCULATE` and `DIVIDE` to ensure accurate comparisons regardless of region size.
* **UX:** Designed a high-contrast dashboard allowing instant visual comparisons of cleaned data.

## **File Structure**

* **`python_cleaning_script.py`**: The core automation and data engineering engine.
* **`Power BI visualization.pbix`**: The final interactive Power BI dashboard.
* **`NC_vs_US_Healthcare_Final_Consolidated.xlsx`**: Clean dataset ready for business modeling.

---

<img width="1452" height="795" alt="image" src="https://github.com/user-attachments/assets/e9494249-3a22-444e-bfa9-1e246a6ce191" />
