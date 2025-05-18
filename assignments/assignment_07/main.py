from classes.skills import Skills
from classes.user import User
from engine.matcher import find_matches

# Create skills
skill_python = Skills("Python", "Intermediate", "Programming")
skill_design = Skills("Graphic Design", "Beginner", "Design")
skill_video = Skills("Video Editing", "Beginner", "Media")

# Create users
alice = User("Alice", skills_offered=[skill_python], skills_wanted=[skill_design])
bob = User("Bob", skills_offered=[skill_design], skills_wanted=[skill_python])
carol = User("Carol", skills_offered=[skill_video], skills_wanted=[skill_python])

# All users
users = [alice, bob, carol]

# Run matcher
matches = find_matches(alice, users)

# Debug
print("Matches found:", matches)

# Display results
if __name__ == "__main__":
    for match in matches:
        print(f"{match['match_with']} offers {match['skill']} (wanted by {alice.name})")
