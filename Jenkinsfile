pipeline {
	agent any
	options {
        buildDiscarder(logRotator(daysToKeepStr: '5', numToKeepStr: '20'))
    }
    triggers {
        pollSCM 'H/30 * * * *'
    }
    environment {
        registry = "basharegbariya/flask_postgres_py"
        registryCredential = 'basharegbariya'
        dockerImage = ''
    }
	stages {
		stage('Pull code from your Github repository') {
			steps {
				git 'https://github.com/basharE/pythonFirstProject.git'
			}
		}
		stage('install_dependencies') {
            steps {
                sh 'pip3 install flask requests selenium psycopg2-binary -t ./'
            }
        }
		stage('Run backend') {
			steps {
				sh 'nohup python3 rest_app.py &'
			}
		}
		stage('Run backend testing') {
			steps {
				sh 'nohup python3 backend_testing.py &'
			}
		}
		stage('clean environemnt') {
			steps {
				sh 'nohup python3 clean_environment.py &'
			}
		}
		stage('Building image') {
            steps {
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                    docker.withRegistry('', registryCredential) {
                    dockerImage.push() // push image to hub
                    }
                }
            }
        }
	}
	post {
        always {
            bat "docker rmi $registry:$BUILD_NUMBER" // delete the local image at the end
        }
    }
}