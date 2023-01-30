from flask import Flask, render_template, request
from helpers import todo

app: Flask = Flask(__name__)


todo_list: list[todo] = []
todo_count: int = 0


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/view-todo-list', methods=["GET", "POST"])
def view_todo_list():
    if request.method == "POST" and len(todo_list) > 0:
        # an item was checked/unchecked -- len > 0 ensures refreshes don't potentially crash the site.
        id: int = int(request.form['check-button'])
        todo_list[id].checked = not todo_list[id].checked
    return render_template('view-list.html', todo_list=todo_list)


@app.route('/edit-todo<todo_number>', methods=["GET", "POST"])
def edit_todo(todo_number: str):
    if request.method == "POST":
        global todo_list

        title: str = request.form['title']
        description: str = request.form['description']
        color: str = request.form['color']
        category: str = request.form['category']
        fave: str = request.form['fave']

        if title == '':
            return render_template("edit-todo.html")

        todo_list[int(todo_number)].title = title
        todo_list[int(todo_number)].description = description
        todo_list[int(todo_number)].color = color
        todo_list[int(todo_number)].category = category
        todo_list[int(todo_number)].fave = fave

        return render_template("edit-success.html")
    return render_template('edit-todo.html', todo=todo_list[int(todo_number)])


@app.route('/create-todo', methods=["GET", "POST"])
def create_todo():
    if request.method == "POST":
        global todo_list
        global todo_count
        title: str = request.form['title']
        description: str = request.form['description']
        color: str = request.form['color']
        category: str = request.form['category']
        fave: str = request.form['fave']

        if title == '':
            return render_template("create-todo.html")

        new_todo: todo = todo(todo_count, title, description, color, category, fave)
        todo_list.append(new_todo)

        todo_count += 1

        return render_template("success.html", title=title, description=description, color=color, category=category, fave=fave)
    return render_template("create-todo.html")


if __name__ == '__main__':
    app.run(debug=True)