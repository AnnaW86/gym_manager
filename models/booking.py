from repositories import start_time_repository

class Booking:
    def __init__(self, member, gym_class, id=None):
        self.member = member
        self.gym_class = gym_class
        self.id = id

    def find_available_class_times(self, id):
        available_class_times = []
        all_start_times = start_time_repository.select_all_ids()
        existing_bookings = start_time_repository.select_all_ids_for_class_type(id)
        for time in all_start_times:
            if time.id not in existing_bookings:
                available_class_times.append(time)