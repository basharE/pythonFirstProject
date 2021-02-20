pipeline {
	agent any
	stages {
		stage('Pull code from your Github repository') {
			steps {
				git 'https://github.com/basharE/pythonFirstProject.git'
			}
		}
		stage('Run backend') {
			steps {
				sh ' nohup python rest_app.py &'
			}
		}
		stage('Run frontend') {
			steps {
				sh ' nohup python web_app.py &'
			}
		}
		stage('Run backend testing') {
			steps {
				bat 'python backend_testing.py'
			}
		}
		stage('Run frontend testing') {
			steps {
				bat 'python frontend_testing.py'
			}
		}
		stage('Run combined testing') {
			steps {
				bat 'python compined_testing.py'
			}
		}
		stage('clean environemnt') {
			steps {
				bat 'python clean_environment.py'
			}
		}
	}
}