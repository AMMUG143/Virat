pipeline{
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                git credentialsId :'AMMUG143', url :'https://github.com/AMMUG143/Virat.git', branch :'main'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate.bat
                python -m pip install --upgrade pip
                pip install -r requirement.txt
                '''
                }
            }

        stage('Run Tests') {
            steps {
                bat '''
                call venv\\Scripts\\activate.bat
                pytest test_login.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Tests passed!'
        }
        failure {
            echo 'Tests failed!'
        }
    }
}
        