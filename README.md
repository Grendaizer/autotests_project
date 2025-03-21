# Autotests Project

This project is a Selenium-based automated testing framework designed for Windows systems. It is fully integrated with Jenkins and Allure for reporting and includes parameterization for flexible execution.

## Installation
### **1. Clone the Repository**
```sh
git clone https://github.com/Grendaizer/autotests_project.git
cd autotests_project
```

### **2. Set Up Python and Virtual Environment**
Ensure you have Python installed and added to the system PATH.

#### **For Local Execution:**
```sh
python -m venv venv
venv\Scripts\activate.bat
pip install --upgrade pip
pip install -r requirements.txt
```

#### **For Jenkins Execution:**
In Jenkins, use the full path to Python when setting up the virtual environment:
```sh
C:\Users\alexe\AppData\Local\Programs\Python\Python39\python.exe -m venv venv
call venv\Scripts\activate
C:\Users\alexe\AppData\Local\Programs\Python\Python39\python.exe -m pip install --upgrade pip
C:\Users\alexe\AppData\Local\Programs\Python\Python39\python.exe -m pip install -r requirements.txt
```

### **3. Set Up Environment Variables**
Create a `.env` file in the root directory if running locally:
```ini
BOT_TOKEN=your_telegram_bot_token
CHAT_IDS=123456789,987654321
HEADLESS=True
DEBUG=True
```
If using Jenkins, set these variables as build parameters.

---

## Running Tests
### **1. Running Locally**
Activate the virtual environment and execute the test script:
```sh
call venv\Scripts\activate
pip install -r requirements.txt
python run_tests.py
```

### **2. Running in Jenkins**
Ensure Jenkins is set up with:
- "This project is parameterized" checked.
- Parameters:
  - `BOT_TOKEN` (string)
  - `CHAT_IDS` (comma-separated Telegram IDs)
  - `HEADLESS` (boolean)
  - `DEBUG` (boolean)
- **Allure Commandline Installed**:
  - Go to Jenkins -> Manage Jenkins -> Global Tool Configuration.
  - Add `Allure Commandline` with installation directory (`D:\Tools\allure-2.33.0`).

Use the full path to Python when running tests in Jenkins:
```sh
C:\Users\alexe\AppData\Local\Programs\Python\Python39\python.exe run_tests.py
```

Run the Jenkins pipeline, and results will be stored in `allure-results`.

---

## Generating Allure Reports
```sh
allure generate allure-results -o allure-report --clean
allure serve allure-report
```
If using Jenkins, ensure the Allure plugin is installed and configured.

---

## Troubleshooting
- **Python not recognized?** Add Python to the system PATH.
- **Allure not found?** Add `D:\Tools\allure-2.33.0\bin` to PATH and restart Jenkins.
- **Missing dependencies?** Run `pip install -r requirements.txt` again.
- **Virtual environment issues?** Ensure `venv` is activated before running tests.

---

## License
This project is open-source and available under the MIT License.

---

### 🚀 Happy Testing!

