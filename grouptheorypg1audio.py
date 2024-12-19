import pyttsx3

text = "Consider the set of two by two real matrices with non-zero determinant."
engine = pyttsx3.init()

engine.setProperty('rate', 135) # Set rate

engine.save_to_file(text, 'grouptheorypg1.mp3') # Save to file
engine.runAndWait()