from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    if data.get('action') in ['opened', 'synchronize']:
        print(f"Received PR {data['pull_request']['id']}")
        return {"status": "received"}, 200
    return {"error": "Unsupported action"}, 400


@app.route('/prs', methods=['GET'])
def list_prs():
    # Temporary mocked data to unblock UI
    return [
        {
            "id": 1,
            "summary": "Initial PR",
            "reviewBullets": ["Check syntax", "Review tests", "Optimize code"],
            "comment": "Looks good!"
        }
    ]


@app.route('/health', methods=['GET'])
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(port=3000)