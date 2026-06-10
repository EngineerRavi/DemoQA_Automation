pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\python -m pip install --upgrade pip'
                bat 'venv\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\python -m pytest -s --html=reports/report.html --self-contained-html'
            }
        }
    }
}