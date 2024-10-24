from collections import Counter
name = "my name is obulesh"
out = {}
for ele in name:
    if ele in out:
        out[ele] += 1
    else:
        out[ele] = 1
print(f"by using for loop{out}")

#by using the counter
count = 0
print(f"by using the counter this out is {Counter(name)}")