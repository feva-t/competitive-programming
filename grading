def Grading(grades):
    Final_Grades=[]
    for a_Grade in grades:
        if a_Grade>= 0 and a_Grade<=100 :
            if ((a_Grade//5 + 1)*5 - a_Grade) < 3 and a_Grade>=38:
                Final_Grades.append((a_Grade//5+1)*5)
            elif ((a_Grade//5 + 1)*5 - a_Grade) >= 3 or a_Grade<=38:
                Final_Grades.append(a_Grade)
        else:
            continue
    return Final_Grades
