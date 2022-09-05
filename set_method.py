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

talaba1.set_bosqich(3)
print(talaba1.get_info())