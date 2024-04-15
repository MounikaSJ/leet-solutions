def countStudents(students, sandwiches) -> int:
    j = 0
    while j < len(students):
        if students[0] != sandwiches[0]:
            temp = students[0]
            students.pop(0)
            students.append(temp)
            j+=1
        else:
            sandwiches.pop(0)
            students.pop(0)
            j=0
    return len(students)

students =  [1,1,0,0]
sandwiches = [0,1,0,1]

result = countStudents(students,sandwiches)
print(result)