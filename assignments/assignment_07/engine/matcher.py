def find_matches(current_user, other_user):
    matches = []
    for other in other_user:
        if other == current_user:
            continue
        for wanted in current_user.skills_wanted:
            for offer in current_user.skills_offered:
                if wanted.name.lower() == offer.name.lower():
                    matches.append({
                        "match_with": other.name,
                        "skill": offer.name
                    })

    return matches