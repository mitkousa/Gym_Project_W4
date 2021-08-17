from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.booking import Booking
import repositories.booking_repository as booking_repository
import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings")
def bookings():
    bookings = booking_repository.select_all()
    return render_template("bookings/index.html", bookings = bookings)

@bookings_blueprint.route("/bookings/new")
def new_booking():
    members = member_repository.select_all()
    lessons = lesson_repository.select_all()
    return render_template("bookings/new.html", members = members, lessons = lessons)

@bookings_blueprint.route("/bookings/<id>/edit")
def edit_booking(id):
    booking = booking_repository.select(id)
    members = member_repository.select_all()
    lessons = lesson_repository.select_all()
    return render_template('bookings/edit.html', booking=booking, members=members, lessons=lessons)

@bookings_blueprint.route("/bookings/<id>", methods=['POST'])
def update_booking(id):
    member_id = request.form["member_id"]
    lesson_id = request.form["lesson_id"]
    member = member_repository.select(member_id)
    lesson = lesson_repository.select(lesson_id)
    booking = Booking(member, lesson, id)
    booking_repository.update(booking)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>")
def show(id):
    booking = booking_repository.select(id)
    members = booking_repository.members(booking)
    return render_template("bookings/show.html", booking = booking, members = members)

@bookings_blueprint.route("/bookings", methods = ['POST'])
def create_booking():
    member_id = request.form['member_id']
    lesson_id = request.form['lesson_id']
    member = member_repository.select(member_id)
    lesson = lesson_repository.select(lesson_id)
    booking = Booking(member, lesson)
    booking_repository.save(booking)
    return redirect("/bookings")

@bookings_blueprint.route("/bookings/<id>/delete", methods = ['POST'])
def delete_booking(id):
    booking_repository.delete(id)
    return redirect("/bookings")

