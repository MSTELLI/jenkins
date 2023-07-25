pipeline {
    agent any

    environment {
        GOOGLE_APPLICATION_CREDENTIALS = credentials('hopi-big-data') // Jenkins'ta tanımlanmış olan GCS için hizmet hesabı kimlik bilgisi
        BUCKET_NAME = "hopi-test-bucket" // Hedef GCS kovasının adı
        FILE_NAME = "airflow_test.py" // Aktarılacak dosyanın adı
    }

    stages {
        stage('Install gsutil') {
            steps {
                script {
                    sh "gcloud components install gsutil"
                }
            }
        }
        
        stage('Upload to GCS') {
            steps {
                script {
                    sh "gsutil cp ${FILE_NAME} gs://${BUCKET_NAME}/${FILE_NAME}"
                }
            }
        }
    }
}
