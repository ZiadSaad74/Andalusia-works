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
