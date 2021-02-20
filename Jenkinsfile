pipeline {
	agent any
	stages {
		stage('Pull code from your Github repository') {
			steps {
				git 'https://github.com/basharE/pythonFirstProject.git'
			}
		}
		stage ("Install Application Dependencies") {
            steps {
                sh '''
                    pip install -r requirements.txt
                    deactivate
                   '''
           }
        }
		stage('Run backend') {
			steps {
				sh 'nohup python rest_app.py &'
			}
		}
		stage('Run frontend') {
			steps {
				sh 'nohup python web_app.py &'
			}
		}
		stage('Run backend testing') {
			steps {
				sh 'python backend_testing.py'
			}
		}
		stage('Run frontend testing') {
			steps {
				sh 'python frontend_testing.py'
			}
		}
		stage('Run combined testing') {
			steps {
				sh 'python compined_testing.py'
			}
		}
		stage('clean environemnt') {
			steps {
				sh 'python clean_environment.py'
			}
		}
	}
}