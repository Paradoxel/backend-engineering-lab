from flask import Flask

app = Flask(__name__)

tasks = [
    {
        "id": 1,
        "title": "Learn Docker",
        "completed": False,
    },
    {
        "id": 2,
        "title": "Build Flask API",
        "completed": True,
    },
]



@app.route("/")
def home():
    return {
        "message": "Welcome to Task API",
        "status": "running",
    }


@app.route("/tasks")
def get_tasks():
    return tasks


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)