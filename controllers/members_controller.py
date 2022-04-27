from flask import Blueprint, redirect, render_template

from models.member import Member
from repositories import member_repository

members_blueprint = Blueprint("members", __name__)

#INDEX
@members_blueprint.route("/members")
def members():
    members = member_repository.select_all()
    return render_template("members/index.html", members = members)