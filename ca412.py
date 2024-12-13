# i = 1
# while i <= 4:  # Loop for rows
#     j = 1
#     while j <= 7:  # Loop for columns
#         if 4 - i + 1 <= j <= 4 + i - 1:  # Range for '*'
#             print('*', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()  # Move to the next line
#     i += 1
i = 4
while i >= 1:  # Loop for rows
    j = 7
    while j >=1:  # Loop for columns
        if 4+i-1 >=j>= 4 - i+ 1:  # Range for '*'
            print('*', end='')
        else:
            print('-', end='')
        j -= 1
    print()  # Move to the next line
    i -= 1
