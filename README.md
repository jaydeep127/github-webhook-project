# GitHub Webhook Listener (Flask + MongoDB)

This project listens to GitHub Webhook events like:

- ✅ Push
- ✅ Pull Request
- ✅ Merge (bonus)

It stores each event in MongoDB and displays them in a live auto-refreshing UI built using Flask.

---

## 🚀 Features

- Accepts GitHub webhook events
- Detects push, pull request, and merge actions
- Stores data in MongoDB
- Displays data in browser (refreshes every 15 seconds)
- Easy to run locally

---

## 📦 Technologies Used

- Python 3
- Flask
- PyMongo
- flask-cors
- MongoDB
- GitHub Webhooks
- HTML + CSS

---

## 🧪 How to Run Locally

1. **Install dependencies**
```bash
pip install -r requirements.txt
2. Make Sure MongoDB is Running
MongoDB must be running on your machine at:
mongodb://localhost:27017
