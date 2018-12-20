#why do we need self? 
def selfDividingNumbers(self, left, right):
    def self_dividing(n):
        for d in str(n):
            if d == '0' or n % int(d) > 0:
                print('d',d)
                return False
        return True     
    ans = []
    for n in range(left, right + 1):
        print('n',n)
        print('left',left)
        print('right+1',right+1)
        if self_dividing(n):
            ans.append(n)
    return ans

print('test')
print(selfDividingNumbers(3,1,22))