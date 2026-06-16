pipeline {
    agent any

    stages {

        stage('Clean Workspace') {
            steps {
                cleanWs()
            }
        }

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

            publishHTML([
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'DemoQA Test Report',
                keepAll: true,
                allowMissing: false,
                alwaysLinkToLastBuild: true
            ])

            archiveArtifacts(
                artifacts: 'screenshots/*.png',
                allowEmptyArchive: true
            )

            echo 'Pipeline execution completed'
        }

        success {
            echo 'Tests Passed Successfully ✅'
        }

        failure {
            echo 'Tests Failed ❌ - Check HTML report and screenshots'
        }
    }
}