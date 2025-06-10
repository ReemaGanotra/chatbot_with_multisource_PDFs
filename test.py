from google.generativeai import GenerativeModel
import google.generativeai as genai
import os


from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key= os.getenv("Google_API_Key"))
for model in genai.list_models():
    print(model.name)

model = GenerativeModel("gemini-2.0-flash")
response = model.generate_content("Hello, tell me about neural networks")
print(response.text)

