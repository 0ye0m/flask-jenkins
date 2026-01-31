pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
    steps {
        sh '''
        set -e

        apt-get update

        apt-get install -y \
            python3 \
            python3-pip \
            python3-venv \
            build-essential \
            git \
            curl \
            wget \
            ca-certificates \
            libssl-dev \
            libffi-dev

        python3 -m pip install --upgrade pip setuptools wheel
        python3 -m pip install -r requirements.txt
        '''
    }
}



        stage('Run Tests & Coverage') {
            steps {
                sh '''
                export PYTHONPATH=$PWD
                python3 -m pytest --cov=app --cov-report=xml tests/
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
