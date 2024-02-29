pipeline {
    agent any

    properties([disableConcurrentBuilds(), pipelineTriggers([pollSCM('* * * * *')])])

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                script {
                    docker.build('wog/main-score:latest')
                }
            }
        }

        stage('Run') {
            steps {
                writeFile file: 'scores.txt', text: '25'
                script {
                    docker.image('wog/main-score:latest').run('-p 8777:5000 -v scores.txt:/app/scores.txt')
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    docker.image('wog/main-score:latest').inside {
                        sh 'python e2e.py'
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    docker.image('wog/main-score:latest').stop()
                    docker.image('wog/main-score:latest').push('wog/main-score:latest')
                }
            }
        }
    }
}