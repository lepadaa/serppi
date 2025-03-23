from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

SERPAPI_KEY = os.environ.get("SERPAPI_KEY")

@app.route('/web_search', methods=['POST'])
def web_search():
    data = request.json
    query = data.get("query")

    params = {
        "engine": "google",
        "q": query,
        "hl": "en",
        "gl": "fi",
        "api_key": SERPAPI_KEY
    }

    response = requests.get("https://serpapi.com/search", params=params)
    results = []

    if response.status_code == 200:
        data = response.json()
        organic_results = data.get("organic_results", [])
        for item in organic_results[:5]:
            results.append({
                "title": item.get("title"),
                "snippet": item.get("snippet"),
                "url": item.get("link")
            })

    return jsonify({"results": results})
