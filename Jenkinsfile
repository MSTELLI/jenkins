pipeline {
    agent any

    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('hopi-big-data')
        BUCKET_NAME = "hopi-test-bucket"
        FILE_NAME = "./dag/airflow_first_file.py"
    }

    stages {
        stage('Install gsutil') {
            steps {
                // gsutil yüklemek için gcloud komutunu çağırın
                script {
                    sh "gcloud components install gsutil"
                }
            }
        }
        
        stage('Upload to GCS') {
            steps {
                // Dosyayı GCS'ye yüklemek için gsutil komutunu kullanın
                script {
                    sh "gsutil cp ${FILE_NAME} gs://${BUCKET_NAME}/${FILE_NAME}"
                }
            }
        }
    }
}
