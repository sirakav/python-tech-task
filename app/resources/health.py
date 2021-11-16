# Standart library
from time import time

# Flask and other third party packages
from flask import Blueprint, jsonify

blueprint = Blueprint("health", __name__)


@blueprint.route("/health")
def health():
    return jsonify({"message": time()})
