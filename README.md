--------------------------------------------
PROJECT PURPOSE: 
--------------------------------------------

Automated the extraction and transformation of multi-sheet CMS Medicare data using Python to benchmark North Carolina's healthcare outcomes against National averages. 
This project establishes a clean dataset for identifying cost-efficiency gaps, quality improvement targets, and future visual modeling.

--------------------------------------------
Project highlights on returned data: 
--------------------------------------------
United States (Avg) > North Carolina > Variance:

Total Discharges: US 7,361,070 > NC 230,418
Avg. Payment per Discharge: US $15,324 > NC $14,429 > -5.8%
ER Dependency Rate: US 79.33% > NC 79.49% > +0.16%
Mortality Rate: US 4.71% > NC 5.04% > +0.33%
Avg. Length of Stay: US 5.51 Days > NC 5.62 Days > +0.11 Days

---------------------------------------------
Overall findings to be modeled:
---------------------------------------------

North Carolina demonstrates measurable cost-effectiveness, spending nearly 6% less per discharge than the national US average. 
The slight positive variance in Mortality and Length of Stay (LOS) suggests a strategic opportunity for quality improvement initiatives. 
This data may provide the baseline for a predictive model to optimize LOS without compromising patient outcomes.


---------------------------------------------
Technical Challenges & Solutions:
---------------------------------------------

1. CMS datasets use multi-line headers and metadata rows that can break standard imports.
> Solution: Developed a discovery loop that scans every tab and row to dynamically locate the header anchor ("Area of Residence") regardless of sheet position.

2. Version Compatibility (Pandas 2.2+): Addressed the deprecation of .applymap() which caused script failures in modern Python environments.
> Solution: Implemented a version-agnostic cleaning function using a conditional attribute check (hasattr(df, 'map')) to ensure cross-environment stability.

3. Data Normalization: Overcame inconsistent string formatting (hidden newlines \n, currency symbols, and commas).
> Solution: Built a regex-based cleaning pipeline to force high-integrity numeric conversion for future Power BI modeling.
