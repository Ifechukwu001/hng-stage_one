from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/stage-one-api")
def app_api():
    """JSON API"""
    slack_name = request.args.get("slack_name")
    track = request.args.get("track")

    weekdays = {
        0: "Monday",
        1: "Tuesday",
        2: "Wednesday",
        3: "Thursday",
        4: "Friday",
        5: "Saturday",
        6: "Sunday"
    }

    date = datetime.utcnow()
    utc_time = datetime.isoformat(date).split(".")[0]

    response = {
        "slack_name": slack_name,
        "current_day": weekdays[date.weekday()],
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Ifechukwu001/hng-stage_one/blob/main/app.py",
        "github_repo_url": "https://github.com/Ifechukwu001/hng-stage_one",
        "status_code": 200
    }

    return jsonify(response)
