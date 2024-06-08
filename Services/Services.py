from Repository.BookRepository import get_all_books, insert_book, delete_book, update_book
from Repository.AuthorRepository import get_authors_by_category, delete_author
from Repository.ReviewRepository import get_all_reviews, add_review
from Repository.WishlistRepository import get_wishlist_by_customer, add_wishlist, delete_wishlist
def get_all_books_ser():
    return get_all_books()

def insert_book_ser(book):
    return insert_book(book)

def delete_book_ser(book):
    return delete_book(book)

def partial_update_book_ser(book_id, updated_fields):
    error_msg = None
    try:
        error_msg = update_book(book_id, updated_fields)
    except Exception as e:
        error_msg = str(e)
    return error_msg

def get_authors_by_category_ser(category_name):
    return get_authors_by_category(category_name)

def delete_author_ser(author_id):
    return delete_author(author_id)

def get_all_reviews_ser():
    return get_all_reviews()

def add_review_ser(review):
    return add_review(review)

def get_wishlist_by_customer_ser(customer_id):
    return get_wishlist_by_customer(customer_id)

def add_wishlist_ser(wishlist):
    return add_wishlist(wishlist)

def delete_wishlist_ser(wishlist_id):
    return delete_wishlist(wishlist_id)