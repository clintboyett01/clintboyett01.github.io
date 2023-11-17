from flask import Flask, request, jsonify

# Create a Flask application
app = Flask(__name__)

# Sample data (for demonstration)
data = {
    '1': {'name': 'John', 'age': 30},
    '2': {'name': 'Jane', 'age': 25},
    '3': {'name': 'Bob', 'age': 35},
}

# Define a route for the root endpoint
@app.route('/', methods=['GET'])
def hello_world():
    return "Hello, World!"

# Define a route to get a specific item by ID
@app.route('/items/<string:item_id>', methods=['GET'])
def get_item(item_id):
    if item_id in data:
        return jsonify(data[item_id])
    else:
        return jsonify({'error': 'Item not found'}), 404

# Define a route to create a new item
@app.route('/items', methods=['POST'])
def create_item():
    item_data = request.get_json()
    if 'name' in item_data and 'age' in item_data:
        new_id = str(len(data) + 1)
        data[new_id] = {
            'name': item_data['name'],
            'age': item_data['age']
        }
        return jsonify({'message': 'Item created', 'id': new_id}), 201
    else:
        return jsonify({'error': 'Invalid data'}), 400

if __name__ == '__main__':
    app.run(debug=True)
