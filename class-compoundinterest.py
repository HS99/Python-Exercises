# Program 6 - Compute the compound interest. The formula of CI is P(1+r/100) raise to t,
# where p is principal amount,
# r is rate of interest, and t is time period.
# Obtain p,r,t from user and find CI.
# Implement using classes.
class computeci:
    def __init__(self):
        self.__p=0.0
        self.__r=0.0
        self.__t=0.0
        self.__ci=0.0

    def set(self):
        self.__p = float(input('Enter principal amount:'))
        self.__r = float(input('Enter rate of interest:'))
        self.__t = float(input('Enter time period:'))

    def computeci(self):
        self.__ci = self.__p * ( 1 + self.__r / 100 ) ** self.__t

    def get(self):
        print('Principal amount', self.__p, 'interest rate', self.__r, 'time', self.__r,
              'compound interest', self.__ci)

def main():
    ci=computeci()
    ci.set()
    ci.computeci()
    ci.get()
if __name__ == '__main__':
    main()