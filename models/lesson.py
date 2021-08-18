from models.member import Member
class Lesson:

    def __init__(self, name, duration, start_time, capacity, id = None):
        self.name = name
        self.duration = duration
        self.start_time = start_time
        self.capacity = capacity
        self.id = id