

class MarsStudent:
    def __init__(self, student_id, password, first_name, last_name, age, coin=0):
        self.student_id = student_id
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.coin = coin

    def full_data(self, input_id, input_password):
        if input_id == self.student_id and input_password == self.password:
            print(f"Ism: {self.first_name}, Familiya: {self.last_name}, Yosh: {self.age}, Koin: {self.coin}")
        else:
            print("Noto'g'ri ID yoki parol.")

    def get_coin(self):

        return self.coin

    def set_coin(self, amount):
        self.coin += amount
        print(f"Koinlar soni: {self.coin}")


student = MarsStudent("s001", "password123", "John", "Doe", 20, 10)

student.full_data("s001", "password123")


print(f"Student koinlar soni: {student.get_coin()}")

student.set_coin(5)  

