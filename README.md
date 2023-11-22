# Text-to-Speech Synthesizer with MySQL Database Integration
This Flask application is designed to convert user-provided text inputs into audio files using the Google Text-to-Speech (gTTS) library and persist the synthesized audio files alongside user input data into a MySQL database.

## Table of Contents
Overview
Features
Setup Instructions
Usage
File Structure
Contributing
License
Overview

This application serves as a RESTful API using Flask, allowing users to submit text input through an HTTP POST request to /synthesize_voice. The provided text is converted into an audio file using gTTS and saved, along with the user input, to a designated MySQL database table.

## Features
Synthesize user input text into an audio file using the Google Text-to-Speech (gTTS) API.
Store synthesized audio files and corresponding user inputs into a MySQL database.
Provides a simple API endpoint for synthesizing voices and saving to the database.

## Setup Instructions

#Installation
Ensure you have Python installed. Install the required Python packages using:
  pip install -r requirements.txt

# MySQL Database Setup
  Create a MySQL database and a table with the following columns:

  file_path (VARCHAR)
  user_input (TEXT)
Ensure the table schema matches the column names and types specified above.

## Configuration
Modify the DatabaseManager initialization parameters in the code (host, user, password, database) to match your MySQL database credentials.


## Running the Application
Execute the Flask app:
python your_file_name.py

## Usage
Send a POST request to /synthesize_voice.
Include a form parameter user_input containing the text to synthesize.

## Notes
The application saves the generated audio file and user input to the specified MySQL database table.

## File Structure
.
├── your_file_name.py       # Main Flask application file
└── user_data/              # Directory to store generated audio files
    └── voice_timestamp.mp3 # Example of generated audio file

## Contribution
Feel free to contribute to improve this project by creating issues or pull requests.

## License
This project is licensed under the MIT License.
