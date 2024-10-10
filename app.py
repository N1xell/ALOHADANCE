from flask import Flask, render_template, request, redirect
import database

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/lessons')
def lessons():
    lessons = database.get_all_lessons()
    return render_template('lessons.html', lessons=lessons)

@app.route('/add_lesson', methods=['GET', 'POST'])
def add_lesson():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        database.add_lesson(title, description)
        return redirect('/lessons')
    return render_template('add_lesson.html')

if __name__ == '__main__':
    app.run(debug=True)
