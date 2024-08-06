from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 150000
}, {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 200000
}, {
    'id': 3,
    'title': 'Frontend Engineer',
    'location': 'Remote',
    'salary': 140000
}, {
    'id': 4,
    'title': 'Backend Engineer',
    'location': 'San Francisco, USA',
    'salary': 180000
}, {
    'id': 5,
    'title': 'Full Stack Engineer',
    'location': 'Remote',
    'salary': 220000
}]


@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
