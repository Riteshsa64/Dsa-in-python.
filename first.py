for i in range(1, 8):   # 1 to 7
    if i <= 4:
        stars = i
    else:
        stars = 8 - i   # 8-5=3, 8-6=2, 8-7=1

    for j in range(stars):
        print("*", end=" ")
    print()


'''
* 
* * 
* * * 
* * * * 
* * * 
* * 
*
'''

