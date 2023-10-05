# https://py2.codeskulptor.org/#user50_6alWnuLWY1pipwH.py
# implementation of card game - Memory

import simplegui
import random

CARD_NUM = 16
NO_EXPOSED = 0
ONE_EXPOSED = 1
TWO_EXPOSED = 2
turns = 0

# helper function to initialize globals
def new_game():
    global game_list, visible, card_pos, state, turns
    turns = 0
    state = NO_EXPOSED
    game_list = list(range(0, 8)) + list(range(0, 8))
    random.shuffle(game_list)
    visible = [False for _ in range(16)]
    card_pos = list(range(0, 801, 50))
    label.set_text("Turns = " + str(turns))
    
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global visible, turns, card_pos, state, first_card, second_card
    for i in range(16):
        if card_pos[i] < pos[0] and pos[0] < card_pos[i+1] and not visible[i]:
            visible[i] = True
            if state == NO_EXPOSED:
                state = ONE_EXPOSED
                first_card = (game_list[i], i) 
                turns += 1
            elif state == ONE_EXPOSED:
                state = TWO_EXPOSED
                second_card = (game_list[i], i)
            else:
                if first_card[0] != second_card[0]:
                    visible[first_card[1]] = False
                    visible[second_card[1]] = False
                first_card = (game_list[i], i) 
                state = ONE_EXPOSED
                turns += 1
                
    label.set_text("Turns = " + str(turns))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    pos = 0
    for i in range(16):
        if visible[i]:
            canvas.draw_text(str(game_list[i]), [pos+22, 50], 20, 'White')
        else:
            canvas.draw_polygon([(pos, 0), (pos, 100), (pos+50, 100), ((pos+50, 0))]
                                , 3, 'Blue', 'Green')
        pos += 50


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric