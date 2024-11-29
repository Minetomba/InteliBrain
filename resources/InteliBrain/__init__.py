import json
import random
import os
class ChatBot:
    def __init__(self, intents_file: str):
        """
        Initialize the IntentHandler with the path to the intents.json file.
        """
        try:
            os.chdir("Resources")
            with open(intents_file, 'r', encoding='utf-8') as file:
                self.intents = json.load(file)
            os.chdir("..")
        except FileNotFoundError:
            raise FileNotFoundError("The intents file was not found.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the intents file.")
    
    def get_response(self, user_input: str):
        """
        Process the user input and return a matching response from intents.json.
        
        Parameters:
            user_input (str): The user input.
        
        Returns:
            str: A random response from the matching intent or a default message if no match is found.
        """
        # Normalize input to lowercase for matching
        normalized_input = user_input.lower()
        
        for intent in self.intents.get("intents", []):
            patterns = intent.get("patterns", [])
            # Match ignoring case
            if any(normalized_input == pattern.lower() for pattern in patterns):
                return random.choice(intent.get("responses", []))
        
        return "I'm sorry, I didn't understand that. Can you rephrase?"

    def list_intents(self):
        """
        List all available intent tags from the intents.json file.
        
        Returns:
            list: A list of intent tags.
        """
        return [intent.get("tag", "unknown") for intent in self.intents.get("intents", [])]
