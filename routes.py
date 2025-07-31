from app import app, db
from app.models import Job
from flask import jsonify, request

@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([{'id': j.id, 'title': j.title, 'company': j.company, 'description': j.description} for j in jobs])

@app.route('/jobs', methods=['POST'])
def add_job():
    data = request.get_json()
    new_job = Job(title=data['title'], company=data['company'], description=data['description'])
    db.session.add(new_job)
    db.session.commit()
    return jsonify({'message': 'Job added'}), 201