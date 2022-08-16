def si_ci(p,r,t):
    si= (p*r*t)/100
    ci= p*(1+r/100)**t -p
    return si,ci


print(si_ci(1000,5,2))

