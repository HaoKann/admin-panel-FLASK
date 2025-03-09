from app import db
from datetime import datetime

class Employee(db.Model):
    __tablename__ = 'employees'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255))
    date_of_birth = db.Column(db.DateTime(), nullable=False)
    address = db.Column(db.String(255))
    salary = db.Column(db.Integer(), nullable=False)

    def __repr__(self):
        return f'Сотрудник {self.id}, {self.name}, {self.surname}, {self.date_of_birth}, {self.address}, {self.salary}'