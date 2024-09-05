import logging
import os
import openai
from dotenv import load_dotenv

class OpenAIApiHandler:
    def __init__(self):
        self._configure_openai()
        self._configure_logging()

    def _configure_openai(self):
        load_dotenv()
        self.OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
        self.OPENAI_API_BASE = os.environ.get('OPENAI_API_BASE')

        if not self.OPENAI_API_KEY or not self.OPENAI_API_BASE:
            raise EnvironmentError("API Key and/or API Base URL are missing.")
        
        openai.api_type = "azure"
        openai.api_key = self.OPENAI_API_KEY
        openai.api_base = self.OPENAI_API_BASE
        openai.api_version = "2023-03-15-preview"

    def _configure_logging(self):
            """Configure logging settings."""
            logging.basicConfig(level=logging.ERROR, format='%(asctime)s [%(levelname)s]: %(message)s')

    def generate_chat_completion(self, messages: list, temp: float = 0) -> str:
        """
        Generate chat completion using OpenAI API.

        :param messages: The messages array to pass to the API
        :return: The content from the response or an error message
        """
        try:
            response = openai.ChatCompletion.create(
                engine="gpt-35-turbo",
                messages=messages,
                temperature=temp,
                max_tokens=4000,
                top_p=0.95,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None
            )
            return response['choices'][0]['message']['content']
        except openai.error.OpenAIError as e:
            logging.error(f"Error during API call: {e}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            raise
