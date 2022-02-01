def fileread(file):

    with open(file, "r") as f:
        "Reads abd returns"
        f_read = f.readlines()
        
        #replace is not necessary since it strips when turning to an int
        f = [int(i.replace("\n", "")) for i in f_read]
        return f

file1 = fileread("100 days of python\\Day 26\\file1.txt")
file2 = fileread("100 days of python\\Day 26\\file2.txt")

result = [num for num in file1 if num in file2]

print(result)


#instrctor's method
# with open("100 days of python\\Day 26\\file1.txt") as f:
#     file1_data = f.readlines()

# with open("100 days of python\\Day 26\\file2.txt") as f:
#     file2_data = f.readlines()

# result = [int(num) for num in file1_data if num in file2_data]


# print(result)

