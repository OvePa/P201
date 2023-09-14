class MyParentClass:
    def __init__(self, course, institute):
        self.course = course
        self.institute = institute

    def printname(self):
        print(self.course, self.institute)


class SubClass(MyParentClass):
    def __init__(self, course, institute):
        super().__init__(course, institute)


subclass = SubClass("Python201", "Educative")
subclass.printname()
