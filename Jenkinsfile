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
                // Google Cloud SDK'nın yüklü olduğundan emin ol
                sh 'gcloud version'
                
                // Python dosyasını GCS'ye yükle
                sh "gsutil cp ${PYTHON_FILE_NAME} gs://${GCS_BUCKET}/${GCS_FOLDER}/${PYTHON_FILE_NAME}"
            }
        }
    }
}
