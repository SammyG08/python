import google.generativeai as genai
import pyttsx3 as tts
import os

genai.configure(api_key= os.environ["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.0-pro-latest')
response = model.generate_content("The opposite of hot is")
print(response.text)

# engine = tts.init()
# engine.say(model.generate_content('The opposite of cold is'))
# engine.runAndWait()
# engine.stop()
#
