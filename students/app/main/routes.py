from flask import render_template, redirect, url_for, request, jsonify, request, render_template
from . import main
from ..models import Student
from .. import db


@main.route('/students/', methods=['GET'])
def get_students():
    return jsonify({'students': [student.get_url() for student in
                                  Student.query.all()]})

@main.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    return jsonify(Student.query.get_or_404(id).export_data())

@main.route('/students/', methods=['POST'])
def new_student():
    student = Student()
    student.import_data(request.json)
    db.session.add(student)
    db.session.commit()
    return jsonify({}), 201, {'Location': student.get_url()}

@main.route('/students/<int:id>', methods=['PUT'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    student.import_data(request.json)
    db.session.add(student)
    db.session.commit()
    return jsonify({})

# todo: implement this template
@main.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@main.route('/')
def index():
    highlight = {'min': 1, 'max': 2}
    students = Student.query.all()
    return render_template('index.html', students=students, highlight=highlight)