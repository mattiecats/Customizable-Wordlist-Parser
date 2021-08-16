import re

def individualy():
    f = open('disneymovielist.txt', 'r')
    individual = []
    individual = f.read().split()
    return individual
    # makes every word in the wordlist singular

def addfront(mainlist):
    front = ['1990' + s for s in mainlist]
    return front
    # adds 1990 to the front of wordlist using a loop


def addrear(mainlist):
    front = [s + '1990' for s in mainlist]
    return front
    # adds 1990 to the end of wordlist using a loop


def removechar(mainlist):
    # removes characters (,./<>? etc...)
    char = [re.sub("[:,&'\-() 0-9]","",s) for s in mainlist]
    return char

def main():
    # input word file and output word file
    f = open('disneymovielist.txt', 'r')
    mainlist = []
    chardupe = []
    mainlist = [line.rstrip() for line in f]
    char = removechar(mainlist)

    #print(addrear(removechar(mainlist)))
    #print(addfront(removechar(mainlist)))
    #print(addfront(individualy()))
    #print(addrear(individualy()))

    list1 = addrear(removechar(mainlist))
    list2 = addfront(removechar(mainlist))
    list3 = addfront(removechar(individualy()))
    list4 = addrear(removechar(individualy())) #combines list

    final_list = list1 + list2 + list3 + list4
    
    for i in range(len(final_list)):
        final_list[i] = final_list[i].lower()
    print(final_list) #lowercase parser

    with open('output.txt', 'w+') as output:
        for items in final_list:
            output.write('%s\n' % items)
    output.close() #writes to file


if __name__ == '__main__': main()
