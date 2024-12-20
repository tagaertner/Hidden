# each tuple has diff len
# need to take into account the numbs. 
# iterate over the rows 
# create a str  containg every "n " rom iteration
# if n > 100 retun first letter and if n == 1 retrun all
#
#   Do I need to know the positions of numbers? no
#   Do I need to compare numbers with each other? ys
#   Do I just need to check the values?''yes
# edge case if n < 0:
# raise ValueERror
#  create empty list all_chars = []
# regual for each char  in maxtric
#           for each char in row:
#               add. char to all_char
#   create empty result string
# for position from 0 to length of all_chars:
#     if position + 1 is divisible by n:
#         add character at position to result   
def hidden(matrix, n):
    # Your implementation here!
    if n <= 0:
        raise ValueError("n must be a positive integer")
    
    all_char = []
    
    for row in matrix:
        for char in row:
            all_char.append(char)
            
    result =  ""
    for position in range(len(all_char)):
        if position % n == 0:
            
            result += all_char[position]
    return result
    

matrix_1 = (
    ('u','e','r','e', ' ', 'e'),
    ('d', 'z', 'o', 'b', 'i', 'v'),
    ('n',),
    ('w', 'g', 'q', ' ', '5', 'g', 'w'),
    ('r',),
    ('y', 'e'),
    ('u', 'a', 'u', 't')
)
assert hidden(matrix_1, 2) == 'ur doing great'
assert hidden(matrix_1, 3) == 'uedbnqgya'
assert hidden(matrix_1, 525600) == 'u'
assert hidden(matrix_1, 1) == 'uere edzobivnwgq 5gwryeuaut'

matrix_2 = (
    ('💜',),
)
assert hidden(matrix_2, 17) == '💜'
assert hidden(matrix_2, 1) == '💜'

print("All tests passed! Discuss time and space complexity if time remains!")

