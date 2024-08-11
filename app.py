from flask import Flask, request, jsonify, send_from_directory
import cleverbotfreeapi

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        message = data.get('message')
        context = data.get('context', [])
        session = data.get('session', None)

        response = cleverbotfreeapi.cleverbot(message, context, session)
        return jsonify({'reply': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
