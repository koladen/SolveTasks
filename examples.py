def example_massiv():
    things = ['mozarella', 'cinderella', 'salmonella']
    things[1] = things[1].capitalize()
    things[0] = things[0].upper()
    # del things[2]
    things.remove('salmonella')
    anotherlist = ['Groucho', 'Chico', 'Harpo']
    anotherlist[2] = anotherlist[2].lower()
    # anotherlist[2] = ("".join(list(anotherlist[2])[::-1])).capitalize()
    anotherlist[2] = anotherlist[2][::-1].capitalize()
    print(anotherlist)
    print(things)


def example_dict():
    e2f = dict(dog='chien', cat='chat')  # {'dog':'chien', 'cat':'chat'}
    f2e = {}
    for key, expr in e2f.items():
        f2e[expr] = key
    life = dict(animals=dict(cats=['Henri', 'Grumpy', 'Lucy'], octopi='octopus', emus=['emu', 'straus']), plants=[],
                others=[])
    print(list(life['animals']['cats']))
    # f2e = e2f.items()
    print(e2f['cat'])
    print(f2e['chien'])
    print(list(e2f.keys()))


def example_vklyuchenie():
    number_list = []
    for i in range(1, 6):
        number_list.append(i)
    number_list2 = list(range(1, 6))
    number_list3 = [number for number in range(1, 6)]
    a_list = [number for number in range(1, 6) if number % 2 == 1]
    rows = range(1, 4)
    cols = range(1, 3)
    cells = [(row, col) for row in rows for col in cols]
    print(cells)
    # print(type(cells[1]))
    # print(cells[4].get(3, 'нету такого'))
    word = 'letters'
    letter_counts = {letter: word.count(letter) for letter in set(word)}
    print(letter_counts)


def answer():
    print(42)


def run_smth(funcname):
    funcname()

def document_it(func):
    def new_function(*args, **kwargs):
        print('Zapuskaem funkciyu: ' + func.__name__)
        print('Pozicionnie argumenti: ', args)
        print('Argumenti slovari: ', kwargs)
        result = func(*args, **kwargs)
        print('Resultat: ', result)
        return result

    return new_function

def square_it(func):
    def newfunc(*args, **kwargs):
        print('popali v kvadrat')
        result = func(*args, **kwargs)
        return result * result
    return newfunc

def sumargs(*args):
    return sum(args)


#@square_it
#@document_it
def addits(a, b):
    return a + b

def run_with_positional_args(funcname, *args):
    return funcname(*args)


def knights(saying):
    def inner2():
        return 'Mi govorim ' + saying + '!!!'

    return inner2


def edit_story(words, funcname):
    for word in words:
        print(funcname(word))


def uvelichivaem(word):
    return word.upper() + '!'


def print_args(*args):
    print('arguments ', args)


def print_kwargs(**kwargs):
    print('argumenti - slovari', kwargs)


def my_range(first=0, last=100, step=1):
    number = first
    while number < last:
        yield number
        number += step




#fdecor = document_it(sumargs)  # Возвращаем новую функцию из декоратора!
#fdecor(1, 2, 7)

ranger = my_range(0, 4)
print(sum(ranger))

a = knights('Utka')
b = knights('Zveryuga')

vosglasi = ['blya', 'suka', 'aaaaa']
# edit_story(vosglasi,uvelichivaem)
edit_story(vosglasi, lambda testp: testp.upper() + '!')

testdict = {'ausver': 3, 'animal': 'los'}

example_massiv()
example_dict()
example_vklyuchenie()
run_smth(answer)
print(run_with_positional_args(sumargs, 1, 2, 3, 4, 5, 6, 7, 8, 8))
print_args(17, 47, 'test', (99, 888))
print_kwargs(a='a', b='b')
print(testdict['animal'])

fdecor = document_it(addits)
fdecor(3, 5)