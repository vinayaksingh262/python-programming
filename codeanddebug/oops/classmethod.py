class Employee:
    company = "google"

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name


print(Employee.company)
Employee.change_company("microsoft")
print(Employee.company)
