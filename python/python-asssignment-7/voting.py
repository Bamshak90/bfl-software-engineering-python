"""
Voting System

Task:
- Implement a simple voting system.
- Store candidates in a dictionary { "candidate_name": vote_count }
- Allow voters (by ID) to vote only once.
- Use *args to register multiple candidates at once.
- Use **kwargs to update candidate details like party, region.


// NOT FOR THIS ASSIGNMENT
Future OOP Extension:
- Candidate as a class.
- Voter as a class with has_voted flag.
- Election as a manager class.
"""

candidates = {}
voters = set()

def register_candidate(name, party, region):
    """Register a single candidate with fixed details."""
    if name in candidates:
        return f"Candidate {name} already registered!"
    
    candidates[name] = {
        "votes": 0,
        "party": party,
        "region": region
    }
    return f"Candidate {name} registered successfully."


def cast_vote(voter_id, candidate_name):
    """Allow a voter to vote only once."""
    if voter_id in voters:
        return f"Voter {voter_id} has already voted!"
    
    if candidate_name not in candidates:
        return f"Candidate {candidate_name} not found!"
    
    voters.add(voter_id)
    candidates[candidate_name]["votes"] += 1
    return f"Vote casted for {candidate_name}."


def election_result():
    """Return winner and vote counts."""
    if not candidates:
        return "No candidates registered!"
    

    max_votes = 0
    for candidate_data in candidates.values():
        votes = candidate_data["votes"]
        if votes > max_votes:
            max_votes = votes

    winners = []
    for name, data in candidates.items():
        if data["votes"] == max_votes:
            winners.append(name)

    return {"winners": winners, "candidates": candidates}



print(register_candidate("Alice", "Independent", "North"))
print(register_candidate("Bob", "Independent", "North"))
print(register_candidate("Charlie", "Green", "West"))

print(cast_vote("V1", "Alice"))
print(cast_vote("V2", "Bob"))
print(cast_vote("V3", "Alice"))

print(election_result())
