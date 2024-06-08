from flask import Blueprint, jsonify, request
from Services.Services import get_wishlist_by_customer_ser, add_wishlist_ser, delete_wishlist_ser
from Models.Wishlist import Wishlist

wishlist_bp = Blueprint('wishlist', __name__)

@wishlist_bp.route('/api/wishlist/<int:customer_id>', methods=['GET'])
def get_wishlist(customer_id):
    wishlist, error_msg = get_wishlist_by_customer_ser(customer_id)

    if wishlist:
        wishlist_list = [{
            'Wishlist_ID': item.Wishlist_ID,
            'Level': item.Level,
            'Customer_ID': item.Customer_ID,
            'Book_ID': item.Book_ID
        } for item in wishlist]
        return jsonify({'wishlist': wishlist_list}), 200
    else:
        return jsonify({'message': 'Failed to get wishlist', 'error': error_msg}), 404

@wishlist_bp.route('/api/wishlist', methods=['POST'])
def add_wishlist_route():
    data = request.get_json()
    wishlist = Wishlist(
        Wishlist_ID=None,
        Level=data['Level'],
        Customer_ID=data['Customer_ID'],
        Book_ID=data['Book_ID']
    )
    wishlist_id, error_msg = add_wishlist_ser(wishlist)
    if wishlist_id:
        return jsonify({'message': 'Wishlist added successfully', 'Wishlist_ID': wishlist_id}), 201
    else:
        return jsonify({'message': 'Failed to add wishlist', 'error': error_msg}), 400

@wishlist_bp.route('/api/wishlist/<int:wishlist_id>', methods=['DELETE'])
def delete_wishlist_route(wishlist_id):
    error_msg = delete_wishlist_ser(wishlist_id)
    if not error_msg:
        return jsonify({'message': 'Wishlist deleted successfully'}), 200
    else:
        return jsonify({'message': 'Failed to delete wishlist', 'error': error_msg}), 400
