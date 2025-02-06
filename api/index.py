from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/greet', methods=['get'])
def greet():

    name = request.args.get('name')

    if name:
        return jsonify({"message" : f"HI, {name}"})
    else:
        return jsonify({"error": "please enter a name"})

if __name__ = '__main__':
    app.run(debug=True)
