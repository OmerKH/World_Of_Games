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
                bat 'docker-compose build --no-cache'
            }
        }
        stage('Run') {
            steps {
                bat 'docker-compose up -d'
                // sh 'docker run -d --name flask_app -p 8777:8777 -v $(pwd)/Scores.txt:/app/Scores.txt flaskapp'
            }
        }
        stage('Test') {
            steps {
                bat 'python test/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                bat 'docker-compose down'
                // Push to DockerHub
                bat 'docker tag flaskapp omerkh/flaskapp:latest'
                bat 'docker push omerkh/flaskapp:latest'

            }
        }
    }
}
