class Student:
    def init(self, first_name, last_name, birth_date):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date

    def display_info(self):
        print(f"Ім'я: {self.first_name}")
        print(f"Прізвище: {self.last_name}")
        print(f"Дата народження: {self.birth_date}")

student1 = Student("Олександр", "Зинченко", "12.03.2010");

student2 = Student("Марія", "Жукова", "22.05.2011");

student1.display_info()
print()
student2.display_info()