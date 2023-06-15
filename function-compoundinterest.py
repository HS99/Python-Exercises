# Program 5 - Compute the compound interest. The formula of CI is P(1+r/100) raise to t,
# where p is principal amount,
# r is rate of interest, and t is time period.
# Obtain p,r,t from user and find CI.
# Implement using functions.
def computeci(p,r,t):
    ci = p * ( 1 + r / 100 ) ** t
    return ci
p=float(input('Enter principal amount:'))
r=float(input('Enter rate of interest:'))
t=float(input('Enter time period:'))
i=computeci(p,r,t)
print('Principal amount', p, 'interest rate', r, 'time', t,'compound interest', i)