students = [
    {
        "firstName":"tavish",
        "lastName":"anade",
        "age":20,
        "city":"nagpur",
        "skills":["python","html","css"]
    },
    {
        "firstName":"sarika",
        "lastName":"pansare",
        "age":22,
        "city":"mumbai",
        "skills":["djnago","tosca","css","javascript"]
    },
    {
        "firstName":"amol",
        "lastName":"rao",
        "age":23,
        "city":"nagpur",
        "skills":["sql","powerBI"]
    }
]


#program 1
#name:number of skills

for student in students:
    print(student['firstName'],len(student['skills']))


#program 2
#name of person leaving in pune
for student in students:
    if(student['city'] == "pune"):
        print(student['firstName'])


#program 3
#add a property
# institute:minskole

for student in students:
    student.update({"institute":"minskole"})
print(students)



# program 4
#add the skill of every user -"promt engineering"
for student in students:
    student['skills'].append("promt enginnering")
print(students)


#program 5
# average age of all students
total=0
for student in students:
    total=total+student['age']
print(total/len(students))

#program 6
# name of a person with python skills
for student in students:
    if "python" in student['skills']:
        print(student['firstName'])
