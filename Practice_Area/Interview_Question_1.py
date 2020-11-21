# float calculateTaxes(income, brackets)# where "brackets" is a list of pairs, e.g.# [
# [5000, 0],
# [10000, 0.1],
# [20000, 0.2],
# [10000, 0.3],
# [null, 0.4],
# ]# This indicates that:# The first $5K is untaxed
# The next $10K is taxed at 10%
# The next $20K is taxed at 20%
# The next $10K is taxed at 30%
# All income above this is taxed at 40%# So, for an income of $55K, the tax would be $0K + $1K + $4K + $3K + $4K = $12K.# 55000 = 
#     5000 = 0
#     10000 = 1000
#     20000 = 4000
#     10000 = 3000
#     10000 = 4000

def calculateTaxes(income, brackets):
    tot_tax = 0
    for i in brackets:
        if i[0] != 'null':
            income = income - i[0]
            if income >= 0:
                tot_tax += (i[1]*i[0])
        else:
            tot_tax += i[1]*income    
            return tot_tax

