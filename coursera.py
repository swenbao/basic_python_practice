# template for "Stopwatch: The Game"
import simplegui

# define global variables
tick = 0
tick_or_not = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(tick):
    min = tick // 600
    sec = (tick - min*600) // 10
    decisec = tick % 10
    
    str_min = str(min)
    str_sec = str(sec)
    str_decisec = str(decisec)
    
    if len(str_sec) == 1:
        return str_min + ":" + "0" + str_sec + "." + str_decisec
    else:
        return str_min + ":" + str_sec + "." + str_decisec
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global tick_or_not
    tick_or_not = True
    
def stop():
    global tick_or_not
    tick_or_not = False

def reset():
    global tick, tick_or_not
    tick_or_not = False
    tick = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tick, tick_or_not
    if tick_or_not:
        tick += 1
    
# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(tick), [40, 100], 50, 'WHITE')
    
# create frame
frame = simplegui.create_frame('frame', 200, 200)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.add_button('Start', start)
frame.add_button('Stop', stop)
frame.add_button('Reset', reset)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric
