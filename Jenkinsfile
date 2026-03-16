

pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'echo Running Playwright tests'
            }
        }
    }
}
