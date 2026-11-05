
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data stored in memory
sample_data = [
    {"id": 1, "name": "Python", "category": "Programming"},
    {"id": 2, "name": "Flask", "category": "Framework"},
    {"id": 3, "name": "GitHub", "category": "Version Control"}
]


# GET endpoint: welcome message
@app.route("/hello", methods=["GET"])
def hello():
    return jsonify({
        "message": "Welcome to my Flask API!"
    }), 200


# GET and POST endpoint: sample data
@app.route("/data", methods=["GET", "POST"])
def data():
    if request.method == "GET":
        return jsonify(sample_data), 200

    # Handle POST requests
    new_data = request.get_json(silent=True)

    if not isinstance(new_data, dict):
        return jsonify({
            "error": "A JSON object is required"
        }), 400

    if "name" not in new_data or "category" not in new_data:
        return jsonify({
            "error": "Name and category are required"
        }), 400

    new_item = {
        "id": len(sample_data) + 1,
        "name": new_data["name"],
        "category": new_data["category"]
    }

    sample_data.append(new_item)

    return jsonify({
        "message": "Data added successfully",
        "item": new_item
    }), 201

if __name__ == "__main__":
    app.run(debug=True, port=5001)