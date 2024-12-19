import pyttsx3

text = "For matrix multiplication, the entry in the eyeth row and jayth column of the product of two matrices A and B is " \
"obtained by multiplying term-by-term the entries of the eyeth row of A and the jayth column of B."
engine = pyttsx3.init()

engine.setProperty('rate', 135) # Set rate

engine.save_to_file(text, 'grouptheorypg2.mp3') # Save to file
engine.runAndWait()