pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root:root'
        }
    }
    
    stages {
        stage('Install Python Deps') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}