class Wishlist:
    def __init__(self, Wishlist_ID, Level, Customer_ID, Book_ID):
        self.Wishlist_ID = Wishlist_ID
        self.Level = Level
        self.Customer_ID = Customer_ID
        self.Book_ID = Book_ID


    def to_dict(self):
        return {
            'Wishlist_ID': self.Wishlist_ID,
            'Level': self.Level,
            'Customer_ID': self.Customer_ID,
            'Book_ID': self.Book_ID,
        }
