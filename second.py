'''  *
  * *
 * * *
* * * *'''
# for i in range(1, 5):
#     # spaces
#     for j in range(4 - i):
#         print(" ", end="")

#     # stars
#     for j in range(i):
#         print("*", end=" ")

#     print()         

for i in range(4, 0, -1):   # 4 → 1
    for j in range(4-i):
        print("", end=" ")

    for j in range(i):
        print("*", end=" ")

    print()         
 