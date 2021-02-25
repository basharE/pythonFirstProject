pipeline {
	agent any
	environment {
        PYTHONPATH = "/Users/basharegbariya/venv/Python3.8/lib"
    }
	stages {
		stage('Pull code from your Github repository') {
			steps {
				git 'https://github.com/basharE/pythonFirstProject.git'
			}
		}
		stage('install_dependencies') {
            steps {
                sh 'pip3 install flask requests selenium pymysql -t ./'
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
				sh 'nohup python backend_testing.py &'
			}
		}
		stage('Run frontend testing') {
			steps {
				sh 'nohup python frontend_testing.py &'
			}
		}
		stage('Run combined testing') {
			steps {
				sh 'nohup python compined_testing.py &'
			}
		}
		stage('clean environemnt') {
			steps {
				sh 'nohup python clean_environment.py &'
			}
		}
	}
}