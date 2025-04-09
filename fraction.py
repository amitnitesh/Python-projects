class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d

    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    def __add__(self,other):
        num=self.num*other.den+self.den*other.num
        den=self.den*other.den
        return "{}/{}".format(num,den)
    def __sub__(self,other):
        num = self.num * other.den -self.den * other.num
        den = self.den * other.den
        return "{}/{}".format(num, den)

    def __mul__(self,other):
        num=self.num*other.den
        den=self.den*other.den
        return "{}/{}".format(num,den)

    def __truediv__(self, other):
        num=self.num*other.den
        den=self.den*other.num
        return "{}/{}".format(num,den)
