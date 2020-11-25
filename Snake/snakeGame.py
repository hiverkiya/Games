import random  #
import curses

s = curses.initscr()  # To initialize the screen
curses.curs_set(0)  # So that cursor doesn't show up on screen
sh, sw = s.getmaxyx()  # getting screen height and width
w = curses.newwin(sh, sw, 0, 0)  # New window from left of screen
w.keypad((1))  # Enable to accept keypad input
w.timeout(100)  # 100 ms timeout of screen

snk_x = sw / 4  # Snake's initial position
snk_y = sh / 2
# Making snake's body
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x - 1],
    [snk_y, snk_x - 2]
]
food =[sh/2,sw/2] #creating food and adding it to screen
w.addch(food[0],food[1],curses.ACS_PI)
key = curses.KEY_RIGHT
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key
    #Losing conditions for snake
    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake[1:]:
        curses.endwin()
        quit()
    new_head = [snake[0][0],snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0]+=1
    if key == curses.KEY_UP:
        new_head[0]-=1
    if key == curses.KEY_LEFT:
        new_head[1]-=1
    if key == curses.KEY_RIGHT:
        new_head[1]+=1
    snake.insert(0,new_head)

    if snake[0]==food:
        food=None
        while food is None:
            nf=[
             random.randint(1,sh-1),
             random.randint(1,sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0],food[1],curses.ACS_PI)
    else:
        tail = snake.pop()
        w.addch(tail[0],tail[1],' ')
    w.addch(snake[0][0],snake[0][1])