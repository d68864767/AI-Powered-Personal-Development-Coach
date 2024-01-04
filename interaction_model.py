```python
from bson.objectid import ObjectId
from datetime import datetime

class Interaction:
    def __init__(self, data):
        self.id = str(data.get('_id')) if data.get('_id') else None
        self.user_id = data.get('user_id')
        self.question = data.get('question')
        self.answer = data.get('answer')
        self.timestamp = data.get('timestamp', datetime.now())  # Default timestamp is current time

    def to_dict(self):
        return {
            '_id': ObjectId(self.id) if self.id else None,
            'user_id': self.user_id,
            'question': self.question,
            'answer': self.answer,
            'timestamp': self.timestamp
        }
```
