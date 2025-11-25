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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pytest'
            }
        }

        stage('Generate documentation') {
            steps {
                sh 'doxygen Doxyfile'
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'html/**', allowEmptyArchive: true
        }
    }
}
