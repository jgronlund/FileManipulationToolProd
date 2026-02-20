This file contains more in depth information on the project.

Integration/Dev-Ops Specific

There is an integration flow for release cycle. Github Actions is setup through the files under .github/workflows.

- ci.yml

- release.yml

The ci.yml will be run per pull request on any branch to make sure the code is following the correct structure using linters and as well as performing how it should with unit testing. It also calculates code coverage and expects at least 70% to be covered.

The release.yml will be run per push to master. It will be checking that the code base still passes the integration tests which will be testing the functionality of the debian product as well as a smoke test checking that the application can setup on the proper platform.

A Dockerfile is also set up for testing purposes. To use make sure you have the Docker application downloaded and then execute:
        
        docker build --platform linux/amd64 -t filetool-test .
        
        docker run --platform linux/amd64 -it filetool-test


To clone this repo for developer work or testing:

        git clone https://github.com/jgronlund/FileManipulationToolProd.git
        
        cd filetool
        
        python3 -m venv venv
        
        source venv/bin/activate
        
        pip install -r requirements.txt
        
        pytest tests/unit
        
        pytest tests/integration (if filetool app is already running) 
