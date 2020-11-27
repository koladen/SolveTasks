print([number for number in range(1, 11) if number % 2 == 1])
squares = {number:(number*number) for number in range(1,11)}
print(squares)
odd = {number for number in range(1, 11) if number % 2 == 0 }
print(odd)
print(set(squares))
print(odd&set(squares))
gen = (number for number in range(1,11))
for i in gen:
    print('Got', i)

def good():
    return ['Harry', 'Ron', 'Hermiona']

print(good())

def get_odds(start=1, finish=10, step=1):
    iterator = start
    while iterator<=finish:
        if iterator % 2 == 0:
            yield iterator
        iterator+=step
#n=0
for ind, znach in enumerate(get_odds(1, 10), 1):

    #print(n)
    if ind == 3:
        print(znach)
    #n = n + 1


def decor(func):
    def newf(*args):
        print('func ', func.__name__, ' start')
        result = func(*args)
        print('func stop')
        return result
    return newf
@decor
def summa(*args):
    return sum(args)

#fdecor = print(decor(summa)(1,2,7))
print(summa(1,3,7))


titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nunturns into a monster', 'A haunted yarn shop']
#for i,j in zip(titles,plots):
#    ddict[i] = j
ddict = dict(zip(titles,plots))
print(ddict['Creature of Habit'])