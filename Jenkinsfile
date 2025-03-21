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
                python -m venv venv
                call venv\\Scripts\\activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                python run_tests.py
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
