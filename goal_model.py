```python
from bson.objectid import ObjectId

class Goal:
    def __init__(self, data):
        self.id = str(data.get('_id')) if data.get('_id') else None
        self.user_id = data.get('user_id')
        self.title = data.get('title')
        self.description = data.get('description')
        self.status = data.get('status', 'Not Started')  # Default status is 'Not Started'
        self.progress = data.get('progress', 0)  # Default progress is 0

    def to_dict(self):
        return {
            '_id': ObjectId(self.id) if self.id else None,
            'user_id': self.user_id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'progress': self.progress
        }
```
