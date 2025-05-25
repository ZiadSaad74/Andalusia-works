# Welcome to my works during my journey with Andalusia Business Solutions.

# Repositry Ovreview:
This repository contains several analytical tasks for my position in **Andalusia Health Business Solutions**, like dashboards, machine learning models, web scraping data projects. Below is a breakdown of each folder, including descriptions, objectives, and the main skills or tools used.

# 1- AWP dashboard:

**Description**: 
- A Power BI dashboard designed for a real estate team data that targets doctors (DRs) to sell Andalusia clinics.
- It provides actionable insights about team performance metrics, the distributions of lead sourses (Digital - Referrals) The dashboard helps the team track key indicators, identify high-potential leads, total results for agent calls with leads, and optimize their sales strategy.

**Dashboards features**
- Total interested leads sold over time.
- Conversion rate (Leads to Interested leads).
- Average time to close a deal for each agent.
- Touchability (If there's agent call/meet this lead of not) and reachability for the leads (If the lead answered the agent calls or not )
- The results of all agents calls.
- Interactive Filters: Filter by Agent name, doctor specialty, time period (e.g., Year, Month).
- Visualizations: Includes bar charts, pie charts, and KPI cards for a clear overview of performance.

# 2- Agents Performance and Response Rate Analysis.

**Description**: 
- A Python-based data analysis project designed for the real estate team, data source is CRM database.

- This project provides actionable insights into agent performance, lead response delays, optimal call timings, and overall lead reachability. The goal is to enhance engagement, improve follow-up strategies, and optimize scheduling based on data-driven findings.

**Project Features**:
- Delayed Response Time Analysis: Measures the time between lead assignment and the first call to identify operational inefficiencies and improve responsiveness.

- Optimal Call Timing (Days & Hours): Determines the best days and hours to contact doctors by analyzing call logs and response patterns to increase answered calls.

- Agent Performance Evaluation: Assesses each agent's reachability rate (calls answered) and interest rate (converted to interested leads), identifying high and low performers.

- Unreachability Pattern Detection: Highlights hours with low engagement and high unreachability to avoid inefficient calling times.

- Actionable Insights for Management: Provides insights that guide team leaders in scheduling improvements, resource allocation, and targeted training.

**Preprocessing Steps**:
- Cleaned missing values in key fields: Specialty, Last Call Status, Appointment Results, Not Interested Reason, and Follow-up Action.
- Identified and resolved inconsistencies such as missing lead activities and mismatched call records between datasets.
- Filtered data between October 1, 2024 and February 10, 2025 according to the business requirement.
- Merged the Leads dataset with Phone Calls Activity logs for consolidated analysis.

**Techniques**: Python, Pandas, Matplotlib and Seaborn for visualizations

# 3- AHA – Internship Management System
**Description:**

- A smart internship recommendation system developed for Andalusia Academy, designed to resolve inconsistencies in job titles and improve alignment between candidate roles and available training programs.

- The system uses a keyword-based matching algorithm to recommend the most suitable training programs or individual courses based on the candidate's job title. It supports HR recruiters in program assignment and optimizes the training workflow.

**Project Features**:

- Smart Matching of Job Titles to Programs:
Uses keyword-driven logic to accurately map job titles to relevant training programs, solving the challenge of inconsistent and unstructured job data.

- Recruiter Support During Interviews:
The dashboard acts as a support tool for HR recruiters, helping them make informed decisions during interviews by suggesting the most relevant training paths.

- Fallback Course Recommendation System:
If a lead is not suitable for an existing program, the system searches for relevant individual training courses and provides recommendations accordingly.

- Enhanced Data Collection Process:
Due to low-quality input data (missing values, free-text fields), a proposal was sent to improve the Ads application form structure, suggesting new columns and dropdown fields to streamline future processing.

- Manual System Dependency:
The current data pipeline is manually maintained through a SharePoint Excel sheet. The importance of CRM integration was discussed to make the system more dynamic and scalable.

**Preprocessing Steps**:

- Data Cleaning:
Fixed missing values and incorrect entries, especially in City and Job Title fields, which were originally input as free-text instead of dropdowns.

- Matching Challenges:
The Job Title field had a high number of unique and inconsistent values, making matching difficult. A dynamic, dictionary-based solution was proposed and is currently under discussion with CRM and team managers.

- Manual Data Updates:
Since the system isn't yet connected to the CRM, the data is manually updated by specialists via SharePoint Excel.

- System Deployment:
The dashboard and model were completed and sent to Mr. Mohammad Mossad for hosting and future integration.


# 4- Ads Leads Analysis by Locations
**Description:**

- A Power BI dashboard project designed to analyze leads generated from social media ads, with a specific focus on geographic engagement.

- The objective is to determine which governorates generate the most leads and to understand how call outcomes vary across different locations. This helps optimize marketing strategies and improve targeting for future ad campaigns.

**Project Features**:

- Governorate-Level Lead Engagement Analysis:
Visualizes which governorates engage the most with ads and contribute the highest volume of leads.

- Call Result Distribution by Location:
Breaks down call outcomes (e.g., Interested, Not Interested, No Answer) for each governorate to assess lead quality by area.

- Percentage-Based Comparisons:
Displays the percentage of each call result per location, helping identify strong and weak performance zones.

- Interactive Filtering:
Enables filtering by Governorate or Agent Name for detailed exploration and extraction of insights.

- Exportable Insights:
The dashboard allows users to export segmented data based on location or agent for reporting or follow-up purposes.

**Preprocessing Steps**:

- Data Cleaning:
Cleaned and prepared the raw dataset provided by the Social Media Specialist, ensuring it was 100% ready for analysis.

- Dataset Merging:
Merged the ad lead data with the main leads dataset, filtered from 1st December 2024, since the ads data only contained lead name and governorate.

- Dashboard Implementation:
Performed the full analysis and visualization in Power BI, focusing on geographic performance and call result metrics.

- Scraping Doctors’ Data
Description:

# 5- Scrapping doctors’ information from external medical platforms.

- The purpose was to enrich the Andalusia CRM with verified data about doctors across various specialties, regions, and institutions to support targeted marketing and recruitment efforts.

**Project Features**:

- Automated Web Scraping:
Collected public information about doctors, including names, specialties, cities, institutions, and contact details.

- Multi-Site Integration:
The script was designed to handle different website structures and extract structured data across multiple directories.

- Data Standardization:
Ensured all collected data was cleaned, normalized, and formatted to be imported directly into the CRM system.

- Duplicate Detection and Handling:
Applied logic to detect and remove duplicates using fuzzy matching to avoid redundant entries in the CRM.

- Specialty-Based Filtering:
Scraped profiles were categorized by medical specialty to support segmentation and focused communication.

**Preprocessing Steps**:

- Web Scraping Script Development:
Built using Python, with libraries such as BeautifulSoup, Requests, and Selenium (for dynamic pages).

- Data Cleaning and Structuring:
Cleaned inconsistent values, removed invalid entries, and structured data into a tabular format with fields like Name, Specialty, City, Institution, and Contact.

- Validation:
Random samples were manually validated to ensure scraping accuracy before pushing the full dataset.




