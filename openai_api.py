```python
import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_advice(prompt):
    """
    Function to generate advice using OpenAI GPT-3
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.6,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in generating advice: {str(e)}")
        return None

def generate_answer(question):
    """
    Function to generate answer to a question using OpenAI GPT-3
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=question,
            temperature=0.6,
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"Error in generating answer: {str(e)}")
        return None
```
