class StudentList:
    def __init__(self):
        self.__list = []
    def append(self, 학생):
        self.__list.append(학생)
    def print(self):
        for student in self.__list:
            print(student.sum())