import json
from OpenAI.openai_handler import OpenAIHandler
 
handler = OpenAIHandler()

job_description = (
    "The primary responsibilities of the Data Scientist include analyzing large datasets, "
    "developing predictive models, and providing actionable insights to stakeholders. "
    "Experience with Python, R, SQL, and machine learning frameworks is required."
)

messages = handler.create_messages(job_description)

try:
    result = handler.generate_chat_completion(messages)
    print("API Response:")
    print(json.dumps(result, indent=4))
except Exception as e:
    print(f"An error occurred: {e}")