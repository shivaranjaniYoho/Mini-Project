# Employee Data Analysis

## About the Project

This project is about analysing employee data using Python.

The project helps us understand employee departments, salaries and salary distribution using charts.

## Dataset

The dataset contains 10 employee records with the following details:

- Employee ID
- Employee Name
- Department
- Salary
- Joining Date
- City

## Python Libraries Used

- Pandas
- Matplotlib
- Seaborn
- Jupyter
- Nbconvert

## Project Structure

```text
employee-report/
│
├── data/
│   └── employees.csv
│
├── charts/
│   ├── department_chart.png
│   ├── salary_chart.png
│   └── salary_distribution.png
│
├── reports/
│   ├── summary.txt
│   └── employee_report.html
│
├── employee_analysis.ipynb
├── README.md
└── requirements.txt
```

## How to Run the Project

### Step 1: Clone the project

```bash
git clone https://github.com/shivaranjaniYoho/employee-report.git
```

### Step 2: Open the project folder

```bash
cd employee-report
```

### Step 3: Install the required libraries

```bash
python -m pip install -r requirements.txt
```

### Step 4: Open Jupyter Notebook

```bash
python -m jupyter notebook
```

Open `employee_analysis.ipynb` and run the cells.

### Step 5: Create HTML Report

```bash
python -m jupyter nbconvert --to html employee_analysis.ipynb --output employee_report.html --output-dir reports
```

## Charts Created

1. Employees by Department
2. Average Salary by Department
3. Employee Salary Distribution

## Conclusion

This project helped me practise Python, Pandas and data visualisation. I used charts to understand employee information and present the findings.

## Project Reports

- Summary report: reports/summary.txt
- HTML report: reports/employee_report.html

## Bonus: Streamlit Dashboard

This project also includes a Streamlit dashboard.

The dashboard displays:
- Employee details
- Employees by department
- Employee salary distribution
- Average salary

### How to run Streamlit

```bash
python -m pip install -r requirements.txt
    python -m streamlit run app.py


Save using `Ctrl + S`.

## Step 44 – Upload your bonus work to GitHub

First, create a new branch:

```powershell
git checkout main
git pull origin main
git checkout -b streamlit-dashboard