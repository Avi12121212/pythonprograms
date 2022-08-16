s1 =set ({1,2,5,6,3})
print(s1)
s2= (2,5,4,7,3,8)
# print(s1,s2)
# print(type (s1))
s1 = s1.union (s2)
# print(s1)
s1.update([4,7,3])
# print(s1)
# ''''''' alphabaticale

football={'v','f'}
cricket= {'v','h'}
h= football.union(cricket)
# print("union",h)


intrs= football.intersection(cricket)
# print('intersection',intrs)


diff= cricket.difference(football)
print("different", diff)

symmt= football.symmetric_difference(cricket)
print('symmt different', symmt)


