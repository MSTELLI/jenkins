pipeline {
    agent any

    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('gcp-connection')
        BUCKET_NAME = "hopi-test-bucket"
        SOURCE_NAME = "./dag/airflow_first_file.py"
        FILE_NAME = "airflow_first_file.py"
        
    }

    stages {
        stage('Upload to GCS') {
            steps {
                script {
                    sh "gsutil cp ${SOURCE_NAME} gs://${BUCKET_NAME}/${FILE_NAME}"
                }
            }
        }
    }
}
