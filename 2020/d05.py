# def loc(i):
#     row_low = 0
#     row_high = 127
#     col_low = 0
#     col_high = 7
#     r = 0
#     cls = 0
#
#     for ind, cls in enumerate(i):
#         if cls == 'F':
#             row_high -= (row_high - row_low + 1) // 2
#         elif cls == 'B':
#             row_low += (row_high - row_low + 1) // 2
#         elif cls == 'L':
#             col_high -= (col_high - col_low + 1) // 2
#         elif cls == 'R':
#             col_low += (col_high - col_low + 1) // 2
#         if ind == 6:
#             r = {'F': row_low, 'B': row_high}[cls]
#         if ind == 9:
#             cls = {'L': col_low, 'R': col_high}[cls]
#     return r * 8 + cls


ids = [int(i.replace('B', '1').replace('F', '0')
           .replace('R', '1').replace('L', '0'), 2)
       for i in open("Input/d5.txt").read().split()]
print(max(ids))

s = sorted(ids)
for i in range(1, len(s)):
    if s[i] - s[i - 1] == 2:
        print(i + s[0])
