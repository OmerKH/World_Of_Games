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
                sh 'docker build -t flaskapp .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:5000 -v $(pwd)/Scores.txt:/app/Scores.txt --name wog_flask flaskapp'
            }
        }
        stage('Test') {
            steps {
                sh 'python test/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker stop wog_flask'
                sh 'docker rm wog_flask'
                // Push to DockerHub
                sh 'docker tag flaskapp omerkh/flaskapp:latest'
                sh 'docker push omerkh/flaskapp:latest'

            }
        }
    }
}
