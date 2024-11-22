#Nested loops

# for i in range(4):  #nested loops
#     for j in range(3):
#         print(i,j)


# d=["Mon","Tues","Wed"]
# for i in range(len(d)):
#     print(d[i])

# d=["Mon","Tues","Wed"]
# i=0
# while i<len(d):
#     print(i,d[i])

# for i in range(10):
#     if i%2==0:
#         continue
#     if i>8:
#         break
#     print(i)


# m=[[2,3,5],[7,8,9]]
# for i in range(len(m)):
#     print(m[i])


m=[[1,2,3],[7,8,9]]
for i in range(len(m)):
    for j in range(len(m[0])):
        print(m[i][j])
