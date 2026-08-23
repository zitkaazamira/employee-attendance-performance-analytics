# Attendance & Performance Analytics 🌷

An interactive people analytics project built with Python and Streamlit to explore employee attendance patterns, performance metrics, and department-level trends.

## Live Demo

Coming soon.

## Project Overview

Attendance and performance data are often stored separately or reviewed only as administrative records.

This project turns those records into an interactive analytical workspace where users can explore attendance patterns, compare departments, review employee performance, and identify records that may need further attention.

The project also explores the relationship between attendance and performance without assuming that correlation represents causation.

## Main Features

### People Analytics Snapshot

Provides a quick overview of:

• Number of employees  
• Average attendance rate  
• Average performance score  
• Average late frequency  
• Employees that may need attention  

### Interactive Filters

The analysis can be filtered by:

• Department  
• Month  

This allows users to explore specific teams or reporting periods.

### Department Comparison

Compares departments using indicators such as:

• Attendance rate  
• Performance score  
• Late frequency  
• Absence days  
• Target achievement  

### Attendance vs Performance

Explores whether attendance patterns appear to be associated with employee performance.

The app calculates a correlation value and provides an interactive scatter plot.

This analysis is exploratory. A correlation does not mean that attendance causes higher or lower performance.

### Attention List

The app creates a simple review list based on several indicators, including:

• Attendance below 90%  
• Performance score below 75  
• High frequency of lateness  
• High number of absence days  

The list can be sorted to help prioritize which records should be reviewed first.

### Data Export

Filtered employee records can be downloaded as CSV for further analysis or reporting.

## Workflow

```text
Employee Records
       ↓
Attendance Metrics
       ↓
Performance Metrics
       ↓
Department Comparison
       ↓
Relationship Analysis
       ↓
Attention List
       ↓
Export Data
```

## Tools

Python  
Pandas  
Streamlit  
OpenPyXL  

## Dataset

The application includes a synthetically generated dataset containing monthly records for 120 employees across six departments.

The dataset includes:

• Employee ID  
• Department  
• Month  
• Working days  
• Present days  
• Late occurrences  
• Leave days  
• Absence days  
• Attendance rate  
• Performance score  
• Target achievement  
• Workload category  
• Evaluation status  

No confidential employee or organizational data is used.

## Why I Built This

Administrative records can provide useful insights beyond routine documentation.

I built this project to explore how attendance and employee performance data can be transformed into information that supports monitoring, reporting, and further evaluation.

It also demonstrates how simple statistical analysis can be combined with an interactive dashboard to make operational data easier to understand.

## Important Note

The employee attention flags used in this project are simplified portfolio rules and are not formal HR evaluation criteria.

The relationship between attendance and performance is also presented as an exploratory association rather than a causal conclusion.

## Run Locally

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run people_pulse_analytics.py
```

## Project Structure

```text
employee-attendance-performance-analytics/
├── people_pulse_analytics.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

## Notes

This project was created for portfolio and learning purposes using synthetic data.
