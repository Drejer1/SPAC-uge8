
# CerealDB api 

A project made as part of [Specialisternes](https://dk.specialisterne.com/) academy course during week 8.

This project is designed build a docker container and CI/CD pipeline based on assignment [insertlink].




## Features


- Create docker container
- Have CI/CD setup
- 
## Installation

1. Clone the repository:
```bash
    git clone https://github.com/Drejer1/SPAC-uge8.git
    cd SPAC-uge8/PythonCerealAPI
```
2. Create a virtual environment and activate it:
```bash
    python -m venv venv 
    source venv/bin/activate  # On Windows 
    use `venv\Scripts\activate`
```
3. Install the required dependencies:
```bash
    pip install -r requirements.txt
```
4. Make sure a local MySQL server is running and containing a database named "cereal_database"
5. Run the query located inside the Miscellaneous folder
6. Run ParseAndInsert.py
7. Run FillDatabaseWithPathsToImages.py
8. Make sure docker/dockerdesktop is installed
9. run command from project folder
```bash
    docker build --tag 'cereal' .
    
```

## Executing
Simply run "docker run -d -p 127.0.0.1:8001:8000"
Check if containers API is visible on localhost:8001


## Feedback wanted on

