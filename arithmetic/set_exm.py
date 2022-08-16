a = {'c', 'c++', 'java'}
b = {'c++', 'java', 'python'}
c = {'java', 'python', 'c', 'pascal'}

A = a.intersection(b).intersection(c)
print("Known to all ", A)

# difference
B = a.difference(b)
print('a knows but not b', B)

# only known to one student
allsub = a.union(b).union(c)
print("all ", allsub)

C = allsub.difference(a).difference(b)
print(' only one subject known by one student', C)
cstudents = set()
if "c" in a:
    cstudents.add("a")
if "c" in b:
    cstudents.add("b")
if "c" in c:
    cstudents.add("c")
print(cstudents)

pythonstudent = set()
if 'python' in a:
    pythonstudent.add('a')
if 'python' in b:
    pythonstudent.add('b')
if 'python' in c:
    pythonstudent.add('c')
print(pythonstudent)
