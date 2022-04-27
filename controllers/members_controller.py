from flask import Blueprint, redirect, render_template, request

from models.member import Member
from repositories import member_repository

members_blueprint = Blueprint("members", __name__)

# INDEX
@members_blueprint.route("/members")
def members():
    return render_template("members/index.html", members = member_repository.select_all())

# NEW
@members_blueprint.route("/members/new")
def new_member():
    return render_template("members/new.html", )

# CREATE
@members_blueprint.route("/members", methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership_number = request.form['membership_number']
    member = Member(first_name, last_name, membership_number)
    member_repository.save(member)
    return redirect('/members')