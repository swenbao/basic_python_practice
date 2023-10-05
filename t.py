import time

time.sleep(0.5)
print("叮咚！歡迎光臨全聯福利中心！！")
time.sleep(1)
print("你跨過了自動門，冷風彿過你的四肢，突如其來的溫差使你忍不住發抖。")
time.sleep(1)
print("你環顧四周，發現全聯福利中心的燈光暗淡，顯得有些詭異", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".")

print("""------

你要:
1) 乾！太可怕惹！逃走！
2) 進去啊！怕屁怕！

------
""")

selection = input()
print(selection)