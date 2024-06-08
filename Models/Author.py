class Author:
    def __init__(self, Author_ID, Author_Name, Year_Born, Year_Died):
        self.Author_ID = Author_ID
        self.Author_Name = Author_Name
        self.Year_Born = Year_Born
        self.Year_Died = Year_Died

    def to_dict(self):
        return {
            'Author_ID': self.Author_ID,
            'Author_Name': self.Author_Name,
            'Year_Born': self.Year_Born,
            'Year_Died': self.Year_Died
        }
