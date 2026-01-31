from flask import Flask, render_template, jsonify, request, abort

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/status')
def status():
    return jsonify(status="online", version="1.1.0")

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form.get('student_name')
    if not data:
        abort(400)  # Bad Request
    return jsonify(message=f"Received: {data}"), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
