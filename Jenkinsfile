pipeline {
	agent any
	options {
		timestamps()
		}
	stages {
		stage("Install dist and testing"){
			steps {
				git 'https://github.com/mrstreth/lab_jenkins.git'
				sh 'pip3 install -r requirements.txt'
				sh 'pytest -v --junitxml=report.xml'
				junit 'reports/**/*.xml' 
				}
		}
	}
}
