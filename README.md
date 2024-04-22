# Boat Lifestyle Real-Time Sales Dashboard
This project integrates Python, SQL Server, and Power BI to create a real-time sales dashboard for Boat Lifestyle. The dashboard visualizes live sales data and provides insights into product performance, customer trends, and revenue analysis.

## Project Overview
Python Script: A Python script generates random sales data and inserts it into the SQL Server database.
SQL Server Database: Three static tables—product, product details, and customer—are created to store relevant data.
Power BI Report: Power BI connects to the SQL Server database in direct query mode to visualize real-time sales data.
## How It Works
### Python Script: 
The script generates random sales data including sale ID, product key, customer ID, and sale date. It then inserts this data into the respective tables in the SQL Server database.
### SQL Server Database: 
The database contains three static tables: product, product details, and customer. These tables store information about products, their details, and customer demographics.
### Power BI Report:
Power BI connects to the SQL Server database and creates visualizations based on the live data. The report displays key metrics such as total sales, top-selling products, and customer demographics.
## Tables in SQL Server
Product: Stores information about products including product key, name, and category.
Product Details: Contains additional details about each product such as price and description.
Customer: Stores customer data including customer ID, name, age, city, and state.
Files
simulation.py: Python script to generate random sales data.
boat_sales.pbix: Power BI report file.
## Author
Piyush Dhondiyal
## Below, there is a video demonstrating how the project works. Watch it for better understanding.


https://github.com/piyush8781/boat-lifestyle-sales-dashboard/assets/163038938/9fdc25a2-9303-4a8d-bb9f-e3ee104e122f

