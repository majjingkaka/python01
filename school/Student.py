class Student():

    name = '홍길동'
    age = 0

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def console(self, title):
        print('제목',title)
        print('이름',self.name)
        print('나이',self.age)



    
