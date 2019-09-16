node("docker") {
    docker.withRegistry('', 'bef9483a-47b8-4096-9bce-bc0cdd198b9a') {

        git url: "https://github.com/MichaelHaigh/dev-docker-app/", credentialsId: 'aea9e704-c6d6-4aae-91be-7243a5e7e850'
        env.GIT_COMMIT = sh(script: "git rev-parse HEAD", returnStdout: true).trim()

        stage "Build"
        def devdockerapp = docker.build "michaelatnutanix/dev-docker-app"
    
        stage "Publish"
        devdockerapp.push 'latest'
        devdockerapp.push "${env.GIT_COMMIT}"

        stage "Deploy"
        kubernetesDeploy configs: 'dev-docker-dep.yaml', kubeConfig: [path: ''], kubeconfigId: '45312c5c-24d1-4c15-aec3-da4e8637e925', secretName: '', ssh: [sshCredentialsId: '*', sshServer: ''], textCredentials: [certificateAuthorityData: '', clientCertificateData: '', clientKeyData: '', serverUrl: 'https://']
    }
}
