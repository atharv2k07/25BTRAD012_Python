class Library:
    def __init__(self, book):
        self.book = book
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued")
        else:
            print("Book not available")

    def return_book(self):
        self.available = True
        print("Book returned")

    def display(self):
        print("Available:", self.available)

b = Library("Python")
b.issue()
b.display()
b.return_book()
b.display()