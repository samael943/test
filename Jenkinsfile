def sendEmailOnFailure() {
    emailext(attachLog: true, body: "$BUILD_URL", subject: "Failure: $JOB_NAME #${env.BUILD_NUMBER}",
        recipientProviders: [[$class: 'RequesterRecipientProvider'], [$class: 'DevelopersRecipientProvider']])
}

pipeline {
    agent any

    options{
        disableConcurrentBuilds()
        timeout(time: 10, unit: 'MINUTES')
    }

    stages {
        stage('Build image') {
            steps{
                sh('cd app/ && docker build . -t web-app')
            }
        }

        stage('Run integration tests') {
            steps{
                sh('cd app/ && docker-compose up -d')
                sh('cd tests/ && docker build . -t integration-tests && docker run integration-tests')
            }
        }

    }

    post {
        always {
            sh('cd app/ && docker-compose down')
            cleanWs()
        }
        failure {
            sendEmailOnFailure()
        }
    }
}