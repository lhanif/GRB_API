from flask import Blueprint, jsonify, request
from Models.Review import Reviews  
from Services.Services import get_all_reviews_ser, add_review_ser

reviews_bp = Blueprint('reviews', __name__)

@reviews_bp.route('/api/reviews', methods=['GET'])
def get_reviews():
    reviews, error_msg = get_all_reviews_ser()

    if reviews:
        reviews_list = [review.to_dict() for review in reviews]
        return jsonify({'reviews': reviews_list}), 200
    else: 
        return jsonify({'message': 'Failed to get reviews', 'error': error_msg}), 404

@reviews_bp.route('/api/reviews', methods=['POST'])
def add_review():
    data = request.get_json()
    review = Reviews(
        Reviews_ID=None,  
        Customer_ID=data['Customer_ID'],
        Book_ID=data['Book_ID'],
        Comments=data['Comments'],
        Rate=data['Rate']
    )
    reviews_id, error_msg = add_review_ser(review)
    if reviews_id:
        return jsonify({'message': 'Review added successfully', 'Reviews_ID': reviews_id}), 201
    else:
        return jsonify({'message': 'Failed to add review', 'error': error_msg}), 400
