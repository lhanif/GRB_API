import psycopg2
from Models.Review import Reviews


def db_conn():
    url = "postgresql://postgres:Luthfi14@localhost:5432/GRB_Store"
    return psycopg2.connect(url)

def get_all_reviews():
    connection = None
    cursor = None
    try:
        connection = db_conn()
        cursor = connection.cursor()
        
        cursor.execute('''SELECT * FROM public."Reviews"''')
        data = cursor.fetchall()

        reviews = [Reviews(
            Reviews_ID=review[0],
            Customer_ID=review[1],
            Book_ID=review[2],
            Comments=review[3],
            Rate=review[4]
        ) for review in data]
        
        return reviews, None
    except Exception as e:
        return [], str(e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def add_review(review):
    connection = None
    cursor = None
    try:
        connection = db_conn()
        cursor = connection.cursor()
        
        cursor.execute('''
            INSERT INTO public."Reviews" ("Customer_ID", "Book_ID", "Comments", "Rate")
            VALUES (%s, %s, %s, %s)
            RETURNING "Reviews_ID";
        ''', (review.Customer_ID, review.Book_ID, review.Comments, review.Rate))
        
        connection.commit()

        reviews_id = cursor.fetchone()[0]

        return reviews_id, None
    except Exception as e:
        return None, str(e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
