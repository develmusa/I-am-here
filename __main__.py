
import pyautogui 
import threading

last_position = pyautogui.position()
idle_time = 1.0
move_distance = 50

def move():
  print("move")
  pyautogui.moveRel(0, -move_distance)
  pyautogui.moveRel(0, move_distance)




def printit():
  global last_position
  global idle_time
  position_now = pyautogui.position()
  if last_position == position_now:
    move()
  else:
    last_position = position_now
  threading.Timer(idle_time, printit).start()

if __name__ == '__main__':
  printit()    