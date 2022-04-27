from flask import Blueprint, render_template, request, redirect

from models.class_type import ClassType
from repositories import class_type_repository

class_types_blueprint = Blueprint("class_types", __name__)

# INDEX
@class_types_blueprint.route("/class_types")
def class_types():
    return render_template("class_types/index.html", class_types = class_type_repository.select_all())