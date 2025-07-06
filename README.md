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


## 🧪 How to Run the Project Locally

- Create a new virtual environment  
  ```
  pip install virtualenv
  ```

- Create the virtual env  
  ```
  virtualenv venv
  ```

- Activate the virtual env  
  ```
  venv\Scripts\activate
  ```

- Install Python requirements  
  ```
  pip install -r requirements.txt
  ```

- Make sure MongoDB is running  
  ```
  mongodb://localhost:27017
  ```

- Run the Flask app  
  ```
  python app.py
  ```

- Expose localhost using Ngrok  
  ```
  ngrok http 5000
  ```

- Test GitHub Webhook: Push, Pull Request, Merge

- View live updates (refreshes every 15 seconds)  
  ```
  http://localhost:5000/events/view
  ```







