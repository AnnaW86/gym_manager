class Member:
    def __init__(self, first_name, last_name, membership_number, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_number = membership_number
        self.id = id

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def check_members_existing_booking(self, gym_class, bookings):
        booked = False
        for booking in bookings:
            if booking.member_id == self.id and booking.gym_class_id == gym_class.id:
                booked = True
        return booked