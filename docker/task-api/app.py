from flask import Flask, jsonify, request

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


@app.route("/tasks/<int:task_id>")
def get_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            return jsonify(task)

    return jsonify(
        {
            "error": "Task not found"
        }
    ), 404


@app.route("/tasks",method=["POST"])
def create_task():
    data = request.get_json()

    task ={
        "id":len(tasks)+1,
        "title":data['title'],
        "completed":False
    }

    tasks.append(task)
    return jsonify(task),201


@app.route("/tasks/<int:task_id>",method="DELETE")
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify(
                {
                    "message": "Task deleted successfully"
                }
            ), 200
    return jsonify(
        {
            "error": "Task not found"
        }
    ), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)