import os
import openai
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
OPENAI_API_BASE = os.environ.get('OPENAI_API_BASE')

openai.api_type = "azure"
openai.api_key = OPENAI_API_KEY
openai.api_base = OPENAI_API_BASE 
openai.api_version = "2023-03-15-preview"

userPrompt="Write a Python Function to add 2 numbers"

response = openai.Completion.create(
  engine="gpt-35-turbo",
  prompt=userPrompt,
  temperature=0,
  max_tokens=50,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None)

print(response.choices[0].text.strip(" \n"))