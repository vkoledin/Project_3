# Project_3
## Netflix Data Analysis
In this project, we decided to analyze the user data on the Netflix platform. We tried to adress the ethical challenges and tried to come up with some solutions. We analyzed the revenue, the demographics and locations. 
## The Dashboard
We built a dashboard to proivde insights into Netflix's user base across different countries, focusing on subscription types and device usage. The dashboard is powered by a Flask backend with interactive Plotly visualizations. The dashbaord has a dropdown menu to select a country allowing the user to see two pie charts that are dynamically generated based on the selected country. These charts show the proportion of subscription types and devices used in the selected country. Below that the user can see a stacked bar chart that provides a global view of subscription types. Each bar represents a country, and the segments within the bars represent different subscription plans allowing the user to compare the popularity of different plans across countries.Finally, there is another dropdown to select a subscription type, and a bar chart that shows the number of users for that plan across different countries. 
The flask backend served several key functions in our dashboard:
**1. Purpose and Functionality:**
* **Data Handling:** It manages the extraction and manipulation of data from our database (or CSV file in this case).
* **API Endpoints:** Flask provides endpoints that our frontend interacts with to retrieve specific data based on user requests.
* **Integration:** It seamlessly integrates with our frontend technologies, ensuring smooth communication and data flow.

**2. Data Management:**
* "We utilized Flask to read our dataset (Netflix userbase data) from a CSV file."
* "Using pandas within Flask, we processed and prepared the data for visualization."
* "We employed Flask's routing capabilities to create API endpoints that deliver JSON data to our JavaScript frontend based on user interactions."


## Data Visualization Track Requirements (75 points)
### Data and Delivery (20 points)
The dataset contains at least 100 unique records. (5 points)

A database is used to house the data (SQL, MongoDB, SQLite, etc.). (5 points)

The GitHub repo has a README.md that includes the following: (10 points)

An overview of the project and its purpose

Instructions on how to use and interact with the project

At least one paragraph summarizing efforts for ethical considerations made in the project

References for the data source(s)

References for any code used that is not your own

### Visualizations (25 points)
A minimum of three unique views present the data. (10 points)
The visualizations are presented in a clear, digestible manner. (5 points)
The data story is easy to interpret for users of all levels. (10 points)
Usability (30 points)
The script, notebook, or webpage created to showcase data visualizations runs without error. (10 points)

A Python or JavaScript library not shown in class is used in the project. (10 points)

The project includes some level of user-driven interaction, conforming to one of the following designs: (10 points)

HTML menus, dropdowns, and/or textboxes to display JavaScript-powered visualizations

Flask backend with interactive API routes that serve back Python or JavaScript created plots

Visualizations created from user-selected filtered data
