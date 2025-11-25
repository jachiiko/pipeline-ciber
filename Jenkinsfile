pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/jachiiko/pipeline-ciber.git'
            }
        }

        stage('Install dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Generate documentation') {
            steps {
                bat 'doxygen Doxyfile'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'html/**', fingerprint: true
        }
    }
}
