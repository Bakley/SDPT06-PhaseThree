# Intro to OOP
# OOP Syntax
# Creating variables && assign data
# Naming conventions [language used/jargon]
# Class attribute and class methods

class Voter:
    # class definition
    def __init__(self, name, voter_id):
        """
        Initialize the state of an objects
        Assign value to data members
        """
        self.name = name
        self.voter_id = voter_id
        self.has_voted = False #instance variable/attribute

    def showing_self(self):
        return self
    
    def convert_to_dictionary(self):
        return {
            "name": self.name,
            "voter_id": self.voter_id,
            "has_voted": self.has_voted
        }
    
    def cast_vote(self, candidate_name, voting_system):
        if not self.has_voted:
            voting_system.receive_vote(candidate_name)
            self.has_voted = True
        else:
            print(f"{self.name} has already voted!")

class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def receive_vote(self):
        self.votes += 1

    def __str__(self) -> str:
        return f"Candidate {self.name}: {self.votes} votes"

class VotingSystem:
    def __init__(self):
        self.candidates = {}
        self.voters = {}

    def add_candidate(self, candidate):
        if candidate.name.strip():
            if candidate.name not in self.candidates:
                self.candidates[candidate.name] = candidate
                print(f"{candidate.name} added as a candidate!")
            else:
                print(f"Warning: {candidate.name} already exists!")
        else:
            print("Error: Candidate name cannot be blank")

    def register_voter(self, voter):
        if voter.name.strip():
            if voter.name not in self.voters:
                self.voters[voter.voter_id] = voter
                print(f"{voter.name} added as a candidate!")
            else:
                print(f"Warning: {voter.name} already exists!")
        else:
            print("Error: Voter name cannot be blank")

    def receive_vote(self, candidate_name):
        if candidate_name in self.candidates:
            self.candidates[candidate_name].receive_vote()
        else:
            print("No Candidate!")

    def announce_winner(self):
        winner = max(self.candidates.values(), key=lambda candidate: candidate.votes)
        print(f"The winner is {winner.name}")

def display_menu():
    print("\nMenu:")
    print("1. Add Candidate")
    print("2. Register Voter")

    print("5. Cast Vote")
    print("6. Announce Winner")
    print("7. Exit")

if __name__ == "__main__":
    voting_system = VotingSystem()

    while True:
        display_menu()
        user_choice = input("\nEnter your option: ")

        if user_choice == "1":
            candidate_name = input("Enter candidate name: ")
            candidate = Candidate(candidate_name)
            voting_system.add_candidate(candidate)
        
        elif user_choice == "2":
            voter_name = input("Enter voter name: ")
            voter_id = input("Enter voter ID: ")
            voter = Voter(voter_name, voter_id)
            voting_system.register_voter(voter)


        elif user_choice == "5":
            voter_id = input("Enter your voter ID: ")
            if voter_id in voting_system.voters:
                candidate_name = input("Enter candidate name you want to vote for: ")
                voting_system.voters[voter_id].cast_vote(candidate_name, voting_system)
            else:
                print("Error: Invalid voter ID. Please register first.")

        elif user_choice == "6":
            voting_system.announce_winner()

        elif user_choice == "7":
            print("Exiting the voting app.")
            break

        else:
            print("Invalid choice!")
