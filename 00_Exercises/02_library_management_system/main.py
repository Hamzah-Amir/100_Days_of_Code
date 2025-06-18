from dataclasses import dataclass, field

@dataclass
class Library:
    name: str = "Library" # You can also write your name while making instance by only defining datatype in class
    books: list = field(default_factory=lambda: ["Urdu","Islamiat", "English", "Math"])
    no_of_books: int = field(init=False)

    def __post_init__(self):
        self.no_of_books = len(self.books)

    def add_books(self, book_name): # Method of adding book
        # Adding new books in the library
        self.books.append(book_name.capitalize())
        print(f"{book_name} Book is added to your Library!")
    
    def remove_books(self, book_name):     
        if book_name in self.books:
            self.books.remove(book_name)
            print(f'{book_name} is removed from your Library.')
        elif book_name not in self.books:
            print("The book is not present in the Library.")
    
    def read_book(self,book_name):
        if book_name in self.books:
            print(f"Here you go, you can read {book_name} book in library")
        else:
            print("Book is not present in the Library")
    
    def lend_book(self,book_name='', days=''):
        
        if book_name in self.books:
            print(f'We are lending {book_name} book to you for {days} days.')
            print("Please return it in time.")
    
    def library_info(self): # CHecking the info of library
        print("DETAILS OF YOUR LIBRARY:")
        self.no_of_books = len(self.books)
        print(f"Total number of books in library is {self.no_of_books}.\nThe name of the books in library are:")
        for i in self.books:
            print(f'\"{i} Book\"')

while True: # Control flow of program
    try:
        start = input("Do you want to start the program (yes or no): ").lower() # Taking input if user want to exit or continue
    except Exception as e:
        print(e)

    if start == 'yes': # Handling if user wants to continue or start a program
        print("\n*****Checking library initial setup*****")
        library = Library()
        print(library)
        print(f"\n******{library.name.upper()}******")
    
        inp = input("Are you an admin of library or a member: ").lower() # Defining role of user in library

        if inp == 'admin': # Control flow for admin of a library
            library = Library(name=input("Enter Name Of Your Library: "))
            purpose = input("Do you want to add a book or remove a book from Library or view details(add,remove,info): ").lower()
            
            if purpose == 'add':
                try:
                    print("\nProcess of Adding New Book.")
                    book = input("Enter name of book you want to add in your library: ")
                    library.add_books(book)
                except Exception as e:
                    print(e)
            
            elif purpose == 'remove':
                print(f"\nProcessing removal of book from Library")
                try:
                    book = input(f"Enter name of these {library.books} book you want to remove from your Library: ").capitalize()
                    library.remove_books(book)
                except:
                    print("Please enter a Valid book name.")
    
            elif purpose == 'info':
                print("--------------------------")
                library.library_info()
            
            else:
                print("You entered invalid input please write (add,remove or info) only")

        elif inp == 'member': # CO\ontrol flow for member of a Library
            
            purpose = input("Do you want to read a book or lend a book from library: ").lower()
            
            if purpose == 'read':
                try:
                    book = input(f"Which book you want to read from {library.books}: ").capitalize()
                    library.read_book(book)
                except:
                    print(f"Sorry {book} is not present in library!")
                print("Thanks for visiting our library")
            
            elif purpose =='lend':
                try:
                    book = input(f'Which book you want to lend for home from {library.books}: ').capitalize()
                    days = int(input(f'For how many days you want to lend {book} book: '))
                    library.lend_book(book, days)
                    print("Thanks for visiting the library")
                except Exception as e:
                    print(e)
        
        else: # Handling invalid inputs
            print("You entered invalid input please enter (admin or member) only")
    
    elif start == 'no': # If user wants to exit the program control goes here
        print("Thanks for using my Library management system.")
        break
    else:
        print("You entered invalid input")
