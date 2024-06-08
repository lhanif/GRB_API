import psycopg2
from Models.Wishlist import Wishlist 

def db_conn():
    url = "postgresql://postgres:Luthfi14@localhost:5432/GRB_Store"
    return psycopg2.connect(url)

def get_wishlist_by_customer(customer_id):
    connection = None
    cursor = None
    try:
        connection = db_conn()
        cursor = connection.cursor()
        
        cursor.execute('''
            SELECT * FROM public."Wishlist" WHERE "Customer_ID" = %s
        ''', (customer_id,))
        data = cursor.fetchall()

        wishlist = [Wishlist(
            Wishlist_ID=wishlist[0],
            Level=wishlist[1],
            Customer_ID=wishlist[2],
            Book_ID=wishlist[3]
        ) for wishlist in data]
        
        return wishlist, None
    except Exception as e:
        return [], str(e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def add_wishlist(wishlist):
    connection = None
    cursor = None
    try:
        connection = db_conn()
        cursor = connection.cursor()
        
        cursor.execute('''
            INSERT INTO public."Wishlist" ("Level", "Customer_ID", "Book_ID")
            VALUES (%s, %s, %s)
            RETURNING "Wishlist_ID";
        ''', (wishlist.Level, wishlist.Customer_ID, wishlist.Book_ID))
        
        connection.commit()

        wishlist_id = cursor.fetchone()[0]

        return wishlist_id, None
    except Exception as e:
        return None, str(e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def delete_wishlist(wishlist_id):
    connection = None
    cursor = None
    try:
        connection = db_conn()
        cursor = connection.cursor()
        
        cursor.execute('''DELETE FROM public."Wishlist" WHERE "Wishlist_ID" = %s''', (wishlist_id,))
        
        connection.commit()

        return None
    except Exception as e:
        return str(e)
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
