class Reviews:
    def __init__(self, Customer_ID, Book_ID, Comments, Rate, Reviews_ID=None):
        self.Reviews_ID = Reviews_ID
        self.Customer_ID = Customer_ID
        self.Book_ID = Book_ID
        self.Comments = Comments
        self.Rate = Rate

    def to_dict(self):
        return {
            'Reviews_ID': self.Reviews_ID,
            'Customer_ID': self.Customer_ID,
            'Book_ID': self.Book_ID,
            'Comments': self.Comments,
            'Rate': self.Rate
        }
