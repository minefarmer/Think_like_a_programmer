'''
marks = []
marksOfRich = [55, 67, 78, 66, 89]
MarksofJohn = [43, 76, 54, 87, 90]
MarksofMaria = [77, 65, 76, 87, 65]
MarksofAhmed = [65, 76, 87, 55, 77]
MarksofMax = [65, 98, 45, 65, 88]
marks.append(marksOfRich)
marks
[[55, 67, 78, 66, 89]]
marks.append(MarksofMaria)
marks.append(MarksofMaria)
marks.append(MarksofAhmed)
marks
[[55, 67, 78, 66, 89], [77, 65, 76, 87, 65], [77, 65, 76, 87, 65], [65, 76, 87, 55, 77]]
marks[0]
[55, 67, 78, 66, 89]
marks[2][1]
65
marks[1][3]
87
marks[1][3] = 100
marks[1][3]
100


matrix = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]

for i in matrix:
    print(i)

    
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]


'''