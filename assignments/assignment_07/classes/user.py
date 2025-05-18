class User:
    def __init__(self, name, skills_offered=None, skills_wanted=None):
        self.name = name
        self.skills_offered = skills_offered or []
        self.skills_wanted = skills_wanted or []
        self.sessions = []
        self.reviews = []

    def add_skills_offered(self, skills):
        self.skills_offered.append(skills)

    def add_skills_wanted(self, skills):
        self.skills_wanted.append(skills)

    def add_session(self, session):
        self.sessions.append(session)

    def add_review(self, review):
        self.reviews.append(review)

    def get_profile_summary(self):
        return {
            "name": self.name,
            "skills_offered": [str(skill) for skill in self.skills_offered],
            "skills_wanted": [str(skill) for skill in self.skills_wanted],
            "reviews": [str(review) for review in self.reviews]
        }

    def __str__(self):
        return f"User: {self.name}"