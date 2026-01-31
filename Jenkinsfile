pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Pull code from your repository
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                // Runs tests and generates an XML coverage report for SonarQube
                sh 'pytest --cov=app --cov-report=xml tests/'
            }
        }

      
    }

    post {
        always {
            // Clean up the workspace after completion
            cleanWs()
        }
    }
}
