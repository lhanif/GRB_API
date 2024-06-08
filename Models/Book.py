class Book:
    def __init__(self, Book_Name, Publish_Year, Pages, Price, Language_ID, Publisher_ID, Book_ID=None):
        self.Book_ID = Book_ID
        self.Book_Name = Book_Name
        self.Publish_Year = Publish_Year
        self.Pages = Pages
        self.Price = Price
        self.Language_ID = Language_ID
        self.Publisher_ID = Publisher_ID

    def to_dict(self):
        return {
            'Book_ID': self.Book_ID,
            'Book_Name': self.Book_Name,
            'Publish_Year': self.Publish_Year,
            'Pages': self.Pages,
            'Price': self.Price,
            'Language_ID': self.Language_ID,
            'Publisher_ID': self.Publisher_ID
        }
