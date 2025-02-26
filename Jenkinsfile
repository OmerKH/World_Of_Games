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
                // Build the Docker image
                bat 'docker build -t flaskapp .'
            }
        }
        stage('Run') {
            steps {
                // Stop and remove the existing container if it exists
                bat 'docker stop wog_flask || echo "No existing container to stop."'
                bat 'docker rm wog_flask || echo "No existing container to remove."'
                
                // Run the Dockerized application
                bat 'docker run -d -p 8777:5000 -v $(pwd)/Scores.txt:/app/Scores.txt --name wog_flask flaskapp'
            }
        }
        stage('Test') {
            steps {
                bat 'python test/e2e.py'
            }
        }
        stage('Finalize') {
            steps {
                // Terminate the tested container
                bat 'docker stop wog_flask'
                bat 'docker rm wog_flask'
                // Push the new image to DockerHub
                bat 'docker tag flaskapp omerkh/flaskapp:latest'
                bat 'docker push omerkh/flaskapp:latest'
            }
        }
    }
}
