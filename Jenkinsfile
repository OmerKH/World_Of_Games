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
                bat 'docker build -t omerkh/flaskapp:latest .'
            }
        }
        stage('Run') {
            steps {
                bat 'helm lint world-of-games'
                bat 'helm upgrade --install wog-release world-of-games -f world-of-games/values.yaml'
            }
        }
        stage('Test') {
            steps {
                bat 'pip3 install -r requirements.txt'
                bat 'python3 test/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                bat 'helm uninstall wog-release || true'
                // Push to DockerHub
                bat 'docker push omerkh/flaskapp:latest'
            }
        }
    }
}
