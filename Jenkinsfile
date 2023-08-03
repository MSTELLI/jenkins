pipeline {
    agent any

    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('gcp-connection')
        BUCKET_NAME = "hopi-test-bucket"
        FILE_NAME = "./dag/airflow_first_file.py"
    }

    stages {
        stage('Upload to GCS') {
            steps {
                script {
                    sh "gsutil cp ${FILE_NAME} gs://${GCS_BUCKET}/${FILE_NAME}"
                }
            }
        }
    }
}
