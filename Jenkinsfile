pipeline {
    agent {
        label 'slave1'
    }
    stages {
        stage('Git') {
            steps{
                git branch: 'feature1', url: 'https://github.com/Smruti861/srbehera.git'
            }
        }
        stage('shell') {
            steps{
                sh 'bash sum.sh'
            }
        }
    }
}
