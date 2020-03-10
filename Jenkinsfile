pipeline { 
    agent any
    options {
        timestamps()	
    }
    stages {
        stage("Install dist"){
            steps {
		git 'https://github.com/mrstreth/lab_jenkins.git'
		sh 'pip3 install -r requirements.txt'
	        }
        }
        stage("Testing"){
            steps {
		sh 'pytest -v --junitxml=report.xml'
	        }
        }
        stage("Report errors") {
            steps {
		junit 'reports/**/*.xml' 
            }
        }
    }
}
