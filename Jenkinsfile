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
                bat 'docker-compose build'

            }
        }
        stage('Run') {
            steps {
                bat 'docker-compose up -d'

            }
        }
        stage('Test') {
            steps {
                // Remove the line to install selenium outside the Docker container

                bat 'docker-compose run --rm e2e_tests'


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
