my_dict={'Name': 'abc', 
         'Age': 23,
'mob': 1234567890,}
print(my_dict)
print(my_dict['Name'])
## update value
my_dict['Name']='xyz'
my_dict['Age']=26
print(my_dict)
## delete key
del my_dict['Name']
print(my_dict)
## search key
print(my_dict.get('mob'))
##update contact number
my_dict['mob']=9876543210
print(my_dict)
job = my_dict.pop('mob')
print(job)
print(my_dict)