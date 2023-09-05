from app import app, db
from flask import render_template, request, url_for, redirect
from app.models import Student

@app.route('/students')
def list_students():
    students = Student.query.all()
    return render_template(template_name_or_list="students.html", students=students)


@app.route('/students/create', methods=['GET', 'POST'])
def create_student():
    stud_id = request.args.get('id')
    stud_name = request.args.get('name')
    student = Student(id=stud_id, name=stud_name)
    db.session.add(student)
    db.session.commit()
    return redirect(url_for('list_students'))
