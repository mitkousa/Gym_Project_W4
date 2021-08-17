import pdb
from models.member import Member
from models.lesson import Lesson
from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository
import repositories.booking_repository as booking_repository

member_repository.delete_all()
lesson_repository.delete_all()
booking_repository.delete_all()

member1 = Member("Will Smith")
member_repository.save(member1)

member2 = Member("Rachel McAdams")
member_repository.save(member2)

member3 = Member("Ryan Gosling")
member_repository.save(member3)

member4 = Member("Eva Mendes")
member_repository.save(member4)

lesson1 = Lesson("Yoga", 45, "18:00", 4)
lesson_repository.save(lesson1)

lesson2 = Lesson("Bootcamp", 30, "12:00", 6)
lesson_repository.save(lesson2)

lesson3 = Lesson("Burn it", 25, "17:00", 3)
lesson_repository.save(lesson3)

lesson4 = Lesson("Zumba", 40, "16:00", 2)
lesson_repository.save(lesson4)

booking1 = Booking(member1, lesson2)
booking_repository.save(booking1)

booking2 = Booking(member2, lesson1)
booking_repository.save(booking2)

booking3 = Booking(member3, lesson4)
booking_repository.save(booking3)

booking4 = Booking(member4, lesson3)
booking_repository.save(booking4)

pdb.set_trace()


