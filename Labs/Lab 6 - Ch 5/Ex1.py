# Write a program that counts how many of the
# squares of the numbers from 1 to 100 end in a 1.

squares = [i*i for i in range(1, 101)]
nums = [i for i in squares if str(i).endswith("1")]
print(f"Squares from 1 to 100 ending in 1: {len(nums)}")
