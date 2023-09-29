from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)

@app.route('/')
def index():
    return render_template('courses.html')

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    course_list = [{'id': course.id, 'title': course.title, 'description': course.description} for course in courses]
    return jsonify(course_list)

@app.route('/course/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    if course:
        return jsonify({'id': course.id, 'title': course.title, 'description': course.description})
    else:
        return jsonify({'message': 'Course not found'}), 404

@app.route('/course', methods=['POST'])
def create_course():
    data = request.get_json()
    new_course = Course(title=data['title'], description=data['description'])
    db.session.add(new_course)
    db.session.commit()
    return jsonify({'message': 'Course created successfully'}), 201

@app.route('/course/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get(course_id)
    if course:
        data = request.get_json()
        course.title = data['title']
        course.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Course updated successfully'})
    else:
        return jsonify({'message': 'Course not found'}), 404

@app.route('/course/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get(course_id)
    if course:
        db.session.delete(course)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully'})
    else:
        return jsonify({'message': 'Course not found'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
