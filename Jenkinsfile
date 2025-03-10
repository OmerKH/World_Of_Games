pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/OmerKH/World_of_Games.git'
            }
        }
        stage('Build') {
            steps {
                // bat 'docker build -t flaskapp .'
                sh 'docker-compose build'
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
                sh 'python test/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker stop flask_app'
                sh 'docker rm flask_app'
                // Push to DockerHub
                sh 'docker tag flaskapp omerkh/flaskapp:latest'
                sh 'docker push omerkh/flaskapp:latest'

            }
        }
    }
}
