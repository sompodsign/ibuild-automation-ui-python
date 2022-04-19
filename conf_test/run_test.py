import subprocess
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from utils.excel_utils import read_configuration_data_from_excel
from utils.json_utils import json_reader
from utils.general_functions import read_date, read_time, get_html_reports
from send_mail import send_report

test_environment_type = json_reader("config.json")['settings']["environmentType"]
configuration_data = read_configuration_data_from_excel("./test_data/{}_test_data.xlsx".format(test_environment_type))

parallel = configuration_data["parallel_run"]
test_item = configuration_data["test_item"].casefold()

ui_report_file_name_prefix = f"{'ui' if test_item == 'both' else test_item}_{read_date()}_{read_date()}_{read_time()}"
api_report_file_name_prefix = f"{'api' if test_item == 'both' else test_item}_{read_date()}_{read_date()}_{read_time()}"

# Individually will run each test case
individual_ui_run_command = f"pytest -s --alluredir=reports/{'ui' if test_item == 'both' else test_item}_report_allure/{ui_report_file_name_prefix} " \
                            f"--html=reports/{'ui' if test_item == 'both' else test_item}_report_html/report_{ui_report_file_name_prefix}.html --self-contained-html tests/ui_testcases"

# Individually will run each api test case
individual_api_run_command = f"pytest -s --alluredir=reports/{'api' if test_item == 'both' else test_item}_report_allure/{api_report_file_name_prefix} " \
                             f"--html=reports/{'api' if test_item == 'both' else test_item}_report_html/report_{api_report_file_name_prefix}.html --self-contained-html tests/api_testcases"

# Test cases will run based on the amount of threads available
parallel_ui_run_command = f"pytest -s -n auto --alluredir=reports/{'ui' if test_item == 'both' else test_item}_report_allure/{ui_report_file_name_prefix} " \
                          f"--html=reports/{'ui' if test_item == 'both' else test_item}_report_html/report_{ui_report_file_name_prefix}.html --self-contained-html tests/ui_testcases"

# Test cases will run based on the amount of threads available
parallel_api_run_command = f"pytest -s -n auto --alluredir=reports/{'api' if test_item == 'both' else test_item}_report_allure/{api_report_file_name_prefix} " \
                           f"--html=reports/{'api' if test_item == 'both' else test_item}_report_html/report_{api_report_file_name_prefix}.html --self-contained-html tests/api_testcases"


def run_api_and_ui_testcases():
    """
    Run the test cases based on the test item sequentially
    :return:
    """
    subprocess.run(individual_api_run_command, shell=True)
    subprocess.run(individual_ui_run_command, shell=True)


def parallel_ui_testcases_run():
    """
    Run the test cases based on the test item in parallel
    :return:
    """
    subprocess.run(parallel_ui_run_command, shell=True)


def parallel_api_testcases_run():
    """
    Run the test cases based on the test item in parallel
    :return:
    """
    subprocess.run(parallel_api_run_command, shell=True)


def individual_ui_testcases_run():
    """
    Run the test cases based on the test item sequentially
    :return:
    """
    subprocess.run(individual_ui_run_command, shell=True)


def individual_api_testcases_run():
    """
    Run the test cases based on the test item sequentially
    :return:
    """
    subprocess.run(individual_api_run_command, shell=True)


# decide which mode to run the test cases
if parallel == "yes" and test_item == "ui":
    parallel_ui_testcases_run()
elif parallel == "yes" and test_item == "api":
    parallel_api_testcases_run()
elif test_item == "ui" and parallel == "no":
    individual_ui_testcases_run()
elif test_item == "api" and parallel == "no":
    individual_api_testcases_run()
elif test_item == "both":
    run_api_and_ui_testcases()

# send report if generated
html_reports = get_html_reports(test_item)

#TODO: issue on report collecting
# send report to receivers email
project_name = configuration_data["project_name"]
report_receiver_email = configuration_data["report_receiver"]
# send_report(report_receiver_email, html_reports, project_name)

# allure report serve
# ui_allure_serve_command = f"allure serve reports/{test_item}_report_allure/{report_file_name_prefix}"
# api_allure_serve_command = f"allure serve reports/{test_item}_report_allure/{report_file_name_prefix}"
#
# if test_item == "ui":
#     subprocess.run(ui_allure_serve_command, shell=True)
# else:
#     subprocess.run(api_allure_serve_command, shell=True)
