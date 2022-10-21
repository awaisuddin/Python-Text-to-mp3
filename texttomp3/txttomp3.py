# Import the required module
import pyttsx3
  
# Create a string
string = "Why is little Annie's shoe floating in the sea?	 Because the shark burped.  "

# Initialize the Pyttsx3 engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')

engine.setProperty('voice', voices[6].id)

engine.setProperty("rate", 178)
  
# We can use file extension as mp3 and wav, both will work
engine.save_to_file(string, 'speech.mp3')
  
# Wait until above command is not finished.
engine.runAndWait()
