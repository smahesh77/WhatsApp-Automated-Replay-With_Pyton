import pyautogui as pt
from time import sleep
def getcord():
      while True:
            k = int(input("get cursor cords:"))
            if k == 1:
                  g = pt.position()
                  print("color pixel")
                  print(pt.pixel(g[0],g[1]))
                  print(g)
            if k != 1:
                  break
getcord()