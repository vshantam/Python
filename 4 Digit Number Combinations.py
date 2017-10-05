# ALL the combinations of 4 digit combo
class combinations(object):
    def __init__(self,numbers=[]):
        self.numbers=numbers
    @classmethod
    def FourDigitCombinations(self):
        numbers=[]
        for code in range(10000):
            code=str(code).zfill(4)
            print code,
            numbers.append(code)
        return numbers
if __name__=='__main__':
    obj=combinations()
    res=obj.FourDigitCombination()
    #Displaying all the combinations
    for i in numbers:
        print i ,
  
