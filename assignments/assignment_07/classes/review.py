from datetime import datetime

class Review:
    def __init__(self, reviewer, rating, comment="", timestamp=None):
        self.reviewer = reviewer
        self.rating = rating
        self.comment = comment
        self.timestamp = timestamp or datetime.now()

    def __str__(self):
        return f"{self.reviewer} rated {self.rating}/5: {self.comment}"
    
    def to_dict(self):
        return {
            "reviewer": self.reviewer,
            "rating": self.rating,
            "comment": self.comment,
            "timestamp": self.timestamp.isoformat()
        }