import time

def print_slowly(text):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            print(line, end="")
        else:
            print(line)
        time.sleep(1)

def mystery_dots():
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(0.5)
    print(".", end="")
    time.sleep(1)
    
weapens = []
HP = 10

time.sleep(1)
text="""叮咚！歡迎光臨全聯福利中心！！
你跨過了自動門，冷風彿過你的四肢，突如其來的溫差使你忍不住發抖。
你環顧四周，發現全聯福利中心的燈光暗淡，顯得有些詭異
"""

print_slowly(text)
mystery_dots()

while True :
    selection = input("""

------

你要:
1) 乾！太可怕惹！逃走！
2) 進去啊！怕屁怕！

------

""")

    if selection == "1":
        print("廢物！掰掰！")
        exit()
    elif selection == "2":
        break
    else :
        print("你在供三小...\n")
        selection
        continue

print("""
你開始在貨架之間漫步，試圖找到你需要的物品。
當你走近冷凍區時，你發現其中有一個冰箱的燈特別亮
閃閃發亮的光芒似乎在向你招手...
""")

while True :
    selection = input("""------

你要:
1) 乾！太詭異惹！不管！
2) 拿起來

------

""")

    if selection == "1":
        print("泥還是拒絕碰它，並快步走向你要買的東西，買完就走人了")
        exit()
    elif selection == "2":
        break
    else :
        print("你在供三小...\n")
        continue

print("""
你感到一股神秘的力量吸引著你，讓你無法抗拒。
你打開冰箱，發現裡面有一個看似普通的盒子，上面刻著古老的符號。
你將盒子拿起來，突然感到一股強烈的能量衝擊你的身體...
""")

print("""
-----------------------------------------------------
| HP : 10                                           |
| 武器 :                                            |
| 特殊技能 : 變異的螃蟹 (尷尬到使敵人後退無法攻擊） |
| 按 d 可查看系統面板                               |
-----------------------------------------------------
""")

print("""
我的眼前怎麼出現這個神奇的面板
正當你還沒從震驚中回過神來。
一陣低吼聲在你的身後傳來，你轉身一看，發現一只巨大的怪物正在向你衝來。
你嚇得心跳加速，手中的盒子差點掉落在地。你拔腿就跑，嘗試尋找遮蔽物以躲避怪物的攻擊。
你在超市中穿梭奔跑，繞過各種商品，努力避免怪物的攻擊。
就在你以為自己無法逃脫時，你突然想起手中的盒子...
""")

while True :
    selection = str(input("""------

你要:
1) 塊陶啊！！
2) 打開盒子

------

"""))

    if selection == "1":
        print("泥被怪物追上 死惹")
        exit()
    elif selection == "2":
        break
    elif selection == "d":
        print("""
-----------------------------------------------------
| HP : 10                                           |
| 武器 :                                            |
| 特殊技能 : 變異的螃蟹 (尷尬到使敵人後退無法攻擊） |
| 按 d 可查看系統面板                               |
-----------------------------------------------------
""")
    else :
        print("你在供三小...\n")
        selection
        continue

print("""
系統顯示泥獲得新武器：Dior Sauvage！！
""")
weapens+=["Dior Sauvage"]


# 武器：雙頭鷹綠色寶石西裝胸針 潘海利根-雄鹿
# 要有系統面板 寫成 function
# 如果要有那種打字的感覺，要寫一個傳入 str 的 funciton，然後一個字一個字 delay

