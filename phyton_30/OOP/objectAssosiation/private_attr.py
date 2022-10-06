class Student():

    def __init__(self, id):
        self.__id = id
    
    def get_id(self):
        return self.__id

s1 = Student(12345)
print(s1.get_id())
        