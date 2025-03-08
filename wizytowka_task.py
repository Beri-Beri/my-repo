from faker import Faker

class BusinessCard:
    def __init__(self, name, last_name, job_title, company, phone, email)
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
    def card_length(self):
        return len(self.name) + len(self.last_name) + 1
    
class BaseContact(BusinessCard):
    def __init__(self, name, last_name, phone, email):
        super().__init__(name, last_name, company=None, job_title=None, phone=phone, email=email)
    
    def contact(self):
        print(f"Wybieram numer {self.phone} i dzwonię do {self.name} {self.last_name}")
         