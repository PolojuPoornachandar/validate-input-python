pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/PolojuPoornachandar/validate-input-python.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("validate-input-app")
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    docker.image("validate-input-app").inside {
                        sh 'python -m unittest test_app.py'
                    }
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        docker.image("validate-input-app").push()
                    }
                }
            }
        }
    }
}

