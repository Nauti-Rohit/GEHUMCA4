def test(dict, key, value):
   if any(sub[key] == value for sub in dict):
       return True
   return False

emp = [{'employee_id': 10110, 'name': 'James Parkes', 'Dept': 'IT'},
      {'employee_id':  10111, 'name': 'Lisa Hayden', 'Dept': 'Accounts'}, 
      {'employee_id': 10113, 'name': 'Brian Adam', 'Dept': 'HR'},
      {'employee_id': 10114, 'name': 'Rine Arthur', 'Dept': 'Accounts'}, 
      {'employee_id': 10115, 'name': 'Jeff Simson', 'Dept': 'HR'}
      ]
print("\nOriginal dictionary:")
print(emp)
print("\nCheck if a specific Key and a value exist in the said dictionary:")
print(test(emp,'employee_id', 10114))
print(test(emp,'name', 'Brian Adam'))
print(test(emp,'Dept', 'Accounts'))
print(test(emp,'Dept', 'Computer'))
print(test(emp,'name', 'Liza Simson'))
print(test(emp,'employee_id', 10112))