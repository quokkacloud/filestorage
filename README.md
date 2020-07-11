# File storage
## Code characteristics

    Works on Python 3.7

## Setting up a development environment

    # Install required Python packages 
    pip install -r requirements.txt
    # You need `curl` to test API
    apt-get install curl
    
## Initializing the Database

    # Create DB tables and populate the tables
    python manage.py db upgrade

## Running the app

    # Start the Flask development web server
    python manage.py runserver
    

# TESTING

    # Show all files and their hash
    >> curl -X GET http://127.0.0.1:5000/files    
    
    # Upload new file
    >> curl -X POST --form file=@<path_to_your_file> http://127.0.0.1:5000/files
    
    # Delete file 
    >> curl -X DELETE http://127.0.0.1:5000/files/<hash_string>
    
    # Download file from server
    >> curl -X GET http://127.0.0.1:5000/files/<hash_string> --output <files_name>
    Or use your web browser
    http://127.0.0.1:5000/files/<hash_string>
    
