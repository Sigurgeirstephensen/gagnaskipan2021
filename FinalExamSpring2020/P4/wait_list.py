
class Student:
    def __init__(self, id, name, phone, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.address = address
    
    def __str__(self):
        return str(self.id) + " " + str(self.name) + " " + str(self.phone) + " " + str(self.address)

    def __lt__(self, other):
        return self.name < other.name


class FunCourse:
    def __init__(self, max_participants):
        self.course_list = {}
        self.wait_list = []
        self.max_participants = max_participants

    def add_student(self, student):
        if len(self.course_list) < self.max_participants:
            self.course_list[student.id] = student
        else:
            self.wait_list.append(student)
    
    def remove_student(self, id):
        try:
            del self.course_list[id]

            # THIS SHOULD ONLY HAPPEN IF SOMEONE WAS ACTUALLY REMOVED FROM THE COURSE
            if len(self.wait_list) > 0:
                student = self.wait_list.pop(0)
                self.course_list[student.id] = student
        except:
            for student in self.wait_list:
                if student.id == id:
                    self.wait_list.remove(student)


    def get_participant_string(self):
        ordered_list = []
        for id in self.course_list:
            ordered_list.append(self.course_list[id])
        ordered_list.sort()
        ret_str = ""
        for student in ordered_list:
            ret_str += str(student) + "\n"
        return ret_str

    def get_wait_list_string(self):
        ret_str = ""
        for student in self.wait_list:
            ret_str += str(student) + "\n"
        return ret_str


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

    print()
    course.remove_student(654)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    print()
    course.remove_student(176)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())


    print("\n\nSOME EXTRA TEST added after exam\n")

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

    print()
    course.remove_student(12)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    print()
    course.remove_student(000)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    print()
    course.remove_student(654)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())

    print()
    course.remove_student(176)
    print("COURSE PARTICIPANTS:")
    print(course.get_participant_string())
    print("WAIT LIST:")
    print(course.get_wait_list_string())