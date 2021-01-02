from itertools import combinations

n_bodies = 0
visited = set()


def main():
    global n_bodies, visited
    positions = []
    with open('Input/d12.txt') as file:
        for line in file:
            array = line.strip().split()
            x = int(array[0][3:-1])
            y = int(array[1][2:-1])
            z = int(array[2][2:-1])
            positions.append([x, y, z])
    n_bodies = len(positions)
    velocities = [[0, 0, 0]] * n_bodies

    op = positions.copy()
    xcount, ycount, zcount = 0, 0, 0
    xcont, ycont, zcont = True, True, True

    while xcont or ycont or zcont:
        positions, velocities = process(positions, velocities)
        xcount += xcont
        ycount += ycont
        zcount += zcont

        xs = [k[0] for k in positions]
        ys = [k[1] for k in positions]
        zs = [k[2] for k in positions]

        if xs == [k[0] for k in op] and [k[0] for k in velocities] == [0] * n_bodies and xcont:
            print('x done', xcount)
            xcont = False
        if ys == [k[1] for k in op] and [k[1] for k in velocities] == [0] * n_bodies and ycont:
            print('y done', ycount)
            ycont = False
        if zs == [k[2] for k in op] and [k[2] for k in velocities] == [0] * n_bodies and zcont:
            print('z done', zcount)
            zcont = False

    print('LCM:', lcm([xcount, ycount, zcount]))


def lcm(nums):
    final_factors = []

    temp_factors = factors(nums)
    while 2 * len(nums) != len(temp_factors):
        most_common = get_largest(temp_factors)  # most common, largest
        final_factors.append(most_common)
        for i, n in enumerate(nums):
            if n // most_common == n / most_common:
                nums[i] = n // most_common
        temp_factors = factors(nums)

    nums.extend(final_factors)
    final = 1
    for k in nums:
        final *= k
    return final


def get_largest(longlist):
    longlist = [i for i in longlist if i != 1]  # remove 1s
    counter, num = 1, longlist[0]
    for i in longlist:
        curr_frequency = longlist.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
        if curr_frequency == counter:
            num = max(num, i)
    return num


def factors(ks):
    f = []
    for k in ks:
        f.extend(j for j in range(1, k + 1) if k / j == k // j)
        if k == 1:
            f.append(1)
    return f


def process(pos, vel):
    pairs = combinations(range(n_bodies), 2)
    for i, j in pairs:  # indices
        del_v = change(pos[i], pos[j])
        vel[i] = add(vel[i], del_v)
        vel[j] = add(vel[j], del_v, False)
    for i in range(n_bodies):
        pos[i] = add(pos[i], vel[i])

    return pos, vel


def change(a, b):
    pull = [0] * 3
    for var in range(3):
        t = 0
        if a[var] > b[var]:
            t = -1
        elif a[var] < b[var]:
            t = 1
        pull[var] = t
    return pull


def add(l1, l2, a=True):
    if a:
        return [l1[i] + l2[i] for i in range(len(l1))]
    else:
        return [l1[i] - l2[i] for i in range(len(l1))]


if __name__ == '__main__':
    main()
