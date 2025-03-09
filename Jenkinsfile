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
                bat 'docker build -t flaskapp .'
            }
        }
        stage('Run') {
            steps {
                bat 'docker run -d --name flask_app -p 8777:8777 -v %cd%/Scores.txt:/app/Scores.txt flaskapp'
            }
        }
        stage('Test') {
            steps {
                // Run the e2e tests
                bat 'python test/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                // Stop and remove the container
                bat 'docker stop flask_app'
                bat 'docker rm flask_app'

                // Push to DockerHub
                bat 'docker tag flaskapp omerkh/flaskapp:latest'
                bat 'docker push omerkh/flaskapp:latest'
            }
        }
    }
}
