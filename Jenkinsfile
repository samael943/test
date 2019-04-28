def sendEmailOnFailure() {
    emailext(attachLog: true, body: "$BUILD_URL", subject: "Failure: $JOB_NAME #${env.BUILD_NUMBER}",
        recipientProviders: [[$class: 'RequesterRecipientProvider'], [$class: 'DevelopersRecipientProvider']])
}

pipeline {
    agent any

    parameters {
        booleanParam(defaultValue: false, description: 'Deploy', name: 'PUSH_AND_DEPLOY')
    }

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

        stage('Start service') {
            steps{
                sh('cd app/ && docker-compose up -d')
            }
        }

        stage('Run integration tests') {
            steps{
                sh('cd tests/integration/ && docker build . -t integration-tests && docker run --network=host integration-tests')
            }
        }

        stage('Push (mock stage)'){
            when {
                expression {
                    params.PUSH_AND_DEPLOY == true
                }
            }
            steps{
                sh('echo Imitate Push')
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