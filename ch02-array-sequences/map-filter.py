x = "!@#$%^&&*()A"

# this one is obviously simpler and easy to read,
# but my forst thought of why id want to use map and filter
# insted if list comprehension is that they might be faster but semingly not.

codes = [ord(i) for i in x if ord(i) > 64]

print(codes)

nums = list(filter(lambda c: c > 64, map(ord, x)))
print(nums)
