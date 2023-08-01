pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://https://github.com/MSTELLI/jenkins.git'
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python ./pythonsulo.py'
            }
        }
    }
}
