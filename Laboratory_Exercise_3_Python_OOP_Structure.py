class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.publication_year = year
        self.is_available = True 

    def display_info(self):
        status = "Available" if self.is_available else "Unavailable (Borrowed)"
        print(f"\nTitle: {self.title} | Author: {self.author} | Status: {status}")

    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print(f"Success! You have borrowed '{self.title}'.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        self.is_available = True
        print(f"Success! You have returned '{self.title}'.")

# --- Main Program ---

def main():
    # We create an empty list (our bookshelf)
    library = [] 
    
    print("=== Library Book Management System (Multi-Book) ===")

    while True:
        print("\nMAIN MENU:")
        print("1. Add New Book")
        print("2. Borrow Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        # --- OPTION 1: ADD BOOK ---
        if choice == '1':
            t = input("Enter Book Title: ")
            a = input("Enter Author Name: ")
            y = input("Enter Publication Year: ")
            
            new_book = Book(t, a, y)
            library.append(new_book)  # <--- This adds it to the list!
            print(f"'{t}' added to library.")

        # --- OPTION 2: BORROW BOOK ---
        elif choice == '2':
            if not library:
                print("No books in library.")
                continue
                
            search_title = input("Enter the title of the book to borrow: ")
            found = False
            for book in library:
                if book.title.lower() == search_title.lower():
                    book.borrow_book()
                    found = True
                    break # Stop searching once found
            
            if not found:
                print("Book not found.")

        # --- OPTION 3: RETURN BOOK ---
        elif choice == '3':
            if not library:
                print("No books in library.")
                continue

            search_title = input("Enter the title of the book to return: ")
            found = False
            for book in library:
                if book.title.lower() == search_title.lower():
                    book.return_book()
                    found = True
                    break 
            
            if not found:
                print("Book not found.")

        # --- OPTION 4: VIEW ALL ---
        elif choice == '4':
            if not library:
                print("The library is empty.")
            else:
                print(f"\n--- List of Books ({len(library)} total) ---")
                for book in library:
                    book.display_info()
                print("-----------------------------------")
        
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()