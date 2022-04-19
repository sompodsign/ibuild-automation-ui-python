import glob
import os
from datetime import datetime


# Read current date
def read_date():
    return str(datetime.today().strftime('%Y-%m-%d'))


# function to read current date and time
def read_datetime():
    return str(datetime.today().strftime('%Y-%m-%d-%H-%M-%S'))


# function to read raw time
def get_raw_time():
    return str(datetime.today().strftime('%Y%d%H%M%S'))


def read_time():
    return str(datetime.today().strftime('%H-%M-%S'))


def get_html_reports(report_type):
    reports = []
    if not report_type == "both":
        try:
            report = os.path.abspath(glob.glob(f"reports/{report_type}_report_html/*.html")[-1])
            reports.append(report)
        except Exception as e:
            print("Report not ready, Error", e)
    else:
        try:
            report1 = os.path.abspath(glob.glob(f"reports/api_report_html/*.html")[0])
            report2 = os.path.abspath(glob.glob(f"reports/ui_report_html/*.html")[0])
            # logs = os.path.abspath(glob.glob("logs/*.log")) # get logs
            reports.append(report1)
            reports.append(report2)
        except Exception as e:
            print("Reports are not ready, Error", e)
    return reports
