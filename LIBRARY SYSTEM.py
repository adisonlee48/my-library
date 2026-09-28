class book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
        self.borrower_name = ""
        self.condition = True

class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
    def remove_book(self,title_to_remove):
        for book in self.books:
            if book.title == title_to_remove:
                self.books.remove(book)
                break
    def display_books(self):
        for book in self.books:
            print(f"{book.title} by {book.author}")
    def search_book(self,search_title,):
        for book in self.books:
            if book.title == search_title:
                return book
        return None
    def count_book(self):
        total_books = len(self.books)
        return total_books

admin_id = "12345678"
admin_password = "12345678"
librarian_id = "01234567"
librarian_password = "01234567"
student_id = "abcdefg"
student_password = "abcdefg"
library = Library()

while True:
    user_id = input("User ID(or type exit to shut down): ")
    if user_id == "exit":
        print("Shutting down the library system. Goodbye!")
        break
    
    elif user_id == admin_id:
        user_password = input("Password: ")

        if user_password == admin_password:
            print("Welcome, JC(Admin)\n")
            while True:
                print("1: Add_Book\n2: Search_Book\n3: Display_Book\n4: Count_Books\n5: Logout")
                service = input("Which Services do you need?\n")
                if service == "1":
                    library.add_book(book(input("BOOK's Title:\n"),input("BOOK's Author\n")))
                elif service == "2":
                    search_title = input("What is the Title of the book you looking for?\n")
                    is_found = library.search_book(search_title)
                    if is_found: 
                        print(f"This book had been borrowed? {is_found.is_borrowed}")
                        if is_found.is_borrowed:
                            print(f"Borrowed by {is_found.borrower_name}")
                        if is_found.condition == True:
                            print("This book is in good condition")
                        elif is_found.condition == False:
                            print("This book is reported Damaged or Lost")
                
                        service_2 = input("1: Remove this Book\n2: Report Lost/Damage\n3: Back\n")
                        if service_2 == "1":
                            Remove = input("Do you want to Remove this book? (Y/N)\n")
                            if Remove.upper() == "Y":
                                library.remove_book(search_title)
                                print("Removed successfully\n")
                            else:
                                print("Thank You\n")
                        elif service_2 == "2":
                            DamageorLost = input("Do you want to set this book as damaged or lost? (Y/N)\n")
                            if DamageorLost == "Y":
                                is_found.condition = False
                        elif service_2 == "3":
                            pass
                        else:
                            print("Please Enter 1/2/3 Only")
                    else:
                        print("This book is currently unavailable\n")
                elif service == "3":
                    library.display_books()

                elif service == "4":
                    total = library.count_book()
                    print(f"The Total Number of Books is {total}\n")
                elif service == "5":
                    break


        else:
            print("Password Incorrect! Please Try Again")

    elif user_id == librarian_id:
        user_password = input("Password: ")

        if user_password == librarian_password:
            print("Welcome, Librarian\n")
            while True:
                print("1: Add_Book\n2: Search_Book\n3: Display_Book\n4: Count_Books\n5: Logout\n")
                service = input("Which Services do you need?\n")
                if service == "1":
                    library.add_book(book(input("BOOK's Title:\n"),input("BOOK's Author\n")))
        
                elif service == "2":
                    search_title = input("What is the Title of the book you looking for?\n")
                    is_found = library.search_book(search_title)
                    if is_found: 
                        print(f"This book had been borrowed? {is_found.is_borrowed}")
                        if is_found.is_borrowed:
                            print(f"Borrowed by {is_found.borrower_name}")
                        if is_found.condition == True:
                            print("This book is in good condition")
                        elif is_found.condition == False:
                            print("This book is reported Damaged or Lost")
                    
                        service_2 = input("1: Remove this Book\n2: Report Lost/Damage\n3: Back\n")
                        if service_2 == "1":
                            Remove = input("Do you want to Remove this book? (Y/N)\n")
                            if Remove == "Y":
                                library.remove_book(search_title)
                                print("Removed successfully\n")
                            else:
                                print("Thank You\n")
                        elif service_2 == "2":
                            DamageorLost = input("Do you want to set this book as damaged or lost? (Y/N)\n")
                            if DamageorLost.upper() == "Y":
                                is_found.condition = False
                        elif service_2 == "3":
                            pass
                        else:
                            print("Please Enter 1/2/3 Only")
                    else:
                        print("This book is currently unavailable\n")
                elif service == "3":
                    library.display_books()
        
                elif service == "4":
                    total = library.count_book()
                    print(f"The Total Number of Books is {total}\n")
                elif service == "5":
                    break
        else:
            print("Password Incorrect! Please Try Again")

    elif user_id == student_id:
        user_password = input("Password: ")

        if user_password == student_password:
            Student_name = input("What is Your Name:\n")
            print(f"Welcome, {Student_name}\n")
        
            while True:
                print("Hi Welcome to JC Library System.\n")
                print("1: Return Book\n2: Search Book\n3: Display Book\n4: Count Books\n5: Exit")
                service = input("Please Choose Your Services:\n")
                if service == "1":
                    search_title = input("What is the Title of the book you are returning?\n")
                    is_found = library.search_book(search_title)
                    if is_found:
                        is_found.is_borrowed = False
                        is_found.borrower_name = ""
                        print("Book returned successfully!\n")
                    else:
                        print("This book does not belong to our library.\n")

                elif service == "2":
                    search_title = input("What is the Title of the book you looking for?\n")
                    is_found = library.search_book(search_title)
                    if is_found:  
                        if is_found.is_borrowed:
                            print("Sorry, this book is currently borrowed by someone else.\n")
                        elif is_found.condition == False:
                            print("Sorry, this book is damaged or lost and cannot be borrowed.\n")
                        else:
                            Borrow = input("Do you want to borrow this book? (Y/N)\n")
                            if Borrow == "Y":
                                is_found.is_borrowed = True
                                is_found.borrower_name = Student_name
                                print("You borrow the book successfully\n")
                            else:
                                print("Thank You\n")
                    else:
                        print("This book is currently unavailable\n")

                elif service == "3":
                    library.display_books()


                elif service == "4":
                    total = library.count_book()
                    print(f"The Total Number of Books is {total}\n")

                elif service == "5":
                    break

                else:
                    print("Please Enter Number 1-5 Only\n")
        else:
            print("Password Incorrect! Please Try Again")
    else:
        print("User ID not found. Please Try Again!\n")

        
               



