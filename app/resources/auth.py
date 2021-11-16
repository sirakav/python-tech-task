# Flask and other third party packages
from flask import Blueprint, jsonify

blueprint = Blueprint("auth", __name__, url_prefix="/auth")


@blueprint.route("/token", methods=["POST"])
def token():
    return jsonify({"message": "This endpoint should issue auth token"})
