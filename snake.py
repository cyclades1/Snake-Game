import random
import curses
import time

sc = curses.initscr()
h, w = sc.getmaxyx()
win = curses.newwin(h, w, 0, 0)

win.keypad(1)
curses.curs_set(0)

sh = h//2
sw = w//4

snake_head = [sh,sw]
snake_position = [[sh,sw],[sh-1,sw],[sh-2,sw]]
apple_position = [20,20]
score = 0


win.addch(apple_position[0], apple_position[1],'*')

prev_button_direction = 1
button_direction = 1
key = curses.KEY_RIGHT

def ca(score):
    apple_position = [random.randint(1,h-2),random.randint(1,w-2)]
    score += 1
    return apple_position, score

def cb(snake_head):
    if snake_head[0]>=h-1 or snake_head[0]<=0 or snake_head[1]>=w-1 or snake_head[1]<=0 :
        return 1
    else:
        return 0

def cs(snake_position):
    snake_head = snake_position[0]
    if snake_head in snake_position[1:]:
        return 1
    else:
        return 0

a = []
while True:
    win.border(0)
    win.timeout(100)

    next_key = win.getch()

    if next_key == -1:
        key = key
    else:
        key = next_key

    if key == curses.KEY_LEFT and prev_button_direction != 1:
        button_direction = 0
    elif key == curses.KEY_RIGHT and prev_button_direction != 0:
        button_direction = 1
    elif key == curses.KEY_UP and prev_button_direction != 2:
        button_direction = 3
    elif key == curses.KEY_DOWN and prev_button_direction != 3:
        button_direction = 2
    else:
        pass

    prev_button_direction = button_direction

    if button_direction == 1:
        snake_head[1] += 1
    elif button_direction == 0:
        snake_head[1] -= 1
    elif button_direction == 2:
        snake_head[0] += 1
    elif button_direction == 3:
        snake_head[0] -= 1

    if snake_head == apple_position:
        apple_position, score = ca(score)
        snake_position.insert(0, list(snake_head))
        a.append(apple_position)
        win.addch(apple_position[0], apple_position[1], '*')

    else:
        snake_position.insert(0, list(snake_head))
        last = snake_position.pop()
        win.addch(last[0], last[1], ' ')

    win.addch(snake_position[0][0], snake_position[0][1],curses.ACS_DIAMOND)
   
    if cb(snake_head) == 1 or cs(snake_position) == 1:
        break


sc.addstr(10, 30, 'Your Score is:  '+str(score))
sc.refresh()
time.sleep(2)
curses.endwin()
