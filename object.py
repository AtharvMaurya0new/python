class Average:
    def __init__(self,chem,math,bio):
        self.chem1=chem
        self.math1=math
        self.bio1=bio
    def calculation(self):
        avg=(self.chem1 +self.math1+self.bio1)/3
        return avg
s1=Average(44,88,66) #yiu can also take 44 66 88 as the lift and store to the variable
print(s1.calculation())   
