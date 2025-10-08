from gpiozero import Button

mainDoor = Button(2)
#adminDoors = Button()

if __name__ == "__main__":
    mainDoor.on_press = lambda: print("Main Door Button Pressed")
    #adminDoors.on_press = lambda: print("Admin Door Button Pressed")