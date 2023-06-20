# About
Covid data processing and reporting in ADF.

# Poject details
- `ecdc_data`: It has the csv files, which contains daily, weekly reports on hospitalization of covid cases of year 2020.
- `eurostat_data`: This folder has gzip file. This file has human population data by age (of covid patients). These files and folder are processed further using ADF. 
- `lookup_data`: Some look up files for country, date are present inside in this lookup folder, which are used during transfrmation phase. 
- `power_bi_reports` : This report contains visual representation of covid trend.
- `processsd` : It is a generated folder from ADF processing via "mapping data flow", which contains all trasformed data from raw covid data.
- `pyspark_notebooks` : It contains script files, which will be orchestrated by ADF. Once it is triggered by ADF, these sripts will run and perform data transformation in databricks.
- `sql_scripts` : After the data are processed in ADF, it has sql script to create underlying tables in azure sql database. This table will store all the processed data in a schematic way.

# CI/ CD
!(./images/adf-cicd-configuration.PNG)
