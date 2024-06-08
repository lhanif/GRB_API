from flask import Flask
from Routes.BookRoute import books_bp
from Routes.AuthorRoute import authors_bp
from Routes.ReviewRoute import reviews_bp
from Routes.WishlistRoute import wishlist_bp
app = Flask(__name__)
app.register_blueprint(books_bp)
app.register_blueprint(authors_bp)
app.register_blueprint(reviews_bp)
app.register_blueprint(wishlist_bp)

if __name__ == '__main__':
    app.run(debug=True)