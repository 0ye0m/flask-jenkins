pipeline {
    agent any

    stages {
        stage('Setup Virtualenv & Install Dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh '''
                . venv/bin/activate
                export PYTHONPATH=$PWD
                pytest --cov=app --cov-report=xml tests/
                '''
            }
        }

        stage('SonarQube Analysis') {
    steps {
        withSonarQubeEnv('SonarQube') {
            sh '''
            sonar-scanner
            '''
        }
    }
}

    }

    post {
        always {
            cleanWs()
        }
    }
}
