from PIL import Image,ImageGrab
import time
import pyautogui as GUI

def action(key):
    GUI.keyDown(key)

def checkCollision(data):
    # BIRDS CHECK
    for i in range(200,300):
        for j in range(300,400):
            if data[i,j] > 150:
                action("down")
                return
    # CACTUS CHECK
    for i in range(200,300):
        for j in range(430,470):
            if data[i,j] > 150:
                action("up")
                return
    return 
           

if __name__ == "__main__":
    time.sleep(2)
    action('up')
    while True:
        img = ImageGrab.grab().convert('L')
        arr = img.load()
        checkCollision(arr)

        
        #CACTUS Area
        for i in range(200,300):
            for j in range(400,500):
                data[i,j] = 0
        #BIRDS Area
        for i in range(200,300):
            for j in range(300,400):
                data[i,j] = 150
        img.show()
        break
        
        
    
