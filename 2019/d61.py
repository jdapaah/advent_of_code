planets = {}


def main():
    with open('/Users/jeremy/AdventOfCode/Input/d6.txt') as file:
        for line in file:
            body, sat = line.strip().split(')')
            planets[sat] = body
    print(sum([orbits(key) for key in planets]))


def orbits(satellite):
    if satellite == 'COM':
        return 0
    else:
        return 1 + orbits(planets[satellite])


if __name__ == '__main__':
    main()
