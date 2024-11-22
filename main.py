from flask import Flask  # Importing the Flask library to create the web application

# Initialize the Flask application
app = Flask(__name__)

# Define the route for the home page
@app.route("/")
def hello_world():
    """Handles the home page request and returns a simple HTML message."""
    return "<p>Hello, World!</p>"

# Run the application only if the script is executed directly
if __name__ == "__main__":
    app.run()
