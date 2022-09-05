class Fan:
    def __init__(self,nom):
        self.nom=nom
        self.talabalar_soni=0
        self.talabalar=[]

    def add_student(self,talaba):
        """Fanga talaba qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_name(self):
        """Fan nomi"""
        return self.nom

    def get_students(self):
            return [talaba.get_info() for talaba in self.talabalar]

    def get_students_num(self):
        """Fanga yozilgan talabalar soni"""
        return self.talabalar_soni



# These codes are got from sariq dev's page. But done by my side
    def delete_student(self, talaba):
        self.talabalar.remove(talaba)
        self.talabalar_soni += 1
