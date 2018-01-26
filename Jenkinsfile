pipeline {
  agent {
    dockerfile {
      filename 'backend/Dockerfile'
    }
    
  }
  stages {
    stage('test') {
      agent {
        dockerfile {
          filename 'backend/Dockerfile'
        }
        
      }
      steps {
        pwd()
      }
    }
  }
}