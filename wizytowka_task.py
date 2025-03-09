from faker import Faker

class BusinessCard:
    def __init__(self, name, last_name, job_title, company, phone, email):
        self.name = name
        self.last_name = last_name
        self.job_title = job_title
        self.company = company
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"{self.name} {self.last_name}, {self.job_title} at {self.company}, Email: {self.email}, Phone: {self.phone}"
    
    def contact(self):
        print(f"Kontaktuję się z {self.name} {self.last_name}, {self.job_title}, Email: {self.email}")

    @property
    def label_length(self):
        return len(self.name) + len(self.last_name) + 1
    
class BaseContact(BusinessCard):
    def __init__(self, name, last_name, phone, email):
        super().__init__(name, last_name, job_title=None, company=None, phone=phone, email=email)
    
    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.last_name}")
         
class BusinessContact(BusinessCard):
    def __init__(self, name, last_name, job_title, company, phone, email, work_phone):
        super().__init__(name, last_name, job_title, company, phone=None, email=None) 
        self.work_phone = work_phone
    
    def contact(self):
        print(f"Wybieram numer służbowy {self.work_phone} i dzwonię do {self.name} {self.last_name}")
