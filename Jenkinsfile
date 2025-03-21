pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Grendaizer/autotests_project.git'
            }
        }
        stage('Setup Python & venv') {
            steps {
                bat '''
                C:\\Users\\alexe\\AppData\\Local\\Programs\\Python\\Python39\\python.exe -m venv venv
                call venv\\Scripts\\activate
                venv\\Scripts\\python.exe -m pip install --upgrade pip
                venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                venv\\Scripts\\python.exe run_tests.py
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                allure generate allure-results -o allure-report --clean
                '''
            }
        }
        stage('Publish Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
            }
        }
    }
}
