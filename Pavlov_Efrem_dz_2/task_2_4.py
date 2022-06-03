employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
for employee in employees:
    employee_name = employee.strip().split()[-1].title()
    print(f'Привет, {employee_name}')
