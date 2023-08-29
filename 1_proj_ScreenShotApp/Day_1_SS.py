
# Enhancement : Below of this code...
import time , random
import pyautogui

def screenShot ( ):
    time.sleep(3) # this will wait 5sec (delay time)
    imgName = random.randint(1,100)# it will generate random number 1 to 100
    nameOfImg = f"{imgName}_pic.png"
    img = pyautogui.screenshot() # this will take the current opening whole screen ScreenShot.
    img.save(f"./SS_Collections/{nameOfImg}")  # path wher you wanna save the SS.

    ''' instead of writing above two line we can do in one line
    # img = pyautogui.screenshot("xyz.jpg")
    img.show() # after saving open the SS.
    ''' 


def SsOfUserChoice() : 
    time.sleep(3)
    status= pyautogui.confirm("You want ScreenShot")
    if (status.lower() == 'ok'): 
         pyautogui.confirm("Click OK") 
         time.sleep(3)     
         imgName = random.randint(1,100)*100
         nameOfImg = f"{imgName}_pic.png"
         img = pyautogui.screenshot(f"./SS_Collections/{nameOfImg}")
         img.show()
    else:
        pyautogui.alert("Oh, So you don't wanna take ScreenShot")



screenShot ( )
SsOfUserChoice() #only enhanced part


'''
-->I am using random module so that next do not replace the existing image.

-->Its user choice whether they want to take SS or not.


'''