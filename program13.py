class person:
    count=0
    def __init__(self,name,age,collegename):
        self.name=name
        self.age=age
        self.collegename=collegename
        person.count+=1
person1=person("Hema",25,"AWEC")
person2=person("Priya",30,"AWEC")
print(person.count)
print(person1.name)
print(person2.age)
print(person1.collegename)