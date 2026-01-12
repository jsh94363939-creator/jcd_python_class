def qe (a,b,c):
    d=(-b+(b**2-4*a*c)**0.5)/(2*a)
    e=(-b-(b**2-4*a*c)**0.5)/(2*a)
    return d


print(qe(1,2,-8)*2)