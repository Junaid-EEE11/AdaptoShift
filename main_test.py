from flask import Flask, request
import os
import mysql.connector
from gtts import gTTS

app = Flask('app')

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello_world', methods=['POST', 'GET'])
def hello_world_api():
    user_input = request.args.get('user_input')
    mode = request.args.get('mode')

    if mode not in ['text', 'voice', 'character']:
        return "Invalid mode selected", 400

    user_folder = "user_data"
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    file_path = os.path.join(user_folder, f"user_data_{mode}.txt")
    with open(file_path, 'w') as file:
        file.write(user_input)

    return f"File saved at {file_path}"

try:
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="junaid",
      database="mydatabase"
    )

    mycursor = mydb.cursor()

    mycursor.execute("ALTER TABLE yourtable ADD COLUMN time TIMESTAMP DEFAULT CURRENT_TIMESTAMP")
    mycursor.execute("ALTER TABLE yourtable ADD COLUMN output VARCHAR(255)")

    mydb.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")

class VoiceGenerator:
    def __init__(self, model):
        self.model = model
        
    def generate_voice_from_text(self, text, file_path):
        tts = gTTS(text=text, lang='en')  # Using gTTS for text-to-speech
        tts.save(file_path)
        return file_path  # Return the file path where the voice is saved

# Example usage
model = "Sample Model"
voice_generator = VoiceGenerator(model)

# Generate voice from text and save it to a file
generated_file_path = voice_generator.generate_voice_from_text("This is a test sentence.", "user_voice.mp3")
print(f"Voice saved at {generated_file_path}")
