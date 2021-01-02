planets = dict()


def main():
    with open('Input/d6.txt') as file:
        for line in file:
            body, sat = line.strip().split(')')
            planets[sat] = body
    print(bi_search())


def bi_search():
    link1 = 'YOU'
    link2 = 'SAN'
    chain1 = [link1]
    chain2 = [link2]
    con_set = set()
    while not con_set:  # while intersection is empty
        if link1 != 'COM':  # extend chains until connection
            link1 = planets[link1]
            chain1.append(link1)
        if link2 != 'COM':
            link2 = planets[link2]
            chain2.append(link2)
        con_set = set(chain1) & set(chain2)
    con_set = con_set.pop() # con_set is connection point

    index1 = chain1.index(con_set)  # how far back from 'you' the cpoint is
    index2 = chain2.index(con_set)  # how far back from 'san' the cpoint is
    # reconnect around that index
    if index1 == len(chain1)-1:  # cut chain2
        chain2 = chain2[:index2]
    elif index2 == len(chain2)-1:  # cut chain1
        chain1 = chain1[:index1]

    #  cut out extras in the list that arrived earlier
    return len(chain1) + len(chain2) - 3


if __name__ == '__main__':
    main()
