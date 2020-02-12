def sendEmailOnFailure() {
    emailext(attachLog: true, body: "$BUILD_URL", subject: "Failure: $JOB_NAME #${env.BUILD_NUMBER}",
        recipientProviders: [[$class: 'RequesterRecipientProvider'], [$class: 'DevelopersRecipientProvider']])
}

pipeline {
    agent any

    environment {
        TESTS_CONTAINER = 'integ-tests'
    }

    parameters {
        booleanParam(defaultValue: false, description: 'Deploy', name: 'PUSH_AND_DEPLOY')
    }

    options{
        disableConcurrentBuilds()
        timeout(time: 5, unit: 'MINUTES')
    }

    stages {
/*        stage('Build image') {
            steps{
                sh('cd app/ && docker build . -t apache')
            }
        }

        stage('Start service') {
            steps{
                sh('cd app/ && docker run -d apache')
            }
        }
*/


        stage('Start service') {
            steps{
                sh  '''
		    ./apache
		    '''
            }
        }

    }

}