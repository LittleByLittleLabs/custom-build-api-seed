import os
from flask import Flask, url_for, jsonify, request, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, '../data.sqlite')

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

db = SQLAlchemy(app)


class ValidationError(ValueError):
    pass


class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)

    def get_url(self):
        return url_for('get_student', id=self.id, _external=True)

    def export_data(self):
        return {
            'self_url': self.get_url(),
            'name': self.name
        }

    def import_data(self, data):
        try:
            self.name = data['name']
        except KeyError as e:
            raise ValidationError('Invalid student: missing ' + e.args[0])
        return self


@app.route('/students/', methods=['GET'])
def get_students():
    return jsonify({'students': [student.get_url() for student in
                                  Student.query.all()]})

@app.route('/students/<int:id>', methods=['GET'])
def get_student(id):
    return jsonify(Student.query.get_or_404(id).export_data())

@app.route('/students/', methods=['POST'])
def new_student():
    student = Student()
    student.import_data(request.json)
    db.session.add(student)
    db.session.commit()
    return jsonify({}), 201, {'Location': student.get_url()}

@app.route('/students/<int:id>', methods=['PUT'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    student.import_data(request.json)
    db.session.add(student)
    db.session.commit()
    return jsonify({})

# todo: implement this template
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.route('/')
def index():
    highlight = {'min': 1, 'max': 2}
    students = Student.query.all()
    return render_template('index.html', students=students, highlight=highlight)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
