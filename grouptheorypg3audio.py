import pyttsx3

text = "This set of matrices forms a group under matrix multiplication. " \
"First, the associative property holds. For any matrices A, bee, and C from this set, A B times C is equal to A times B C. " \
"Second, there is an identity eye such that A times eye and eye times A are equal to A for all A.   " \
"Lastly, for every element A, there exists an inverse such that A times A inverse and A inverse times A are equal to the identity eye. "
engine = pyttsx3.init()

engine.setProperty('rate', 135) # Set rate

engine.save_to_file(text, 'grouptheorypg3.mp3') # Save to file
engine.runAndWait()