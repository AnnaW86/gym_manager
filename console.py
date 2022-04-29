from models.member import Member
from models.class_type import ClassType
from models.location import Location
from models.start_time import StartTime
from models.gym_class import GymClass
from models.booking import Booking

from repositories import member_repository, class_type_repository, location_repository, start_time_repository, gym_class_repository, booking_repository

booking_repository.delete_all()
gym_class_repository.delete_all()
member_repository.delete_all()
class_type_repository.delete_all()
location_repository.delete_all()
start_time_repository.delete_all()

member1 = Member("Rachel", "Jones", 123456)
member2 = Member("David", "Bates", 652143)
member3 = Member("Meena", "Zaib", 332753)
member4 = Member("Emilio", "Cortez", 834852)
member5 = Member("Sam", "McDonald", 659536)
member6 = Member("Charlie", "Davies", 748593)
member7 = Member("Susan", "Stevens", 345379)
member8 = Member("Petra", "Parrot", 365495)
member9 = Member("Guillaume", "Barca", 568752)
member10 = Member("Sacha", "Cortz", 193946)
member11 = Member("Russel", "Wentsworth", 887456)
member12 = Member("David", "MacLaren", 876924)
member13 = Member("Ahmad", "Baqri", 531123)
member14 = Member("Emily", "Robinson", 848435)
member15 = Member("Kit", "Bilson", 384200)

members = [member1,member2,member3,member4,member5,member6,member7,member8,member9,member10,member11,member12,member13,member14,member15]

for member in members:
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

am6 = StartTime('6am')
am7 = StartTime('7am')
am8 = StartTime('8am')
am9 = StartTime('9am')
am10 = StartTime('10am')
am11 = StartTime('11am')
pm12 = StartTime('12pm')
pm1 = StartTime('1pm')
pm2 = StartTime('2pm')
pm3 = StartTime('3pm')
pm4 = StartTime('4pm')
pm5 = StartTime('5pm')
pm6 = StartTime('6pm')
pm7 = StartTime('7pm')
pm8 = StartTime('8pm')
pm9 = StartTime('9pm')
pm10 = StartTime('10pm')

start_times = [am6,am7,am8,am9,am10,am11,pm12,pm1,pm2,pm3,pm4,pm5,pm6,pm7,pm8,pm9,pm10]

for time in start_times:
    start_time_repository.save(time)


class1 = GymClass(spin, am6, 30, location1, 8)
class2 = GymClass(spin, am7, 30, location1, 8)
class3 = GymClass(spin, am11, 45, location1, 8)
class4 = GymClass(spin, pm2, 45, location1, 8)
class5 = GymClass(spin, pm5, 45, location1, 8)
class6 = GymClass(spin, pm6, 30, location1, 8)
class7 = GymClass(pilates, am8, 25, location2, 15)
class8 = GymClass(pilates, am9, 25, location2, 15)
class9 = GymClass(pilates, am10, 40, location2, 15)
class10 = GymClass(pilates, pm12, 40, location2, 15)
class11 = GymClass(pilates, pm3, 30, location2, 15)
class12 = GymClass(hiit, am11, 30, location2, 10)
class13 = GymClass(hiit, pm5, 30, location2, 10)
class14 = GymClass(hiit, pm8, 45, location2, 10)
class15 = GymClass(aquafit, pm1, 30, location3, 10)

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


