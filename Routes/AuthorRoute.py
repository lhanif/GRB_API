from flask import Blueprint, jsonify, request
from Services.Services import get_authors_by_category_ser, delete_author_ser

authors_bp = Blueprint('authors', __name__)

@authors_bp.route('/api/authors/category/<string:category_name>', methods=['GET'])
def get_authors_by_category(category_name):
    authors, error_msg = get_authors_by_category_ser(category_name)
    if authors:
        authors_list = [{
            'Author_ID': author.Author_ID,
            'Author_Name': author.Author_Name,
            'Year_Born': author.Year_Born,
            'Year_Died': author.Year_Died
        } for author in authors]
        return jsonify({'authors': authors_list}), 200
    else:
        return jsonify({'message': 'Failed to get authors by category', 'error': error_msg}), 404

@authors_bp.route('/api/authors/<int:author_id>', methods=['DELETE'])
def delete_author(author_id):
    error_msg = delete_author_ser(author_id)
    if not error_msg:
        return jsonify({'message': 'Author deleted successfully'}), 200
    else:
        return jsonify({'message': 'Failed to delete author', 'error': error_msg}), 400
