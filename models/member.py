class Member:
    def __init__(self, first_name, last_name, membership_number, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.membership_number = membership_number

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"