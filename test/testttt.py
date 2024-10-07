#aaa

aaaa = {
  'S' : [['A',3],['B',6],['C',2]],
  'C' : [['S',2],['E',1]],
  'A' : [['D',3], ['S',3]],
  'B' : [['D',4],['G',9],['E',2],['S',6]],
  'D' : [['A',3],['B',4],['F',5]],
  'E' : [['F',6],['H',5],['C',1],['B',2]],
  'F' : [['G',5],['E',6],['D',5]],
  'G' : [['F',5],['B',9],['H',8]],
  'H' : [['E',5],['G',8]]
}



def Sort_List_Of_List(put_Val):
    lengthOfBasic = len(put_Val)
    print(lengthOfBasic)
    for iterrr in range(0, lengthOfBasic):
        print(iterrr)    
    #     for iterrr2 in range(0, lengthOfBasic-iterrr-1):
    #         if (put_Val[iterrr2][1] > put_Val[iterrr2 + 1][1]):
    #             temporaryyyy = put_Val[iterrr2]
    #             put_Val[iterrr2]= put_Val[iterrr2 + 1]
    #             put_Val[iterrr2 + 1]= temporaryyyy
    # return put_Val





# vvv = [['A', 3], ['B', 6], ['C', 2]]
# v2 = Sort_List_Of_List(vvv)
# print(v2)

# def bfs(aaaa, start_point):
#     valll = []
#     final_list = [] 
#     final_list.append(start_point)
#     for i in range(len(aaaa)):
#         if( start_point == list(aaaa.keys())[i]):
#             # print(i)
#             eleeee = len(list(aaaa.values())[i])
#             # print(list(aaaa.values())[i])
#             # A = list(aaaa.values())[i]
#             # A = Sort_List_Of_List(A)
#             # print(A)
#             d222 = list(aaaa.values())[i]
#             print(d222[0][1])

# bfs(aaaa,'B')



















# abc = [[1,2],[2,4],[4,2],[5,5],[6,5],[4,7],[7,8]]


# for i in range(len(abc)):
#     for j in range(2):
#         # print(i)
#         print(j)
#         # print(abc[i][j])

