# WEB LOG ANALYTICS PROJECT

This project involves two major tasks: ETL (Extract, Transform, Load) in Python and Data Visualization in Power BI. The project aims to extract, clean, and transform data using Python and then create interactive visualizations in Power BI.

## Task 1: ETL in Python

In this task, the ETL process is performed using Python. Below are the steps taken:

1. **Data Extraction**
   - Log data is extracted and loaded into a DataFrame, which acts as the staging layer for further processing.

2. **Data Transformation**
   - Various transformations are applied to the data to separate it into Dimensions and a Fact table.
   - Dimensions:
     - Dimension 1: UserIP
     - Dimension 2: File
     - Dimension 3: Date
   - These dimensions are defined based on the specific attributes of the data.

3. **Data Loading**
   - The transformed tables are loaded into a mySQL database for storage and analysis.

## Task 2: Data Visualization in Power BI

In the second task, data visualization is carried out in Power BI. The following steps are taken:

1. **Data Retrieval from mySQL**
   - Data is pulled from the mySQL database where it was loaded during Task 1.

2. **Defining Relationships**
   - Relationships between the tables are defined to establish connections between them. This is essential for creating meaningful visualizations.

3. **Creating Visualizations**
   - Various types of visualizations are created using the data.
   - Dashboards and reports are designed to present the data in an informative and interactive way.

