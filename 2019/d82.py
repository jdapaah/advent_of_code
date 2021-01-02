def main():
    with open('/Users/jeremy/AdventOfCode/Input/d8.txt') as file:
        full_pic = file.readline().strip()
    image = []
    for pixel in [full_pic[i::150] for i in range(150)]:
        z_ind = pixel.index('0') if '0' in pixel else 101
        o_ind = pixel.index('1') if '1' in pixel else 101
        image.append(pixel[min(z_ind, o_ind)])
    show(image)


def show(pixels):
	c = 0
	for i in range(6):
		for j in range(25):
			print({'0':'X', '1':' '}[pixels[c]], end='')
			c+=1
		print()


if __name__ == '__main__':
    main()
