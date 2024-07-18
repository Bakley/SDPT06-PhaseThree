import logging
from functools import wraps
import hashlib
import os
import base64

# Setup logging
logging.basicConfig(level=logging.INFO)

# User Roles
class UserRole:
    ADMIN = "admin"     # class attribute
    USER  = "Regular"

# Decorators
def authenticate_user(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.auth_manager.logged_in_user:
            return func(self, *args, **kwargs)
        else:
            logging.warning("Authentication required.")
            return None
    return wrapper

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Action '{func.__name__}' initiated.")
        result = func(*args, **kwargs)
        logging.info(f"Action '{func.__name__}' completed.")
        return result
    return wrapper

def check_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            if self.auth_manager.logged_in_user_role == role or self.auth_manager.logged_in_user_role == UserRole.ADMIN:
                return func(self, *args, **kwargs)
            else:
                logging.warning(f"Permission denied.")
                return None
        return wrapper
    return decorator

# User manager
class AuthenticationManager:
    def __init__(self):
        self.logged_in_user = None
        self.logged_in_user_role = None

    @log_action
    def login(self, username, password):
        if username in UserManager.users and UserManager.users[username]["password"] == password:
            self.logged_in_user = username
            self.logged_in_user_role = UserManager.users[username]["role"]
            logging.info(f"User '{username}' logged in with role '{self.logged_in_user_role}'.")
            return True
        else:
            logging.warning("Invalid username or password.")
            return False
        

    @log_action
    def logout(self):
        if self.logged_in_user:
            logging.info(f"User '{self.logged_in_user}' logged out.")
            self.logged_in_user = None
            self.logged_in_user_role = None
        else:
            logging.warning("No user is currently logged in.")

class UserManager:

    # def __init__(self, auth_manager) -> None:
    #     self.auth_manager =  auth_manager
    users = {
        "admin": {
            "password": "adminpass",
            "role": UserRole.ADMIN
        },
        "user_wan": {
            "password": "regularpass",
            "role": UserRole.USER
        },
    }

    @classmethod
    @log_action
    # @check_role(UserRole.ADMIN)
    def register_user(cls, auth_manager, username, password, role):
        if username not in cls.users:
            cls.users[username] = {
                "password": password,
                "role": role
            }
            logging.info(f"User '{username}' registered with role '{role}'.")
        else:
            logging.warning(f"Username '{username}' already exists.")
        
# Candidate Management
class CandidateManager:
    def __init__(self, auth_manager):
        self.candidates = []
        self.auth_manager = auth_manager

    @check_role(UserRole.ADMIN)
    def add_candidate(self, candidate_name):
        if candidate_name not in self.candidates:
            self.candidates.append(candidate_name)
            logging.info(f"Candidate '{candidate_name}' added.")
        else:
            logging.warning(f"Candidate '{candidate_name}' already exists.")

    @log_action
    @check_role(UserRole.ADMIN)
    def remove_candidate(self, candidate_name):
        if candidate_name in self.candidates:
            self.candidates.remove(candidate_name)
            logging.info(f"Candidate '{candidate_name}' removed.")
        else:
            logging.warning(f"Candidate '{candidate_name}' not found.")

    def list_candidates(self):
        logging.info("Candidate List:")
        for candidate in self.candidates:
            logging.info(f"- {candidate}")

# Voter Management
class VoterManager:
    def __init__(self, auth_manager):
        self.voters = {}
        self.auth_manager = auth_manager

    @log_action
    @check_role(UserRole.ADMIN)
    def register_voter(self, voter_id, name):
        if voter_id not in self.voters:
            self.voters[voter_id] = Voter(name, voter_id)
            logging.info(f"Voter '{name}' registered with ID {voter_id}.")
        else:
            logging.warning(f"Voter with ID {voter_id} already registered.")

    @log_action
    @check_role(UserRole.ADMIN)
    def remove_voter(self, voter_id):
        if voter_id in self.voters:
            del self.voters[voter_id]
            logging.info(f"Voter with ID {voter_id} removed.")
        else:
            logging.warning(f"Voter with ID {voter_id} not found.")

class Voter:
    def __init__(self, name, voter_id):
        self.name = name
        self._voter_id = voter_id
        self._has_voted = False
        self._vote = None

    @property
    def has_voted(self):
        return self._has_voted

    @has_voted.setter
    def has_voted(self, value):
        if not isinstance(value, bool):
            raise ValueError("has_voted must be a boolean")
        self._has_voted = value

    @property
    def vote(self):
        return self._vote

    @vote.setter
    def vote(self, candidate_name):
        if self._has_voted:
            raise ValueError("Voter has already voted")
        
        self._vote = VotingSystem.encrypt_data(candidate_name)
        self._has_voted = True

# Voting Operations
class VotingAlgorithm:
    def __init__(self):
        self.votes = {}

    def cast_vote(self, voter_id, candidate_name):
        self.votes[voter_id] = candidate_name

    def has_voted(self, voter_id):
        return voter_id in self.votes
    
class VotingSystem:
    total_votes = 0

    def __init__(self):
        self.auth_manager = AuthenticationManager()

        self.candidate_manager = CandidateManager(self.auth_manager)
        self.voter_manager = VoterManager(self.auth_manager)
        self.voting_algorithm = VotingAlgorithm()

    @log_action
    @check_role(UserRole.USER)
    def vote(self, voter_id, candidate_name):
        if voter_id in self.voter_manager.voters:
            voter = self.voter_manager.voters[voter_id]
            if candidate_name in self.candidate_manager.candidates:
                if not voter.has_voted:
                    voter.vote = candidate_name
                    self.voting_algorithm.cast_vote(voter_id, voter.vote)
                    VotingSystem.total_votes += 1
                    logging.info(f"Voter '{voter.name}' voted for '{candidate_name}'.")
                else:
                    logging.warning(f"Voter '{voter.name}' has already voted.")
            else:
                logging.warning(f"Candidate '{candidate_name}' not found.")
        else:
            logging.warning(f"Invalid voter ID '{voter_id}'.")

    @classmethod
    def get_total_votes(cls):
        return cls.total_votes

    @staticmethod
    def greet():
        print("Welcome to the Voting System")

    @staticmethod
    def validate_voter_id(voter_id):
        if isinstance(voter_id, str) and 3 <= len(voter_id) <= 6 and voter_id.isalnum():
            return True
        logging.warning("Invalid voter ID.")
        return False

    @staticmethod
    def validate_candidate_name(candidate_name):
        if isinstance(candidate_name, str) and 2 <= len(candidate_name) <= 50 and candidate_name.isalpha():
            return True
        logging.warning("Invalid candidate name.")
        return False

    @staticmethod
    def encrypt_data(data):
        encrypted_data = base64.b64encode(data.encode()).decode()
        return encrypted_data

    @staticmethod
    def decrypt_data(encrypted_data):
        decrypted_data = base64.b64decode(encrypted_data.encode()).decode()
        return decrypted_data

    @log_action
    @check_role(UserRole.ADMIN)
    def generate_winner(self):
        vote_count = {}
        for candidate in self.candidate_manager.candidates:
            vote_count[candidate] = 0
        
        for vote in self.voting_algorithm.votes.values():
            decrypted_vote = self.decrypt_data(vote)
            if decrypted_vote in vote_count:
                vote_count[decrypted_vote] += 1
        
        if vote_count:
            winner = max(vote_count, key=vote_count.get)
            logging.info(f"The winner is '{winner}' with {vote_count[winner]} votes. Runnaway {vote_count}")
            return winner
        else:
            logging.warning("No votes have been cast yet.")
            return None

# CLI Interface
def main():
    voting_system = VotingSystem()
    # import pdb
    # pdb.set_trace()

    while True:
        print("\nWelcome to Voting System CLI")
        print("1. Login")
        print("2. Logout")
        print("3. Register User (Admin Only)")
        print("4. Add Candidate (Admin Only)")
        print("5. Remove Candidate (Admin Only)")
        print("6. Register Voter (Admin Only)")
        print("7. Remove Voter (Admin Only)")
        print("8. Vote")
        print("9. Show Total Votes")
        print("10. List Candidates")
        print("11. Generate Winner (Admin Only)")
        print("12. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            voting_system.auth_manager.login(username, password)
        elif choice == "2":
            voting_system.auth_manager.logout()
        elif choice == "3":
            if voting_system.auth_manager.logged_in_user_role == UserRole.ADMIN:
                username = input("New username: ")
                password = input("New password: ")
                role = input("Role (admin/user): ")
                UserManager.register_user(voting_system.auth_manager, username, password, role)
        elif choice == "4":
            voting_system.candidate_manager.add_candidate(input("Candidate name: "))
        elif choice == "5":
            voting_system.candidate_manager.remove_candidate(input("Candidate name: "))
        elif choice == "6":
            voting_system.voter_manager.register_voter(input("Voter ID: "), input("Name: "))
        elif choice == "7":
            voting_system.voter_manager.remove_voter(input("Voter ID: "))
        elif choice == "8":
            voter_id = input("Enter your voter ID: ")
            candidate_name = input("Enter candidate name: ")
            if VotingSystem.validate_voter_id(voter_id) and VotingSystem.validate_candidate_name(candidate_name):
                voting_system.vote(voter_id, candidate_name)
        elif choice == "9":
            total_votes = VotingSystem.get_total_votes()
            logging.info(f"Total votes cast: {total_votes}")
        elif choice == "10":
            voting_system.candidate_manager.list_candidates()
        elif choice == "11":
            voting_system.generate_winner()
        elif choice == "12":
            break
        else:
            logging.warning("Invalid choice. Please try again.")

if __name__ == "__main__":
    VotingSystem.greet()
    main()
