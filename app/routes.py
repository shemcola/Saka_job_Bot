from flask import Blueprint, request, jsonify
from .utils.resume_parser import parse_resume
from .utils.job_scraper import scrape_jobs

api = Blueprint('api', __name__)

@api.route('/upload-resume', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    file.save(f"./uploads/{file.filename}")
    result = parse_resume(f"./uploads/{file.filename}")
    return jsonify(result)

@api.route('/search-jobs', methods=['GET'])
def search_jobs():
    query = request.args.get('query')
    location = request.args.get('location')
    jobs = scrape_jobs(query, location)
    return jsonify(jobs)
