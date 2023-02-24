from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def users_lists():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template ('index.html', users=users)


@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try again.'


if __name__ == "__main__":
    app.run(debug=True)
