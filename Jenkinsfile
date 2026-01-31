pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests & Coverage') {
            steps {
                sh '''
                export PYTHONPATH=$PWD
                pytest --cov=app --cov-report=xml tests/
                '''
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    docker run --rm \
                      -e SONAR_HOST_URL=$SONAR_HOST_URL \
                      -e SONAR_LOGIN=$SONAR_AUTH_TOKEN \
                      -v $PWD:/usr/src \
                      sonarsource/sonar-scanner-cli
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
