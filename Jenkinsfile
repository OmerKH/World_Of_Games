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
                // bat 'docker build -t flaskapp .'
                sh 'docker-compose build --no-cache'
            }
        }
        stage('Run') {
            steps {
                sh 'docker-compose up -d'
                // sh 'docker run -d --name flask_app -p 8777:8777 -v $(pwd)/Scores.txt:/app/Scores.txt flaskapp'
            }
        }
        stage('Test') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python3 test/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker-compose down'
                // Push to DockerHub
                sh 'docker tag flaskapp omerkh/flaskapp:latest'
                sh 'docker push omerkh/flaskapp:latest'

            }
        }
    }
}
