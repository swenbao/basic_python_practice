def sum_int(hw_list):
    sum = 0
    for hw_grade in hw_list:
        if type(hw_grade) == int:
            sum += hw_grade
    return sum

def sum_float(hw_list):
    sum = 0
    for hw_grade in hw_list:
        if type(hw_grade) == float:
            sum += hw_grade
    return sum

