import subprocess
from config import ALLURE_RESULTS_DIR

subprocess.run(["pytest","tests", f"--alluredir={ALLURE_RESULTS_DIR}"])
