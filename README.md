
## Description:

This project was created to facilitate directory backups.

It reads directories and files that have been modified over a period of days and thus makes a zip with only new files.

## Running the project:

### Create virtual environment
    python3 -m venv venv

### Installing project dependencies
    pip install -r requirements.txt

### Environment variables (example)
    LAST_DAYS=10
    PATH_DIRECTORIES="/home/jhonatannobrega/dir1,/home/jhonatannobrega/dir2"

## For future modifications (dev):

### Update dependency backup
    pip freeze > requirements.txt