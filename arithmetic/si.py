p = int(input("enter the value of princle amount= \n"))
r = int(input("enter the value of interest = \n"))
t = int(input("enter the value of time in yr = \n"))
si = p * r * t / 100
# print(p,r,t, si)
print("SI=", si)
ci = p*(1+r/100)**t-p
print('ci=', ci)

