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
                bat '"C:\\Users\\56989\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat '"C:\\Users\\56989\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe" -m pytest'
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

