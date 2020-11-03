from tkinter import *
from left_panel import *
from right_panel import *
import os

class tk_window:
    def __init__(self):

        '''
            Initialize Set Up of GUI
        '''
        self.root = Tk()
        self.root.title("sima_boggle")

        '''
            Dimensions of Canvas
        '''
        HEIGHT = 700
        WIDTH = 1200

        self.canvas = Canvas(self.root, height=HEIGHT, width=WIDTH, bg='white')
        self.canvas.pack()

        self.base_folder = os.path.dirname(__file__)
        self.image_path = os.path.join(self.base_folder, 'left_background.png')
        self.left_background_image = PhotoImage(file=self.image_path)
        self.left_side = Label(self.root, image=self.left_background_image)
        self.left_side.place(relwidth=.5, relheight=1)

        self.base_folder = os.path.dirname(__file__)
        self.image_path = os.path.join(self.base_folder, 'right_background.png')
        self.right_background_image = PhotoImage(file=self.image_path)
        self.right_side = Label(self.root, image=self.right_background_image)
        self.right_side.place(relx=.5, relwidth=.5, relheight=1)
        
        self.my_left_panel = left_panel(self.root, self.left_side)
        self.my_right_panel = right_panel(self.root, self.right_side)

    def start(self):
        self.root.mainloop()