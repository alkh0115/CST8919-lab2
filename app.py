from flask import Flask, request
import logging

app = Flask(__name__)

# Configure logging to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

@app.route("/")
def home():
    return "Welcome to the Flask Security Demo App"

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    # Demo validation
    if username == "admin" and password == "pass123":
        logging.info(f"Successful login for user: {username}")
        return "Login successful", 200
    else:
        logging.warning(f"Failed login attempt for user: {username}")
        return "Login failed", 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
