from models.member import Member
from models.class_type import ClassType

from repositories import member_repository, class_type_repository

member_repository.delete_all()
class_type_repository.delete_all()

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