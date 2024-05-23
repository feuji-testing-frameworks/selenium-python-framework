import subprocess
import threading

def run_ui_testcases() :
    subprocess.run(["pytest" , "./tests/ui_testcases/test_ui.py" , "--alluredir=./allure_report"])

def run_api_testcases() :
    subprocess.run(["pytest" , "./tests/api_testcases/test_api.py" , "--alluredir=./allure_report"])

def run_api_mock_testcases() : 
    subprocess.run(["pytest" , "./tests/api_testcases/test_mockapi.py" , "--alluredir=./allure_report"])

def run_mobile_testcases() :
    subprocess.run(["pytest" , "./tests/mobile_testcases/test_mobile.py" , "--alluredir=./allure_report"])

# Create threads for each category of tests
ui_thread = threading.Thread(target=run_ui_testcases)
api_thread = threading.Thread(target=run_api_testcases)
api_mock_thread = threading.Thread(target=run_api_mock_testcases)
mobile_thread = threading.Thread(target=run_mobile_testcases)

# Start all threads
ui_thread.start()
api_thread.start()
api_mock_thread.start()
mobile_thread.start()

# Wait for all threads to complete
ui_thread.join()
api_thread.join()
api_mock_thread.join()
mobile_thread.join()
