pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/OmerKH/wog_v2'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t omerkh/flaskapp:latest .'
            }
        }
        stage('Run') {
            steps {
                sh 'helm lint world-of-games'
                sh 'helm upgrade --install wog-release world-of-games -f world-of-games/values.yaml'
            }
        }
        stage('Test') {
            steps {
                sh 'pip3 install -r requirements.txt'
                sh 'python3 test/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'helm uninstall wog-release || true'
                // Push to DockerHub
                sh 'docker push omerkh/flaskapp:latest'
            }
        }
    }
}
