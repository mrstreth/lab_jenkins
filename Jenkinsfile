pipeline { 
    agent {
	    label 'python3'
    }
    options {
        timestamps()	
    }
    stages {
        stage("Install dist"){
            steps {
		sh 'echo "step1"'
//sh 'python3 -m pip install -r requirements.txt'
	        }
        }
        stage("Testing"){
            steps {
		sh 'echo "step2"'
                //sh 'python3 -m pytest --junitxml=report.xml'
	        }
        }
        stage("Report errors") {
            steps {
		sh 'echo "step3"'
                //junit 'reports/**/*.xml' 
            }
        }
    }
}
