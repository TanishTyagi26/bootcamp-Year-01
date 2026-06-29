#               =================  Library Book Manager ======================

# Build a Book class with_isbn (private, set once in init), _title, _author (protected), and_copies (private). Implement checkout(n) and return_book(n) methods. Raise ValueError for invalid operations. Add a @property available that returns current copies.

# (Hint: ISBN should have no setter; copies must never go below 0 .)



class Book:

    def __init__(self, isbn, title, author, copies):
        self.__isbn = isbn
        self._title = title
        self._author = author
        self.__copies = copies

    def checkout(self, n):
        if n <= 0:
            raise ValueError("Invalid Input...")

        if n > self.__copies:
            raise ValueError("Not enough copies available...")

        self.__copies -= n
        print(f"{self.__copies} books are left")

    def return_book(self, n):
        if n <= 0:
            raise ValueError("Invalid Input...")

        self.__copies += n
        print(f"{n} books are returned")
        print(f"Total Count of the Books is : {self.__copies}")

    @property
    def available(self):
        return f"{self.__copies} : is the total count of the copies"


book1 = Book(123456, "Ramayana", "Valmiki", 10)

book1.checkout(2)
book1.return_book(5)

print(book1.available)




        

