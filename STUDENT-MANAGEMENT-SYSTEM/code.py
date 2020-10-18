# --------------
class_1 = [ 'Geoffrey hinton', 'Andrew Ng', 'Sebastian Raschka', 'Yoshua Bengio']
class_2 = [ 'Hilary Mason', 'Carla Gentry', 'Corinna Cortes']
new_class = class_1 + class_2
print(new_class)
new_class.append('Peter Warden')
print(new_class)
new_class.remove('Carla Gentry')
print(new_class)
courses = {'Math' : 65, 'English' : 70, 'History' : 80, 'French' : 70, 'Science' : 60}
print(courses)
math = courses['Math']
english = courses['English']
history = courses['History']
french = courses['French']
science = courses['Science']
total = math + english + history + french + science
print(total)
percentage = (total)*100/500
print(percentage)
mathematics = { 'Geoffrey hinton':78, 'Andrew Ng':95,
'Sebastian Raschka':65, 'Yoshua Benjio': 50, 'Hilary Mason':70, 
'Corinna Cortes':66, 'Pter Warden':75}
topper = max(mathematics,key=mathematics.get)
print(topper)
print(topper.split()[0:2])
last_name = 'NG'
first_name = 'ANDREW'
full_name = last_name + " " + first_name
certificate_name = full_name
print(certificate_name)



