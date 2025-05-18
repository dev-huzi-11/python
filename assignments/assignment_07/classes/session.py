class Session:
    def __init__(self, user1, user2, skills, date):
        self.user1 = user1
        self.user2 = user2
        self.skills = skills if isinstance(skills, list) else [skills]
        self.date = date
        self.status = "Pending"
        self.reviews = []

    def mark_completed(self):
        self.status = "Completed"

    def add_review(self, review):
        self.reviews.append(review)

    def __str__(self):
        skills_names = ", ".join([skill.name for skill in self.skills])
        return f"{self.user1.name} ↔ {self.user2.name} for {skills_names} on {self.date} [{self.status}]"