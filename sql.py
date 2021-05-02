import os
# add to my environment variables to fix sqlite3 DDL error
os.environ["CONDA_DLL_SEARCH_MODIFICATION_ENABLE"] = "1"

import sqlite3 as sl
from employee import Employee

# create a connection object which will be representing our db

# in-memory db that relies primarily on memory for data storage
#conn = sl.connect(':memory:') 
conn  = sl.connect('employee.db')

# create a curson to execute some sql commands
c = conn.cursor()

# create employee table

q_create_table = """
                    CREATE TABLE employees (
                        first text,
                        last text,
                        pay real
                    )
                """

# c.execute(q_create_table)


q_insert2table = """
                    INSERT INTO employees VALUES (
                        'Ola', 'Marko', 70000
                    )
                """
#c.execute(q_insert2table)

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp.first, 'last': emp.last, 'pay': emp.pay})

def get_emps_by_name(lastname):
    with conn:
        c.execute("SELECT * FROM employees WHERE last=:last", {'last':lastname})
        return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees
                    SET pay = :pay
                    WHERE first = :first AND last = :last""", 
                    {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})



emp1 = Employee('Donald', 'Trump', 15_000)
emp2 = Employee('Vladimir', 'Putin', 20_000)
emp3 = Employee('Angela', 'Merkel', 40_000)
emp4 = Employee('Donald', 'Tusk', 45_000)

# Insert values to the table (two ways) to avoid sql injections
# c.execute("INSERT INTO employees VALUES (?, ?, ?)", (emp1.first, emp1.last, emp1.pay))

# c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {'first': emp2.first, 'last': emp2.last, 'pay': emp2.pay})

# print(c.fetchall())


marko = get_emps_by_name('Marko')
print(marko)

update_pay(emp2, 25_000)
print('emp2 updated', emp2)

remove_emp(emp1)
print('emp1: ', emp1)

insert_emp(emp4)
print(emp4)

conn.close()