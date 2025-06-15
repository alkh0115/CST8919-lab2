from flask import Flask, request, Response
import logging

# Create the Flask app
app = Flask(__name__)

# Configure logging
handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)  # Capture WARNING and above
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
app.logger.addHandler(handler)
app.logger.setLevel(logging.WARNING)

# Define a simple GET route for testing
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask Security Demo App"

# Define the POST /login route
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "admin" and password == "pass123":
        app.logger.info(f"Successful login for user: {username}")
        return Response("Login successful", status=200)
    else:
        app.logger.warning(f"SECURITY-ALERT: Failed login attempt for user: {username}")
        return Response("Login failed", status=401)

# Run the app (used for local development)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
