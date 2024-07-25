from colorama import Fore
from utils import colorize_output

from models.author import Author
from models.book import Book
from seed import seed_data

def create_tables():
        Author.create_table()
        Book.create_table()

@colorize_output(Fore.GREEN)
def add_author(name, birth_date):
        name = input("Enter author name: ")
        birth_date = input("Enter author birth date (YYYY-MM-DD): ")

        author = Author(name=name, birth_date=birth_date)
        author.save()
        print(f"Author '{name}' added successfully.")

def list_author():
        auth = Author.all()
        for user in auth:
                print(f"ID: {user[0]}, Name: {user[1]}")



def main():
        create_tables()
        seed_data()

        while True:
                
            print("\nLibrary Management CLI")
            print("1. Create Author")
            print("2. Read Author")
            print("3. Update Author")
            print("4. Delete Author")
            print("5. List Authors")
            print("6. Exit")


            
            choice = input("Enter your choice: ")

            if choice == "1":
                   add_author()
            elif choice == "5":
                   list_author()
            elif choice == '6':
                   break
            else:
                   print(Fore.YELLOW, "Invalid Choice. Kindly try again.")
                   
if __name__ == "__main__":
        main()
