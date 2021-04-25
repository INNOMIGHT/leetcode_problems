def grade_calc(grade):

    if grade > 38:
        rem_grade = grade % 5
        if rem_grade > 2:
            grade = grade + 5 - rem_grade
        else:
            grade = grade

    return grade


print(grade_calc(73))
