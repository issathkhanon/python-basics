"""A class register served by Flask.

Run this file from this folder:

    python 30_learn_flask.py

Then open http://127.0.0.1:5000/ in a browser.
The /students addresses answer with JSON. The notebook shows the curl commands.

The script points Flask at the templates folder beside this file.
Each @app.route connects one address and one method to one function.
The server starts only when you run this file.
"""

from pathlib import Path

from flask import Flask, jsonify, render_template, request

# templates/ sits beside this file
app = Flask(__name__, template_folder=Path(__file__).resolve().parent / "templates")

students = [{"id": 1, "name": "Issath"}]


def find_student(student_id):
    """Return the student with this id, or None."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def next_student_id():
    """One more than the highest id already in the list."""
    if not students:
        return 1
    return max(student["id"] for student in students) + 1


@app.route("/")
def home():
    # GET / returns the page in templates/home.html
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    # GET shows the form. POST reads the typed name.
    if request.method == "POST":
        # the input in register.html is named "name"
        name = request.form["name"]
        students.append({"id": next_student_id(), "name": name})
        return render_template("added.html", name=name)
    return render_template("register.html")


@app.route("/students", methods=["GET"])
def get_students():
    return jsonify(students)


@app.route("/students/<int:student_id>", methods=["GET"])
def get_student(student_id):
    # <int:student_id> and the parameter student_id are the same name
    student = find_student(student_id)
    if student is None:
        return jsonify({"error": "student not found"}), 404
    return jsonify(student)


@app.route("/students", methods=["POST"])
def add_student():
    # request.json is the body {"name": "Khan"}
    new_student = {
        "id": next_student_id(),
        "name": request.json.get("name"),
    }
    # append changes this list, so the name students stays the same
    students.append(new_student)
    return jsonify(new_student)


@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    student = find_student(student_id)
    if student is None:
        return jsonify({"error": "student not found"}), 404
    student["name"] = request.json.get("name", student["name"])
    return jsonify(student)


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    global students
    # students = builds a new list, so this name must be the outer list
    if find_student(student_id) is None:
        return jsonify({"error": "student not found"}), 404
    students = [student for student in students if student["id"] != student_id]
    return jsonify(students)


if __name__ == "__main__":
    app.run(debug=True)
