from jinja2 import Template

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
#
# per = Person('Fedor', 33)


per = {'name': 'Fedor', 'age': 34}

tm = Template('Mne {{ p.age }} i zovut {{ p.name }}.')
msg = tm.render(p=per)

print(msg)