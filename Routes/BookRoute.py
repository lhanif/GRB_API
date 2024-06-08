from flask import Blueprint, jsonify, request
from Models.Book import Book
from Services.Services import get_all_books_ser, insert_book_ser, delete_book_ser, partial_update_book_ser

books_bp = Blueprint('books', __name__)

@books_bp.route('/api/books', methods=['GET'])
def get_books():
    books, error_msg = get_all_books_ser()

    if books:
        books_list = [{
            'Book_ID': book.Book_ID,
            'Book_Name': book.Book_Name,
            'Publish_Year': book.Publish_Year,
            'Pages': book.Pages,
            'Price': book.Price,
            'Language_ID': book.Language_ID,
            'Publisher_ID': book.Publisher_ID
        } for book in books]
        return jsonify({'books': books_list}), 200
    else: 
        return jsonify({'message': 'Failed to get books', 'error': error_msg}), 404
    
@books_bp.route('/api/books', methods=['POST'])
def add_book():
    data = request.get_json()
    print("Received data:", data)
    book = Book(
        Book_Name=data['Book_Name'],
        Publish_Year=data['Publish_Year'],
        Pages=data['Pages'],
        Price=data['Price'],
        Language_ID=data['Language_ID'],
        Publisher_ID=data['Publisher_ID']
    )
    book_id, error_msg = insert_book_ser(book)
    if book_id:
        return jsonify({'message': 'Book added successfully', 'Book_ID': book_id}), 201
    else:
        return jsonify({'message': 'Failed to add book', 'error': error_msg}), 400

@books_bp.route('/api/books/<int:book_id>', methods=['PATCH'])
def update_book(book_id):
    data = request.get_json()
    updated_fields = {}
    
    # Mengambil data yang dikirimkan dan menambahkannya ke updated_fields
    if 'Book_Name' in data:
        updated_fields['Book_Name'] = data['Book_Name']
    if 'Publish_Year' in data:
        updated_fields['Publish_Year'] = data['Publish_Year']
    if 'Pages' in data:
        updated_fields['Pages'] = data['Pages']
    if 'Price' in data:
        updated_fields['Price'] = data['Price']
    if 'Language_ID' in data:
        updated_fields['Language_ID'] = data['Language_ID']
    if 'Publisher_ID' in data:
        updated_fields['Publisher_ID'] = data['Publisher_ID']
    
    # Periksa apakah ada data yang dikirimkan untuk diperbarui
    if not updated_fields:
        return jsonify({'message': 'No fields to update'}), 400
    
    # Panggil fungsi untuk melakukan pembaharuan sebagian pada buku
    error_msg = partial_update_book_ser(book_id, updated_fields)
    
    # Periksa apakah ada kesalahan saat melakukan pembaharuan
    if not error_msg:
        return jsonify({'message': 'Book updated successfully'}), 200
    else:
        return jsonify({'message': 'Failed to update book', 'error': error_msg}), 400

@books_bp.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    error_msg = delete_book_ser(book_id)
    if not error_msg:
        return jsonify({'message': 'Book deleted successfully'}), 200
    else:
        return jsonify({'message': 'Failed to delete book', 'error': error_msg}), 400
