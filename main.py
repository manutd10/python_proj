class Talaba:
    def __init__(self,ism,familiya,tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich=1
    def get_info(self):
        """Talaba haqida ma''lumot beradigan metod"""
        return f'{self.ism} {self.familiya} {self.bosqich}- bosqich talabasi'

    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich=bosqich
    def update_bosqich(self):
        """Talabaning bosqichini 1 taga ko'paytirish"""
        self.bosqich += 1

talaba1=Talaba("Olim","Olimov",2002)
print(talaba1.get_info())

talaba1.update_bosqich()
print(talaba1.get_info())
talaba1.update_bosqich()
print(talaba1.get_info())
talaba1.update_bosqich()
print(talaba1.get_info())
talaba1.update_bosqich()
print(talaba1.get_info())

# talaba1.set_bosqich(3)
# print(talaba1.get_info())


class Fan:
    def __init__(self,nom):
        self.nom=nom
        self.talabalar_soni=0
        self.talabalar=[]

    def add_student(self,talaba):
        """Fanga talaba qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]

    def see_methods(klass):
            return [method for method in dir(klass) if method.startswith('__') is False]

    print(see_methods(Talaba))
    print((see_methods(talaba1)))

    print(talaba1.__dict__)
    print(talaba1.__dict__.keys())







matem=Fan("Oliy matematika")
talaba1=Talaba("Said" , "Muxtorov",2002)
talaba2=Talaba("Sardor" ," Gulomov",1995)
talaba3=Talaba("Saidaxror"," Abdullayev",1996)

matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)

mat_talabalar=matem.get_students()
print(mat_talabalar)

