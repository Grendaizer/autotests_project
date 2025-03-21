import subprocess
import os
from config import ALLURE_RESULTS_DIR

PYTHON_PATH = os.path.join(os.getcwd(), "venv", "Scripts", "python.exe")

subprocess.run([PYTHON_PATH, "-m", "pytest", "tests", f"--alluredir={ALLURE_RESULTS_DIR}"])
