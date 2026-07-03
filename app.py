from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Docker Compose Project by Shimya Yusuf</h1><h2>DevOps Portfolio</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
