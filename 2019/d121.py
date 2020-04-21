from itertools import combinations
n_bodies = 0


def main():
    global n_bodies
    positions = []
    with open('/Users/jeremy/AdventOfCode/Input/d12.txt') as file:
        for line in file:
            array = line.strip().split()
            x = int(array[0][3:-1])
            y = int(array[1][2:-1])
            z = int(array[2][2:-1])
            positions.append([x, y, z])
    n_bodies = len(positions)
    velocities = [[0, 0, 0]] * n_bodies
    for timestep in range(1000):
        positions, velocities = process(positions, velocities)
    total_energy = sum([energy(positions[k]) * energy(velocities[k]) for k in range(n_bodies)])
    print('Total energy for system at step 1000:', total_energy)


def process(pos, vel):
    pairs = combinations(range(n_bodies), 2)
    for i, j in pairs:  # indices
        del_v = a_change(pos[i], pos[j])
        vel[i] = add(vel[i], del_v)
        vel[j] = add(vel[j], del_v, False)
    for i in range(n_bodies):
        pos[i] = add(pos[i], vel[i])

    return pos, vel


def a_change(a, b):
    change = [0] * 3
    for var in range(3):
        t = 0
        if a[var] > b[var]:
            t -= 1
        elif a[var] < b[var]:
            t += 1
        change[var] = t
    return change


def add(l1, l2, a=True):
    if a:
        return [l1[i] + l2[i] for i in range(len(l1))]
    else:
        return [l1[i] - l2[i] for i in range(len(l1))]


def energy(l):
    return sum(abs(k) for k in l)


if __name__ == '__main__':
    main()
