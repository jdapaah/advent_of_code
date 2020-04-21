count = 0
for i in range(264360, 746325):
    nums = [int(j) for j in str(i)]

    if nums[0] > nums[1] or nums[1] > nums[2] or nums[2] > nums[3] or nums[3] > nums[4] or nums[4] > nums[5]:
        continue  # numbers must be increasing or flat

    if 2 not in [nums.count(e) for e in range(10)]:
        continue

    count += 1
print(count)
