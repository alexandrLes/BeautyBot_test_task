from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

def handle_function_one(data):
    logging.info(f"handle_function_one")
    return {"status": "success", "message": "handle_function_one"}

def handle_function_two(data):
    logging.info(f"handle_function_two")
    return {"status": "success", "message": "handle_function_two"}

function_router = {
    "function_one": handle_function_one,
    "function_two": handle_function_two,
}

@app.route('/Datalore', methods=['POST'])
def datalore_endpoint():
    data = request.json
    function_name = data.get('function')

    if not function_name:
        return jsonify({"status": "error", "message": "No function"}), 400

    handler = function_router.get(function_name)
    if not handler:
        return jsonify({"status": "error", "message": f"Unknown function"}), 400

    try:
        result = handler(data)
        return jsonify(result), 200
    except Exception as e:
        logging.error(f"Error handling function {function_name}: {e}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(port=5000)
