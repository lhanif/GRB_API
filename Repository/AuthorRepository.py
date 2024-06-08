import psycopg2
from Models.Author import Author  

def db_conn():
    url = "postgresql://postgres:Luthfi14@localhost:5432/GRB_Store"
    return psycopg2.connect(url)

def get_authors_by_category(category_name):
    connection = None
    cursor = None
    try:
        connection = db_conn()
        cursor = connection.cursor()
        
        cursor.execute('''
            SELECT a.*
            FROM public."Author" a
            INNER JOIN public."Book_Author" ba ON a."Author_ID" = ba."Author_ID"
            INNER JOIN public."Book" b ON ba."Book_ID" = b."Book_ID"
            INNER JOIN public."Book_Category" bc ON b."Book_ID" = bc."Book_ID"
            INNER JOIN public."Category" c ON bc."Category_ID" = c."Category_ID"
            WHERE c."Category_Name" = %s
        ''', (category_name,))
        
        data = cursor.fetchall()

        authors = [Author(
            Author_ID=author[0],
            Author_Name=author[1],
            Year_Born=author[2],
            Year_Died=author[3]
        ) for author in data]
        
        return authors, None
    except Exception as e:
        return [], str(e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def delete_author(author_id):
    connection = None
    cursor = None
    try:
        connection = db_conn()
        cursor = connection.cursor()

        cursor.execute('''
            DELETE FROM public."Book_Author" WHERE "Author_ID" = %s
        ''', (author_id,))

        cursor.execute('''
            DELETE FROM public."Author" WHERE "Author_ID" = %s
        ''', (author_id,))

        connection.commit()

        return None
    except Exception as e:
        return str(e)
    finally:
        
        if cursor:
            cursor.close()
        if connection:
            connection.close()

