
class Student:
    def __init__(self, id, name, phone, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
    
    def __str__(self):
        return str(self.id) + " " + str(self.name) + " " + str(self.phone) + " " + str(self.address)


class FunCourse:
    pass

if __name__ == "__main__":
    course = FunCourse(3)
    course.add_student(Student(123, "Kári Halldórsson", "1234567", "Heimahagar 57"))
    course.add_student(Student(176, "Guðni Magnússon", "87685", "Heimahlíð 2"))
    course.add_student(Student(654, "Jón Jónsson", "54321", "Heimaholt 54"))
    course.add_student(Student(12, "Holgeir Friðgeirsson", "2354456567", "Heimateigur 65"))
    course.add_student(Student(32, "Geir Friðriksson", "99875", "Heimageisli 12"))

    print()
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    rem_id = 654
    print("\nremoving participant with id: " + str(rem_id) + "\n")
    course.remove_student(rem_id)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    rem_id = 176
    print("\nremoving participant with id: " + str(rem_id) + "\n")
    course.remove_student(rem_id)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    rem_id = 12
    print("\nremoving participant with id: " + str(rem_id) + "\n")
    course.remove_student(rem_id)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())