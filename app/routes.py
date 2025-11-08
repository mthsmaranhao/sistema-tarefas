from flask import Blueprint, request, jsonify
from app.models import Task

bp = Blueprint("tasks", __name__)

@bp.route("/", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "tasks-api"}), 200

@bp.route("/tasks", methods=["GET"])
def get_all_tasks():
    tasks = Task.find_all()
    return jsonify(tasks)
