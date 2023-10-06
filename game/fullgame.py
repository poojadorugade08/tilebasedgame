from tkinter import *
import os
import tkinter

def open_file2():
    os.system('levfi.py')

root = Tk()
root.title("Game")


# Set window size and position
window_width = 790
window_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))
root.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

# Add background image
bg_image = PhotoImage(file="InstrictionImage.png")
background_label = Label(root, image=bg_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Add button to open file2.py
button_image = PhotoImage(file="st.png")
button = Button(root, image=button_image, bd=0, command=open_file2)
button.place(relx=0.5, rely=0.7, anchor="center")


# Add instructions
instruction = tkinter.Label(root, text=" How To Play Game!!!", font=("Berlin Sans FB Demi", 20), bg="White")
instruction.place(x=50, y=50)

instruction1 = tkinter.Label(root, text="1.Press the start button to begin playing the game", font=("Berlin Sans FB Demi", 14), bg="Sky blue")
instruction1.place(x=50, y=100)

instruction2= tkinter.Label(root, text="2.Press the right directional button on keyboard to proceed.", font=("Berlin Sans FB Demi", 14), bg="Sky blue")
instruction2.place(x=50, y=130)

instruction3= tkinter.Label(root, text="3. To move backward, press the left directional button on keyboard.", font=("Berlin Sans FB Demi", 14), bg="Sky blue")
instruction3.place(x=50, y=160)

instruction4= tkinter.Label(root, text="4. To jump on tiles, click the space button.", font=("Berlin Sans FB Demi", 14), bg="Sky blue")
instruction4.place(x=50, y=190)

instruction5= tkinter.Label(root, text="5. Collect the Golden Coins to raise your score.", font=("Berlin Sans FB Demi", 14), bg="Sky blue")
instruction5.place(x=50, y=220)

instruction6= tkinter.Label(root, text="6. When you walk through the door you will win!!!!.", font=("Berlin Sans FB Demi", 14), bg="Sky blue")
instruction6.place(x=50, y=250)

instruction6= tkinter.Label(root, text="YOU CAN NOW BEGIN THE GAME IF YOU KNOW HOW TO PLAY IT.", font=("Footlight MT Light", 17), bg="Sky blue")
instruction6.place(x=60, y=350)

root.mainloop()