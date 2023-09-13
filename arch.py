import pyttsx3
import os

# Text to be converted to speech
text = "Hello, this is a text-to-speech converter with a male Indian English voice."

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('voice', 'en-in')  # Indian English voice

# Save the converted audio to a file
output_file_path = '/content/drive/My Drive/output1.mp3'
engine.save_to_file(text, output_file_path)

# Wait for the speech to finish
engine.runAndWait()

# Display the link to the saved file
output_file_path
