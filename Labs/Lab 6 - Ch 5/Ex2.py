# Write a program that counts how many of the squares of the
# numbers from 1 to 100 end in a 4 and how many end in a 9.

squares = [i*i for i in range(1, 101)]
numsEndingIn4 = [i for i in squares if str(i).endswith("4")]
numsEndingIn9 = [i for i in squares if str(i).endswith("9")]
print(f"Squares from 1 to 100 ending in 4: {len(numsEndingIn4)}")
print(f"Squares from 1 to 100 ending in 9: {len(numsEndingIn9)}")
