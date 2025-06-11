from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head><title>My Web Page</title></head>
        <body>
            <h1>Hello from Flask!</h1>
            <p>This is a simple Python web app.</p>
        </body>
    </html>
    """
