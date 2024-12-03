from flask import Flask, request, jsonify

app = Flask(__name__)


# Define a route to handle print requests
@app.route('/print', methods=['POST'])
def print_text():
    data = request.json  # Expecting a JSON body in the request
    if not data or 'text' not in data:
        return jsonify({"error": "No text provided"}), 400

    text_to_print = data['text']

    # Placeholder for the printer function call
    print(f"Received text to print: {text_to_print}")

    # You'd call your printer operator function here instead of this print statement.
    # e.g., printer_operator.print(text_to_print)

    return jsonify({"message": "Print request received"}), 200


if __name__ == "__main__":
    app.run(port=5000)
