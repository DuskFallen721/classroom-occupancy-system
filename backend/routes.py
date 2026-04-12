from flask import Blueprint, current_app, jsonify

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return current_app.send_static_file('index.html')

@main.route('/api/status')
def api_status():
    return jsonify({
        'status': 'ok',
        'message': 'Backend connected',
        'service': 'Classroom Occupancy Monitoring System'
    })
