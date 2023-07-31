pipeline {
    agent any
    stages {
        stage('Execute Python Script') {
            steps {
                script {
                    // Python dosyasını çalıştırma ve çıktıyı alıp Jenkins Console Output'a yazdırma
                    def pythonOutput = sh(script: 'python pythonsulo.py', returnStdout: true).trim()
                    echo "Python Output: ${pythonOutput}"
                }
            }
        }
    }
}
