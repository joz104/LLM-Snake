import curses
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
height , width = stdscr.getmaxyx()
snake = [[width//2, height//2]]
food = None
while food != 'q':
     ch = stdscr.getch()
     keymap={
         ord("a"):'l',ord("b"):'u',ord("c"):'r',ord("d"):'d'
     }
     direction = keymap.get(ch,' ')
     if direction==' ':
          pass
     elif direction==keymap["a"]and snake[-1][0]>0:
        snake.insert(-1,[snake[-1][0]-1,snake[-1][1]])
     elif direction==keymap["b"]and snake[-1][1]<height-1:
        snake.insert(-1,[snake[-1][0],snake[-1][1]+1])
     elif direction==keymap["c"]and snake[-1][0]<width-1:
        snake.insert(-1,[snake[-1][0]+1,snake[-1][1]])
     elif direction==keymap["d"]and snake[-1][1]>0:
        snake.insert(-1,[snake[-1][0],snake[-1][1]-1])

     if snake[-1]==food:
        food='q'
        score+=1
     else:
        del snake[:-1]
     stdscr.clear()
     for pos in snake:
      stdscr.addstr(*pos,"X",curses.color_pair(1));
     stdscr.refresh();
     time.sleep(.1)
curses.endwin()