from OpenAI.logger import Logger
import os
import json
from openai import OpenAI
from dotenv import load_dotenv

class OpenAIHandler:
    def __init__(self):
        self.logger = Logger("openai.log")
        self.logger.log.info("Initializing OpenAI Handler")
        self._configure_openai()


    def _configure_openai(self):

        self.logger.log.info("Configuring OpenAI Client")
        load_dotenv()
        OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

        if not OPENAI_API_KEY:
            self.logger.log.error("API Key is missing in .env file.")
            raise EnvironmentError("API Key is missing in .env file.")
        
        self.client = OpenAI(
            api_key=os.environ.get("OPENAI_API_KEY"),
        )

    def create_messages(self, description: str) -> list:
        return [
            {
                "role": "system",
                "content": """You are an assistant that extracts structured data from job descriptions in JSON format. Please ensure the output matches the following keys: Workscheme, Description, TechStack, YoE, MinLevelStudies, and English. The English key should be a boolean (True/False) that indicates whether the position requires English language proficiency, if the initial job description is in English, assume English as a requirement. If the information is in a language other than English, translate it and use English only. Do not add information about the company in the Description, only include relevant information about the job. Add all relevant information about the techstack, including all languages and hard skills. Return only the JSON object as the output, without anything else before or after it."""
            },
            {
                "role": "user",
                "content": f"""Here's an example of how I want the job description processed:
        Job Description:
        "The main challenge for the Artificial Intelligence Developer is to develop and implement advanced AI solutions that optimize educational and administrative processes. This position requires the ability to apply cutting-edge AI technologies to enhance learning quality, automate administrative processes, and support data-driven decision-making, driving innovation and efficiency in the institution."

        Output:
        {{
        "Workscheme": "N/A",
        "Description": "The main challenge for the Artificial Intelligence Developer is to develop and implement advanced AI solutions that optimize processes, improve learning quality, and support decision-making through data-driven technologies.",
        "TechStack": ["Python", "R", "SQL", "NoSQL", "Agile Methodologies"],
        "YoE": "N/A",
        "MinLevelStudies": "N/A",
        "English": False
        }}

    Now process this new job description:
    "{description}"
    """
            }
        ]


    def generate_chat_completion(self, messages: list) -> json:
        try:
            completion = self.client.chat.completions.create(
                messages=messages,
                model="gpt-4o-mini",
                response_format={"type": "json_object"},
            )
            result = completion.choices[0].message.content
            parsed_result = json.loads(result)
       
            return parsed_result
        
        except Exception as e:
            self.logger.log.error(f"Unexpected error: {e}")
            raise