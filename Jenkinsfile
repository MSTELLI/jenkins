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
                    sh """
                        python3 -m pip install google-cloud-storage
                        python3 -c '
                        import os
                        from google.cloud import storage
                        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "${GOOGLE_APPLICATION_CREDENTIALS}"
                        client = storage.Client()
                        bucket = client.bucket("${BUCKET_NAME}")
                        blob = bucket.blob("${FILE_NAME}")
                        blob.upload_from_filename("${FILE_NAME}")
                        '
                    """
                }
            }
        }
    }
}
