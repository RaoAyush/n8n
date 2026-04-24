# from flask import Flask, render_template, jsonify
# import requests


# app = Flask(__name__ )

# # 👉 Your n8n production webhook URL
# DATA_SOURCE_URL = "http://localhost:5678/webhook/get-news"




# # 🏠 Home page (UI)
# @app.route('/')
# def home():
#     return render_template('index.html')


# # 🔌 API route (Frontend will call this)
# @app.route('/get-news')
# def get_news():
#     try:
#         response = requests.get(DATA_SOURCE_URL)

#         # Check if request successful
#         if response.status_code != 200:
#             return jsonify({"error": "Failed to fetch from n8n"}), 500

#         data = response.json()

#         # Ensure data is list
#         if not isinstance(data, list):
#             return jsonify({"error": "Invalid data format"}), 500

#         return jsonify(data)

#     except Exception as e:
#         return jsonify({"error": str(e)}), 500


# # ▶️ Run server
# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

# 👉 Replace with your LIVE n8n URL
DATA_SOURCE_URL = "https://your-n8n-url/webhook/get-news"


# 🏠 Home page
@app.route('/')
def home():
    return render_template('index.html')


# 🔌 API route
@app.route('/get-news')
def get_news():
    try:
        response = requests.get(DATA_SOURCE_URL)

        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch from n8n"}), 500

        data = response.json()

        if not isinstance(data, list):
            return jsonify({"error": "Invalid data format"}), 500

        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ▶️ Run server (ONLY THIS ONE)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)