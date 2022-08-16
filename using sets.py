s1 = set([1, 2, 3,2,2, 4])
print(s1)
cricketers = {"A", "C"}
footballers = {"B", "C"}
print(cricketers.union(footballers))


a= [1,5,4,2,48,3]
a.sort()
print(a)

a= ["cat","dog","ball","apple"]
a.sort()
a.reverse()
print(a.reverse())

a = ["cat", "dog", "ball", "apple"]
a.sort(key=len)
print(a)
a.sort(key=len, reverse=True)
print(a)

def lastchar(s):
    return s[len(s)-1]
a.sort(key= lastchar(s
                     ))
print(a)