from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.lesson import Lesson
import repositories.lesson_repository as lesson_repository

lessons_blueprint = Blueprint("lessons", __name__)

@lessons_blueprint.route("/lessons")
def lessons():
    lessons = lesson_repository.select_all()
    return render_template("lessons/index.html", lessons = lessons)

@lessons_blueprint.route("/lessons/new")
def new_lesson():
    return render_template("lessons/new.html")

@lessons_blueprint.route("/lessons", methods=["POST"])
def create_lesson():
    name = request.form["name"]
    duration = request.form["duration"]
    start_time = request.form["start_time"]
    lesson = Lesson(name, duration, start_time)
    lesson_repository.save(lesson)
    return redirect("/lessons")

@lessons_blueprint.route("/lessons/<id>")
def show(id):
    lesson = lesson_repository.select(id)
    members = lesson_repository.members(lesson)
    return render_template("lessons/show.html", lesson=lesson, members=members)

@lessons_blueprint.route("/lessons/<id>/edit")
def edit_lesson(id):
    lesson = lesson_repository.select(id)
    return render_template('lessons/edit.html', lesson=lesson)

@lessons_blueprint.route("/lessons/<id>", methods=["POST"])
def update_lesson(id):
    name = request.form["name"]
    duration = request.form["duration"]
    start_time = request.form["start_time"]
    lesson = Lesson(name, duration, start_time, id)
    lesson_repository.update(lesson)
    return redirect("/lessons")

@lessons_blueprint.route("/lessons/<id>/delete", methods=["POST"])
def delete_lesson(id):
    lesson_repository.delete(id)
    return redirect("/lessons")

