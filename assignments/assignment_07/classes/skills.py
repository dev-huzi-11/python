class Skills:
    def __init__(self, name, level="Beginner", category="Programming"):
        self.name = name
        self.level = level
        self.category = category

    def __str__(self):
        return f"{self.name} {self.level} {self.category}"
    
    def to_dict(self):
        return {
            "name": self.name,
            "level": self.level,
            "category": self.category
        }