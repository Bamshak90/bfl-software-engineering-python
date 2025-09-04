"""
TASK: Create a VotingSystem class.

Requirements:
1. The class should allow registering candidates.
2. Each candidate should start with 0 votes.
3. The class should allow voters (using voter IDs) to cast votes.
   - Ensure one voter cannot vote more than once.
4. Provide a method to display election results.

Example Usage:
    election = VotingSystem()
    election.register_candidate("Alice")
    election.register_candidate("Bob")
    election.vote("Voter1", "Alice")
    election.vote("Voter2", "Bob")
    election.vote("Voter3", "Alice")
    print(election.results())  # {"Alice": 2, "Bob": 1}
    print(election.winner()) # Alice    
"""

class VoteSystem:
    def __init__(self):
        self.candidates = {}
        self.voters = set()

    def register_candidates(self, name):
        if name in self.candidates:
            print(f"{name} already exists")
        else:
            self.candidates[name] = 0
            print(f"{name} has been registered successfully")

    def cast_vote(self, voter_Id, name):
        if voter_Id in self.voters:
            print(f"Candidate has already voted")
            return
        if name in self.candidates:
            self.candidates[name] += 1
            self.voters.add(voter_Id)
            print(f"{name} has gotten a vote from {voter_Id}")
        else:
            print(f"{name} does not exist as a candidate")

    def display_votes(self):
        for name, votes in self.candidates.items():
            print(f"{name}: {votes}")

    def winner(self):
        if not self.candidates:
            return None

        winning_votes = 0
        winner_name = None

        for name, votes in self.candidates.items():
            if votes > winning_votes:
                winning_votes = votes
                winner_name = name

        if winning_votes == 0:
            return None
        return winner_name


 

election = VoteSystem()
election.register_candidates("Alice")
election.register_candidates("Bob")

election.cast_vote("Voter1", "Alice")
election.cast_vote("Voter2", "Bob")
election.cast_vote("Voter3", "Alice")

election.display_votes()
print("Winner:", election.winner())
