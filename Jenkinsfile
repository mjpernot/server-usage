pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('Test') {
            steps {
                dir ('lib') {
                    git branch: "mod/294", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                dir ('mongo_lib') {
                    git branch: "mod/422", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/mongo-lib.git"
                }
                dir ('mongo_lib/lib') {
                    git branch: "mod/294", credentialsId: "2cfb403c-be21-4fac-94d7-c8cd5c531feb", url: "https://gitlab.code.dicelab.net/JAC-IDM/python-lib.git"
                }
                sh """
                virtualenv test_env
                source test_env/bin/activate
                pip2 install mock==2.0.0 --user
                pip2 install pymongo==3.8.0 --user
                pip2 install psutil==5.4.3 --user
                /usr/bin/python ./test/unit/server_usage/help_message.py
                /usr/bin/python ./test/unit/server_usage/post_process.py
                /usr/bin/python ./test/unit/server_usage/get_svr_mem.py
                /usr/bin/python ./test/unit/server_usage/get_svr_info.py
                /usr/bin/python ./test/unit/server_usage/get_proc_mem.py
                /usr/bin/python ./test/unit/server_usage/run_program.py
                /usr/bin/python ./test/unit/server_usage/main.py
                deactivate
                rm -rf test_env
                """
            }
        }
        stage('SonarQube analysis') {
            steps {
                sh './test/unit/sonarqube_code_coverage.sh'
                sh 'rm -rf lib'
                sh 'rm -rf mongo_lib'
                script {
                    scannerHome = tool 'sonar-scanner';
                }
                withSonarQubeEnv('Sonar') {
                    sh "${scannerHome}/bin/sonar-scanner -Dproject.settings=sonar-project.JACIDM.properties"
                }
            }
        }
        stage('Artifactory upload') {
            steps {
                script {
                    server = Artifactory.server('Artifactory')
                    server.credentialsId = 'art-svc-highpoint-dev'
                    uploadSpec = """{
                        "files": [
                            {
                                "pattern": "./*.py",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/server-usage/"
                            },
                            {
                                "pattern": "./*.txt",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/server-usage/"
                            },
                            {
                                "pattern": "./*.md",
                                "recursive": false,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/server-usage/"
                            },
                            {
                                "pattern": "*.TEMPLATE",
                                "recursive": true,
                                "excludePatterns": [],
                                "target": "pypi-proj-local/highpoint/server-usage/config/"
                            }
                        ]
                    }"""
                    server.upload(uploadSpec)
                }
            }
        }
    }
    post {
        always {
            cleanWs disableDeferredWipeout: true
        }
    }
}
