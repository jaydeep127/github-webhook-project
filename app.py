from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["webhookDB"]
events_collection = db["events"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event_type = request.headers.get("X-GitHub-Event")
    entry = {"event_type": event_type, "timestamp": datetime.utcnow()}

    if event_type == "push":
        entry.update({
            "author": data["pusher"]["name"],
            "to_branch": data["ref"].split("/")[-1]
        })

    elif event_type == "pull_request":
        pr = data["pull_request"]
        entry.update({
            "author": pr["user"]["login"],
            "from_branch": pr["head"]["ref"],
            "to_branch": pr["base"]["ref"]
        })
        
          # ✅ Check if the PR was merged
        if pr.get("merged") or (data.get("action") == "closed" and pr.get("merged")):
            entry["event_type"] = "merge"

    events_collection.insert_one(entry)
    return jsonify({"message": "Webhook received"}), 200

# JSON API (used for testing or frontend fetch)
@app.route("/events", methods=["GET"])
def get_events():
    events = list(events_collection.find().sort("timestamp", -1).limit(10))
    for e in events:
        e["_id"] = str(e["_id"])
        e["timestamp"] = e["timestamp"].strftime("%d %B %Y - %I:%M %p UTC")
    return jsonify(events)

# HTML page route to display event table
@app.route("/events/view")
def show_events():
    events = list(events_collection.find().sort("timestamp", -1).limit(50))
    return render_template("events.html", events=events)

if __name__ == "__main__":
    app.run(port=5000)
