```python
import unittest
from app import app
from database import Database
from openai_api import generate_advice, generate_answer
from user_model import User
from goal_model import Goal
from interaction_model import Interaction

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = Database()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b"Welcome to the AI-Powered Personal Development Coach!")

    def test_create_user(self):
        user_data = {
            'name': 'Test User',
            'email': 'testuser@example.com',
            'password': 'testpassword',
            'goals': [],
            'interactions': []
        }
        response = self.app.post('/user', json=user_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['name'], 'Test User')

    def test_create_goal(self):
        goal_data = {
            'user_id': 'testuserid',
            'title': 'Test Goal',
            'description': 'This is a test goal',
            'status': 'Not Started',
            'progress': 0
        }
        response = self.app.post('/goal', json=goal_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['title'], 'Test Goal')

    def test_create_interaction(self):
        interaction_data = {
            'user_id': 'testuserid',
            'type': 'Question',
            'content': 'This is a test question',
            'response': 'This is a test response'
        }
        response = self.app.post('/interaction', json=interaction_data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json()['type'], 'Question')

    def test_generate_advice(self):
        prompt = "I'm feeling stressed about work. What should I do?"
        advice = generate_advice(prompt)
        self.assertIsNotNone(advice)

    def test_generate_answer(self):
        question = "How can I improve my time management skills?"
        answer = generate_answer(question)
        self.assertIsNotNone(answer)

if __name__ == '__main__':
    unittest.main()
```
