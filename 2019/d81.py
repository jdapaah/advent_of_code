def main():
    with open('/Users/jeremy/AdventOfCode/Input/d8.txt') as file:
        full_pic = [int(num) for num in file.readline().strip()]
    layers = [full_pic[150 * i: 150 * (i + 1)] for i in range(len(full_pic) // 150)]

    test_layer = min(layers, key=lambda single: single.count(0))
    print(test_layer.count(1) * test_layer.count(2))


if __name__ == '__main__':
    main()
