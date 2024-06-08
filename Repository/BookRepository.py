import psycopg2
from Models.Book import Book  

def db_conn():
    url = "postgresql://postgres:Luthfi14@localhost:5432/GRB_Store"
    return psycopg2.connect(url)


def get_all_books():
    connection = None
    cursor = None
    try:
        connection = db_conn()
        cursor = connection.cursor()
        
        cursor.execute('''SELECT * FROM public."Book"''')
        data = cursor.fetchall()

        books = [Book(
            Book_ID=book[0],
            Book_Name=book[1],
            Publish_Year=book[2],
            Pages=book[3],
            Price=book[4],
            Language_ID=book[5],
            Publisher_ID=book[6]
        ) for book in data]
        
        return books, None
    except Exception as e:
        return [], str(e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def insert_book(book):
    connection = None
    cursor = None
    try:
        connection = db_conn()
        cursor = connection.cursor()
        
        cursor.execute('''
            INSERT INTO public."Book" ("Book_Name", "Publish_Year", "Pages", "Price", "Language_ID", "Publisher_ID")
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING "Book_ID";
        ''', (book.Book_Name, book.Publish_Year, book.Pages, book.Price, book.Language_ID, book.Publisher_ID))

        
        connection.commit()

        book_id = cursor.fetchone()[0]

        return book_id, None
    except Exception as e:
        return None, str(e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def update_book(book_id, updated_fields):
    connection = None
    cursor = None
    try:
        connection = db_conn()
        cursor = connection.cursor()
        
        fields_to_update = []
        for field, value in updated_fields.items():
            fields_to_update.append(f'"{field}" = %s')
        
        sql_query = f'''
            UPDATE public."Book"
            SET {', '.join(fields_to_update)}
            WHERE "Book_ID" = %s;
        '''
        
        values = list(updated_fields.values())
        values.append(book_id)
        
        cursor.execute(sql_query, values)
        
        connection.commit()

        return None
    except Exception as e:
        return str(e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def delete_book(book_id):
    connection = None
    cursor = None
    try:
        connection = db_conn()
        cursor = connection.cursor()
        
        cursor.execute('''
            DELETE FROM public."Book"
            WHERE "Book_ID" = %s;
        ''', (book_id,))
        
        connection.commit()

        return None
    except Exception as e:
        return str(e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
