from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return "Hello from Dockerized Python App!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

# To run this Flask app, you can use the command:
# python sample.py
# To run this Flask app in a Docker container, you can create a Dockerfile
# and build the image using: 
# docker build -t my-flask-app .
# Then run the container with:
# docker run -p 5000:5000 my-flask-app
# You can access the app at http://localhost:5000
# Note: Make sure you have Flask installed in your Python environment.
# You can install Flask using pip: 
# pip install Flask
# Ensure you have Docker installed to build and run the container.