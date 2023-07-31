pipeline {
    agent any
    environment {
        // Python dosyasının adını belirleyin
        PYTHON_FILE_NAME = "airflow_test.py"
        // GCS deposu ve klasör yolunu belirleyin
        GCS_BUCKET = "hopi-test-bucket"
        GCS_FOLDER = "suleyman"
    }
    stages {
        stage('Upload Python File to GCS') {
            steps {
                script {
                    // Google Cloud SDK'nın yüklü olduğundan emin ol
                    def gcpCredentials = credentials('new-service')
                    withCredentials([file(credentialsId: 'new-service', variable: 'GCP_CREDENTIALS_JSON')]) {
                        // Google Cloud SDK'nın yüklü olduğundan emin ol
                        sh 'gcloud version'
                        
                        // Python dosyasını GCS'ye yükle
                        sh "gcloud auth activate-service-account --key-file=${GCP_CREDENTIALS_JSON}"
                        sh "echo 'Copying ${PYTHON_FILE_NAME} to gs://${GCS_BUCKET}/${GCS_FOLDER}/${PYTHON_FILE_NAME}'"
                        sh "gsutil cp ${PYTHON_FILE_NAME} gs://${GCS_BUCKET}/${GCS_FOLDER}/${PYTHON_FILE_NAME}"
                        
                        // Ekstra çıktılar
                        sh "echo 'Python File Upload Completed'"
                        sh "gsutil ls gs://${GCS_BUCKET}/${GCS_FOLDER}/"
                    }
                }
            }
        }
    }
}
