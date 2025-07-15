pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/OmerKH/World_Of_Games'
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
                sh 'helm upgrade --install wog-release world-of-games -f Helm/values.yaml'
            }
        }
        stage('Test') {
            steps {
                sh 'sleep 30'
                sh "kubectl port-forward svc/world-of-games 8777:8777 &"
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
