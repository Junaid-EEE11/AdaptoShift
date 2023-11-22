from flask import Flask, request
import mysql.connector
from datetime import datetime
from gtts import gTTS

app = Flask('app')

# Flask routes...

class DatabaseManager:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def save_to_database(self, file_path, user_input):
        try:
            mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                database=self.database
            )

            mycursor = mydb.cursor()

            # Ensure the table has the required columns
            #mycursor.execute("ALTER TABLE yourtable ADD COLUMN IF NOT EXISTS file_path VARCHAR(255)")
            #mycursor.execute("ALTER TABLE yourtable ADD COLUMN IF NOT EXISTS user_input TEXT")

            # Save file path and user input to the database
            insert_query = "INSERT INTO yourtable (file_path, user_input) VALUES (%s, %s)"
            insert_values = (file_path, user_input)
            mycursor.execute(insert_query, insert_values)
            mydb.commit()

            return True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

@app.route('/synthesize_voice', methods=['POST'])
def synthesize_voice():
    user_input = request.form.get('user_input')
    if not user_input:
        return "Please provide text input", 400

    file_name = "voice_"+str(datetime.utcnow().timestamp()).split('.')[0]
    file_path = f"user_data/{file_name}.mp3"

    tts = gTTS(text=user_input, lang='en')
    tts.save(file_path)

    db_manager = DatabaseManager(
        host="localhost",
        user="root",
        password="junaid",
        database="mydatabase"
    )

    if db_manager.save_to_database(file_path, user_input):
        return f"Voice generated and saved with file path: {file_path} and user input: {user_input}"
    else:
        return "Error saving to the database", 500

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    app.run(debug=True)  # Run the Flask app
