from flask import render_template, request, redirect, url_for
from app import app, db
from models import Bug

@app.route('/')
def index():
    bugs = Bug.query.all()
    return render_template('index.html', bugs=bugs)

@app.route('/add', methods=['POST'])
def add_bug():
    title = request.form.get('title')
    description = request.form.get('description')
    new_bug = Bug(title=title, description=description)
    db.session.add(new_bug)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_bug(id):
    bug = Bug.query.get_or_404(id)
    bug.status = request.form.get('status')
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete_bug(id):
    bug = Bug.query.get_or_404(id)
    db.session.delete(bug)
    db.session.commit()
    return redirect(url_for('index'))
