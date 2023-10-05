def my_sum(hw_list):
    sum = 0
    for hw_grade in hw_list:
        sum += hw_grade
    return sum


hw = [100, 0, 97]
hw.append(98)
hw.append(60)

print("請輸入期中考成績：", end="")
mid = float(input())
final = float(input("請輸入期末考成績："))

avg_hw = my_sum(hw) / len(hw) # 這裡也有改動
grade = (mid * 0.3) + (final * 0.3) + (avg_hw * 0.4)
grade **= 0.5 # 縮寫
grade *= 10 # 縮寫

print(grade)


