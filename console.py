from models.member import Member
from models.class_type import ClassType
from models.location import Location
from models.gym_class import GymClass
from models.booking import Booking
from models.membership_type import MembershipType

from repositories import member_repository, class_type_repository, location_repository, gym_class_repository, booking_repository, membership_type_repository

booking_repository.delete_all()
gym_class_repository.delete_all()
member_repository.delete_all()
class_type_repository.delete_all()
location_repository.delete_all()
membership_type_repository.delete_all()

membership_type1 = MembershipType("premium")
membership_type_repository.save(membership_type1)
membership_type2 = MembershipType("off peak")
membership_type_repository.save(membership_type2)

member1 = Member("Rachel", "Jones", 123456, membership_type1)
member2 = Member("David", "Bates", 652143, membership_type2)
member3 = Member("Meena", "Zaib", 332753, membership_type2)
member4 = Member("Emilio", "Cortez", 834852, membership_type1)
member5 = Member("Sam", "McDonald", 659536, membership_type1)
member6 = Member("Charlie", "Davies", 748593, membership_type2)
member7 = Member("Susan", "Stevens", 345379, membership_type1)
member8 = Member("Petra", "Parrot", 365495, membership_type2)
member9 = Member("Guillaume", "Barca", 568752, membership_type1)
member10 = Member("Sacha", "Cortz", 193946, membership_type2)
member11 = Member("Russel", "Wentsworth", 887456, membership_type1)
member12 = Member("David", "MacLaren", 876924, membership_type1)
member13 = Member("Ahmad", "Baqri", 531123, membership_type2)
member14 = Member("Emily", "Robinson", 848435, membership_type1)
member15 = Member("Kit", "Bilson", 384200, membership_type1)

members = [member1,member2,member3,member4,member5,member6,member7,member8,member9,member10,member11,member12,member13,member14,member15]

for member in members:
    member.mark_active_member()
    member_repository.save(member)


spin = ClassType('Spin', 4, 'Hard work')
class_type_repository.save(spin)
pilates = ClassType('Pilates', 2, 'Tone and strengthen')
class_type_repository.save(pilates)
hiit = ClassType('HIIT', 5, 'High impact')
class_type_repository.save(hiit)
aquafit = ClassType('Aquafit', 2, 'Low impact strengthening')
class_type_repository.save(aquafit)

location1 = Location('Main gym')
location_repository.save(location1)
location2 = Location('Studio')
location_repository.save(location2)
location3 = Location('Pool')
location_repository.save(location3)



class1 = GymClass(spin, '6am', 30, location1, 8)
class2 = GymClass(spin, '7am', 30, location1, 8)
class3 = GymClass(spin, '11am', 45, location1, 8)
class4 = GymClass(spin, '2pm', 45, location1, 8)
class5 = GymClass(spin, '5pm', 45, location1, 8)
class6 = GymClass(spin, '6pm', 30, location1, 8)
class7 = GymClass(pilates, '8am', 25, location2, 15)
class8 = GymClass(pilates, '9am', 25, location2, 15)
class9 = GymClass(pilates, '10am', 40, location2, 15)
class10 = GymClass(pilates, '12pm', 40, location2, 15)
class11 = GymClass(pilates, '3pm', 30, location2, 15)
class12 = GymClass(hiit, '11am', 30, location2, 10)
class13 = GymClass(hiit, '5pm', 30, location2, 10)
class14 = GymClass(hiit, '8pm', 45, location2, 10)
class15 = GymClass(aquafit, '1pm', 30, location3, 10)

gym_classes = [class1, class2, class3, class4, class5, class6, class7, class8, class9, class10, class11, class12, class13, class14, class15]

for gym_class in gym_classes:
    gym_class_repository.save(gym_class)


booking1 = Booking(member1, class2)
booking2 = Booking(member1, class7)
booking3 = Booking(member5, class4)
booking4 = Booking(member5, class11)
booking5 = Booking(member3, class2)
booking6 = Booking(member9, class2)
booking7 = Booking(member11, class13)
booking8 = Booking(member14, class14)

bookings = [booking1,booking2,booking3,booking4,booking5,booking6,booking7,booking8]

for booking in bookings:
    booking_repository.save(booking)


