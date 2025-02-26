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
                bat 'docker run -d -p 8777:5000 -v %cd%/Scores.txt:/app/Scores.txt --name wog_flask flaskapp'
            }
        }
        stage('Test') {
            steps {
                // Remove the line to install selenium outside the Docker container

                bat 'docker run --rm -v %cd%/Scores.txt:/app/Scores.txt flaskapp python e2e.py'






            }
        }
        stage('Finalize') {
            steps {
                bat 'docker stop wog_flask'
                bat 'docker rm wog_flask'
                // Push to DockerHub
                bat 'docker tag flaskapp omerkh/flaskapp:latest'
                bat 'docker push omerkh/flaskapp:latest'
            }
        }
    }
}
