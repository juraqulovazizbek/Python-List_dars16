nums = [1, 2, 2, 3, 4, 1, 5, 6, 3, 7]
elements = []

for i in nums:
    if nums.count(i) == 1:
        elements.append(i)

print(elements)
