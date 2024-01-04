```python
from bson.objectid import ObjectId

class User:
    def __init__(self, data):
        self.id = str(data.get('_id')) if data.get('_id') else None
        self.name = data.get('name')
        self.email = data.get('email')
        self.password = data.get('password')  # This should be hashed and salted in a real-world scenario
        self.goals = data.get('goals', [])
        self.interactions = data.get('interactions', [])

    def to_dict(self):
        return {
            '_id': ObjectId(self.id) if self.id else None,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'goals': self.goals,
            'interactions': self.interactions
        }
```
