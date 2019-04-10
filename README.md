# crime_report
virtualenv crime_venv
source crime_venv/bin/activate

#when inside virtual environment( only for the 1st time)
pip install -r requirements.txt

#to run the script
crime_venv/bin/python crime_plot.py
