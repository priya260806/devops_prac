Practical 2:

Aim:
Building a REST API with Flask or FastAPI.

a. Create a simple REST API using Flask or FastAPI with CRUD operations for a
"To-Do List" application.

b. Test the API using Postman or curl.


Solution:

Step 1: Check if Python is Installed

Open Command Prompt (CMD) and run:

python --version

Output:

Python 3.12.4


Step 2: Create a Project Folder

Create a folder for your Flask project:

Flask_Project

Open Command Prompt and navigate to it:

cd path\to\Flask_Project

Example:

cd C:\Users\Nikhita\Documents\Flask_Project


Step 3: Create a Virtual Environment (Recommended)

Inside the project folder, run:

python -m venv venv

This creates a virtual environment named venv.

Activate it:

Windows

venv\Scripts\activate

You should see:

(venv) C:\Users\Nikhita\Documents\Flask_Project>


Step 4: Install Flask

With the virtual environment activated, run:

pip install flask


Step 5: Verify Installation

pip show flask

or

python -m flask --version

Example output:

Flask 3.x.x
Werkzeug 3.x.x


Step 6: Create Your First Flask App

Create a file named app.py:

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(debug=True)


Step 7: Run the Flask App

In Command Prompt:

python app.py

You should see:

* Running on http://127.0.0.1:5000

Open your browser and visit:

http://127.0.0.1:5000

Output:

Hello, Flask!


Code 2:

Replace the code with:

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to my first Flask API",
        "status": "success"
    })

if __name__ == '__main__':
    app.run(debug=True)


Run again:

python app.py

Visit:

http://127.0.0.1:5000

Output:

{
    "message": "Welcome to my first Flask API",
    "status": "success"
}

This is your first REST API endpoint in Flask.


Code 3:

from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data storage
todos = [
    {
        "id": 1,
        "title": "Learn Flask",
        "completed": False
    }
]


# CREATE a new task
@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()

    new_todo = {
        "id": len(todos) + 1,
        "title": data['title'],
        "completed": False
    }

    todos.append(new_todo)

    return jsonify(new_todo), 201


# READ all tasks
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)


# READ a single task
@app.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    todo = next((t for t in todos if t['id'] == id), None)

    if todo is None:
        return jsonify({"message": "Task not found"}), 404

    return jsonify(todo)


# UPDATE a task
@app.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = next((t for t in todos if t['id'] == id), None)

    if todo is None:
        return jsonify({"message": "Task not found"}), 404

    data = request.get_json()

    todo['title'] = data.get('title', todo['title'])
    todo['completed'] = data.get('completed', todo['completed'])

    return jsonify(todo)


# DELETE a task
@app.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    global todos

    todo = next((t for t in todos if t['id'] == id), None)

    if todo is None:
        return jsonify({"message": "Task not found"}), 404

    todos = [t for t in todos if t['id'] != id]

    return jsonify({"message": "Task deleted successfully"})


if __name__ == '__main__':
    app.run(debug=True)


Run again:

python app.py

Visit:

http://127.0.0.1:5000/todos
http://127.0.0.1:5000/todos/2