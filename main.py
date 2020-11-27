# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    рецепты = dict(плов={'рис', 'мясо'}, гуляш={'мясо', 'картошка'}, каша={'рис', 'вода'})
    for блюдо, состав in рецепты.items():
        #if 'мясо' in состав:
        if состав & {'картошка', 'вода'}:
            print('картошка или вода есть в ' + блюдо)
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(name[0:3])
    firstlist = list()
    firstlist = name.split()
    joinedlist = "_".join(firstlist)
    sortedfirstlist = sorted(firstlist)
    secindlist = ["Vtoroi", "Spisoc"]
    inputlist = list(name)
    inputlist.append("Test")
    inputlist.extend(secindlist)
    inputlist.insert(2, "Ehuu!")
    reverseinputlist = inputlist[::-1]
    del reverseinputlist[2]
    reverseinputlist.remove("Ehuu!")
    if 'e' in reverseinputlist:
        print(reverseinputlist.index("e"))
    else:
        print("Netu!")
    tailoflist = reverseinputlist.pop()
    counte = reverseinputlist.count("e")
    exsamplelist = ["1", "2", "rose", "spring"]
    for element in exsamplelist:
        print(element)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(input())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
