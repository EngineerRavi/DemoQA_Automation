pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                bat '"C:\\Users\\ravi.jangra\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m venv venv'
            }
        }

        stage('Install Dependencies') {
            steps {
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

    post {
        always {
            echo 'Pipeline execution completed'
        }

        success {
            echo 'Tests Passed Successfully ✅'
        }

        failure {
            echo 'Tests Failed ❌ - Check logs'
        }
    }
}