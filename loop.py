while True:
    x = int(input("輸入數字:"))
    for b in range(1, x+1):
        if b == 1:
            print(" "*(x-1) + "x")
        else:
            spaces = " " * (x - b) 
            blocks = "x" + "o" * (b * 2 - 3) + "x" #2x- 1 > 1 3 5 7 9
            print(spaces + blocks)
