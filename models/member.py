class Member:
    def __init__(self, first_name, last_name, membership_number, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_number = membership_number
        self.id = id

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def check_existing_booking(self, enrolled_gym_classes, available_classes, bookable_classes):
        for available_class in available_classes:
            booked = False
            for enrolled_class in enrolled_gym_classes:
                if available_class.id == enrolled_class.id:
                    booked = True
            if booked == False:
                bookable_classes.append(available_class)
        return bookable_classes

