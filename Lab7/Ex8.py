'''
At a certain school, student email addresses end with
@student.college.edu, while professor email addresses
end with @prof.college.edu. Write a program that first
asks the user how many email addresses they will be 
entering, and then has the user enter those addresses.
After all the email addresses are entered, the program
should print out a message indicating either that all
the addresses are student addresses or that there were
some profes-sor addresses entered.
'''
num = int(input("Number of email addresses: "))
allStudent = True
for i in range(0, num):
    if(input(f"Enter email {i+1}: ").endswith("@prof.college.edu")):
        allStudent = False
print("All student" if allStudent else "Some professors")
