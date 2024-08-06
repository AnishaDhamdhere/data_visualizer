# Django CSV Visualizer

A Django-based web application that allows users to upload CSV files, performs data analysis using pandas and numpy, and displays the results and visualizations on the web interface.

## Features

- File upload feature for CSV files
- Basic data analysis (first few rows, summary statistics, missing values)
- Data visualization (histograms for numerical columns)

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/django-csv-analyzer.git
   cd data_visualizer```
2. **Create a virtual environment**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install the dependencies**
   ```
   pip install -r requirements.txt
   ```
4. **Run the migrations**
   ```
   python manage.py migrate
   ```
5. **Start the server**
   ```
   python manage.py runserver
   ```
6. **Open browser and navigate to**
   ```
   http://127.0.0.1:8000/
   ```


## Usage

*** Upload a CSV file ***
Go to the root URL (http://127.0.0.1:8000/).
Use the file upload form to upload your CSV file.


*** View Analysis Results ***
After uploading, you will be redirected to a results page.
The results page will display:
The first few rows of the data
Summary statistics for numerical columns
Information on missing values
Histograms for numerical columns