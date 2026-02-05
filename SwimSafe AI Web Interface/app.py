from flask import Flask, render_template, Response, request, jsonify
from detector import generate_frames, list_cameras
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cameras')
def cameras():
    # Returns a JSON list of available camera indices
    return {'cameras': list_cameras()}

@app.route('/video_feed')
def video_feed():
    # If accessed directly in browser, show a message
    if 'text/html' in request.headers.get('Accept', '') and 'camera_id' not in request.args:
        return "<h3>This endpoint provides a video stream for the main page. Please visit the <a href='/'>home page</a> to view the video feed.</h3>"
    camera_id = int(request.args.get('camera_id', 0))
    return Response(
        generate_frames(camera_id),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )

@app.route('/history')
def history():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # or your real password if set
        database="swimsafe_ai"
    )
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM history ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    return render_template('history.html', logs=logs)

@app.route('/history_data')
def history_data():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="swimsafe_ai"
    )
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM history ORDER BY timestamp DESC")
    logs = cursor.fetchall()
    cursor.close()
    db.close()
    return jsonify({'logs': logs})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
