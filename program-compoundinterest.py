# Program 4 - Compute the compound interest. The formula of CI is P(1+r/100) raise to t,
# where p is principal amount,
# r is rate of interest, and t is time period.
# Obtain p,r,t from user and find CI.

p=float(input('Enter principal amount:'))
r=float(input('Enter rate of interest:'))
t=float(input('Enter time period:'))

ci = p * ( 1 + r / 100 ) ** t

print('Compound interest\n' 'Principal amount', p, 'interest rate', r, 'time period', t, 'is', ci)