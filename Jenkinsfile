properties([disableConcurrentBuilds()])

pipeline { 
    agent {
	label 'python3'
	}
    options {
	buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()	
    }
    stages {
        stage("Install dist and testing"){
            steps {
		sh 'echo "TEST"'
              //  sh 'python3 -m pip install -r requirements.txt'
               // sh 'python3 -m pytest --junitxml=report.xml'
	    }
        }
        stage("Report errors") {
            steps {
                junit 'reports/**/*.xml' 
            }
        }
    }
}
