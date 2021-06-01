class Employee:
    """A sample of employee class"""

    def __init__(self, first, last, pay):
        from datetime import date
        self.first = first
        self.last = last
        self.pay = pay
        self.created = date.today()

    @property
    def email(self):
        return f'{self.first}.{self.last}@email.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', '{self.pay})"
        