from db.run_sql import run_sql
from models.booking import Booking
import repositories.lesson_repository as lesson_repository
import repositories.member_repository as member_repository

def save(booking):
    sql = "INSERT INTO bookings ( member_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.lesson.id]
    results = run_sql( sql, values )
    booking.id = results[0]['id']
    return booking


def select_all():
    bookings = []

    sql = "SELECT * FROM bookings"
    results = run_sql(sql)

    for row in results:
        member = member_repository.select(row['member_id'])
        lesson = lesson_repository.select(row['lesson_id'])
        booking = Booking(member, lesson, row['id'])
        bookings.append(booking)
    return bookings

def update(booking):
    sql = "UPDATE bookings SET (member_id, lesson_id) = (%s, %s) WHERE id = %s"
    values = [booking.member.id, booking.lesson.id, booking.id]
    run_sql(sql, values)