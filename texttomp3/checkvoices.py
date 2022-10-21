import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[6].id)
engine.setProperty("rate", 178)
engine.say("Why is little Annie's shoe floating in the sea?	 Because the shark burped. ")
engine.runAndWait()
engine.stop()
