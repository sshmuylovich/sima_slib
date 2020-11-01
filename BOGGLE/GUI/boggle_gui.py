import tkinter as tk
from tkinter import *
import random
import os
# import player
# from player import *

'''
    Dimensions of Canvas
'''
HEIGHT = 700
WIDTH = 1200

'''
    Creates the dice which have letters on each side --> Array of length 6 per die
'''
cube_one = ["A","A","E","E","G","N"]
cube_two = ["A","O","O","T","T","W"]
cube_three = ["D","I","S","T","T","Y"]
cube_four = ["E","I","O","S","S","T"]
cube_five = ["A","B","B","J","O","O"]
cube_six = ["C","I","M","O","T","U"]
cube_seven = ["E","E","G","H","N","W"]
cube_eight = ["E","L","R","T","T","Y"]
cube_nine = ["A","C","H","O","P","S"]
cube_ten = ["D","E","I","L","R","X"]
cube_eleven = ["E","E","I","N","S","U"]
cube_twelve = ["H","I","M","N","QU","U"]
cube_thirteen = ["A","F","F","K","P","S"]
cube_fourteen = ["D","E","L","R","V","Y"]
cube_fifteen = ["E","H","R","T","V","W"]
cube_sixteen = ["H","L","N","N","R","Z"]

'''
    Sets font to OpenDyslexic Mono
'''
def set_font_open_dyslexic_cubes(self):
    font = "%(family)s %(size)i %(weight)s %(slant)s" % {'family': 'OpenDyslexicMono', 'size': 70, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
    self.configure(font=font)

'''
    Lets the user input their own letters
'''
def input_board():
    entry_board = tk.Frame(left_side, bg='#80c1ff', bd=10)
    entry_board.place(relx=0.0833, rely=0.214, relwidth=0.83, relheight=0.714)

    entry_button_frame = tk.Frame(left_side, bg='#80c1ff', bd=5)
    entry_button_frame.place(relx=0.0833, rely=0.07, relwidth=0.83, relheight=0.11)

    '''
        Lets the user exit out of "input mode"
    '''
    def double_check_quit():
        are_you_sure_frame = tk.Frame(entry_board, bg='#80c1ff', bd=5)
        are_you_sure_frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

        double_check_question = tk.Label(are_you_sure_frame, font=("Comic Sans MS", 35), text="Are you sure?", bg='#80c1ff')
        double_check_question.place(relwidth=1, relheight=0.49)

        def sure():
            r1_c1['text'] = ""
            r1_c2['text'] = ""
            r1_c3['text'] = ""
            r1_c4['text'] = ""
            r2_c1['text'] = ""
            r2_c2['text'] = ""
            r2_c3['text'] = ""
            r2_c4['text'] = ""
            r3_c1['text'] = ""
            r3_c2['text'] = ""
            r3_c3['text'] = ""
            r3_c4['text'] = ""
            r4_c1['text'] = ""
            r4_c2['text'] = ""
            r4_c3['text'] = ""
            r4_c4['text'] = ""
            
            are_you_sure_frame.destroy()
            entry_board.destroy()
            entry_button_frame.destroy()

        def not_sure():
            are_you_sure_frame.destroy()

        sure_button = tk.Button(are_you_sure_frame, font=("Comic Sans MS", 35), text="Yes", bg='gray', fg='#c63420', command=lambda: sure())
        sure_button.place(rely=0.51, relwidth=0.49, relheight=0.49)

        not_sure_button = tk.Button(are_you_sure_frame, font=("Comic Sans MS", 35), text="No", bg='gray', fg='#c63420', command=lambda: not_sure())
        not_sure_button.place(relx=0.51, rely=0.51, relwidth=0.49, relheight=0.49)

    '''
        Lets the user confirm their input is correct before setting the values of the cubes
    '''
    def double_check_confirm():
        are_you_sure_frame = tk.Frame(entry_board, bg='#80c1ff', bd=5)
        are_you_sure_frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

        double_check_question = tk.Label(are_you_sure_frame, font=("Comic Sans MS", 35), text="Are you sure?", bg='#80c1ff')
        double_check_question.place(relwidth=1, relheight=0.49)

        def sure():
            r1_c1['text'] = l1.get().upper()
            r1_c2['text'] = l2.get().upper()
            r1_c3['text'] = l3.get().upper()
            r1_c4['text'] = l4.get().upper()
            r2_c1['text'] = l5.get().upper()
            r2_c2['text'] = l6.get().upper()
            r2_c3['text'] = l7.get().upper()
            r2_c4['text'] = l8.get().upper()
            r3_c1['text'] = l9.get().upper()
            r3_c2['text'] = l10.get().upper()
            r3_c3['text'] = l11.get().upper()
            r3_c4['text'] = l12.get().upper()
            r4_c1['text'] = l13.get().upper()
            r4_c2['text'] = l14.get().upper()
            r4_c3['text'] = l15.get().upper()
            r4_c4['text'] = l16.get().upper()

            are_you_sure_frame.destroy()
            entry_board.destroy()
            entry_button_frame.destroy()

        def not_sure():
            are_you_sure_frame.destroy()

        '''
            Yes button
        '''
        sure_button = tk.Button(are_you_sure_frame, font=("Comic Sans MS", 35), text="Yes", bg='gray', fg='#c63420', command=lambda: sure())
        sure_button.place(rely=0.51, relwidth=0.49, relheight=0.49)

        '''
            No button
        '''
        not_sure_button = tk.Button(are_you_sure_frame, font=("Comic Sans MS", 35), text="No", bg='gray', fg='#c63420', command=lambda: not_sure())
        not_sure_button.place(relx=0.51, rely=0.51, relwidth=0.49, relheight=0.49)

    '''
            Confirm button
    '''
    confirm_button = tk.Button(entry_button_frame, font=("Comic Sans MS", 35), text="Confirm", bg='gray', fg='#c63420', command=lambda: double_check_confirm())
    confirm_button.place(relheight=1, relwidth=0.49)

    '''
        Quit button
    '''
    quit_button = tk.Button(entry_button_frame, font=("Comic Sans MS", 35), text="Quit", bg='gray', fg='#c63420', command=lambda: double_check_quit())
    quit_button.place(relx=0.51, relheight=1, relwidth=0.49)

    '''
        Creates entry boxes
    '''
    l1 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l1)
    l1.place(relx=.001,rely=.001, relwidth=.24, relheight=.24)

    l2 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l2)
    l2.place(relx=.254, rely=.001, relwidth=.24, relheight=.24)

    l3 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l3)
    l3.place(relx=.507, rely=.001, relwidth=.24, relheight=.24)

    l4 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l4)
    l4.place(relx=.76, rely=.001, relwidth=.24, relheight=.24)

    l5 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l5)
    l5.place(relx=.001,rely=.254, relwidth=.24, relheight=.24)

    l6 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l6)
    l6.place(relx=.254, rely=.254, relwidth=.24, relheight=.24)

    l7 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l7)
    l7.place(relx=.507, rely=.254, relwidth=.24, relheight=.24)

    l8 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l8)
    l8.place(relx=.76, rely=.254, relwidth=.24, relheight=.24)

    l9 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l9)
    l9.place(relx=.001,rely=.507, relwidth=.24, relheight=.24)

    l10 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l10)
    l10.place(relx=.254, rely=.507, relwidth=.24, relheight=.24)

    l11 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l11)
    l11.place(relx=.507, rely=.507, relwidth=.24, relheight=.24)

    l12 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l12)
    l12.place(relx=.76, rely=.507, relwidth=.24, relheight=.24)

    l13 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l13)
    l13.place(relx=.001,rely=.76, relwidth=.24, relheight=.24)

    l14 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l14)
    l14.place(relx=.254, rely=.76, relwidth=.24, relheight=.24)

    l15 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l15)
    l15.place(relx=.507, rely=.76, relwidth=.24, relheight=.24)

    l16 = tk.Entry(entry_board, bg='yellow', justify='center')
    set_font_open_dyslexic_cubes(l16)
    l16.place(relx=.76, rely=.76, relwidth=.24, relheight=.24)
    
'''
    Generate a random new board based on dice
'''
def random_board():
    cubes=[cube_one, cube_two, cube_three, cube_four, cube_five, cube_six, cube_seven, cube_eight, 
    cube_nine, cube_ten, cube_eleven, cube_twelve, cube_thirteen, cube_fourteen, cube_fifteen, cube_sixteen]

    cubes_temp = []

    letters = []

    for x in range (0, 16):
        random_cube = random.choice(cubes)
        cubes_temp.append(random_cube)
        cubes.remove(random_cube)
        random_letter = random.choice(random_cube)
        letters.append(random_letter)

    r1_c1['text'] = letters[0]
    r1_c2['text'] = letters[1]
    r1_c3['text'] = letters[2]
    r1_c4['text'] = letters[3]
    r2_c1['text'] = letters[4]
    r2_c2['text'] = letters[5]
    r2_c3['text'] = letters[6]
    r2_c4['text'] = letters[7]
    r3_c1['text'] = letters[8]
    r3_c2['text'] = letters[9]
    r3_c3['text'] = letters[10]
    r3_c4['text'] = letters[11]
    r4_c1['text'] = letters[12]
    r4_c2['text'] = letters[13]
    r4_c3['text'] = letters[14]
    r4_c4['text'] = letters[15]

    letters.clear()

'''
    Creates a pop-up window of the instructions
'''
def instructions():
    instructions = tk.Frame(root, bg='#80c1ff', bd=5)
    instructions.place(relx=.1, rely=.1, relwidth=.8, relheight=.8)
    # base_folder = os.path.dirname(__file__)
    # image_path = os.path.join(base_folder, 'left_background.png')
    # info = PhotoImage(file=image_path)
    # info_image = tk.Label(root, image=info)
    # info_image.place(relwidth=.5, relheight=1)
    x_questions = tk.Button(instructions, text="X", command=instructions.destroy)
    x_questions.place(relx=.94, rely=0.01, relwidth=.05, relheight=.05)

'''
    Opening Set Up of GUI
'''
root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='white')
canvas.pack()

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'left_background.png')
left_background_image = PhotoImage(file=image_path)
left_side = tk.Label(root, image=left_background_image)
left_side.place(relwidth=.5, relheight=1)

base_folder = os.path.dirname(__file__)
image_path = os.path.join(base_folder, 'right_background.png')
right_background_image = PhotoImage(file=image_path)
right_side = tk.Label(root, image=right_background_image)
right_side.place(relx=.5, relwidth=.5, relheight=1)

button_frame = tk.Frame(left_side, bg='#80c1ff', bd=5)
button_frame.place(relx=0.0833, rely=0.07, relwidth=0.83, relheight=0.11)

'''
    Creates an empty board
'''
board = tk.Frame(left_side, bg='#80c1ff', bd=10)
board.place(relx=0.0833, rely=0.214, relwidth=0.83, relheight=0.714)

r1_c1 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r1_c1)
r1_c1.place(relx=.001,rely=.001, relwidth=.24, relheight=.24)

r1_c2 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r1_c2)
r1_c2.place(relx=.254, rely=.001, relwidth=.24, relheight=.24)

r1_c3 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r1_c3)
r1_c3.place(relx=.507, rely=.001, relwidth=.24, relheight=.24)

r1_c4 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r1_c4)
r1_c4.place(relx=.76, rely=.001, relwidth=.24, relheight=.24)

r2_c1 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r2_c1)
r2_c1.place(relx=.001,rely=.254, relwidth=.24, relheight=.24)

r2_c2 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r2_c2)
r2_c2.place(relx=.254, rely=.254, relwidth=.24, relheight=.24)

r2_c3 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r2_c3)
r2_c3.place(relx=.507, rely=.254, relwidth=.24, relheight=.24)

r2_c4 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r2_c4)
r2_c4.place(relx=.76, rely=.254, relwidth=.24, relheight=.24)

r3_c1 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r3_c1)
r3_c1.place(relx=.001,rely=.507, relwidth=.24, relheight=.24)

r3_c2 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r3_c2)
r3_c2.place(relx=.254, rely=.507, relwidth=.24, relheight=.24)

r3_c3 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r3_c3)
r3_c3.place(relx=.507, rely=.507, relwidth=.24, relheight=.24)

r3_c4 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r3_c4)
r3_c4.place(relx=.76, rely=.507, relwidth=.24, relheight=.24)

r4_c1 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r4_c1)
r4_c1.place(relx=.001,rely=.76, relwidth=.24, relheight=.24)

r4_c2 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r4_c2)
r4_c2.place(relx=.254, rely=.76, relwidth=.24, relheight=.24)

r4_c3 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r4_c3)
r4_c3.place(relx=.507, rely=.76, relwidth=.24, relheight=.24)

r4_c4 = tk.Label(board, bg='yellow')
set_font_open_dyslexic_cubes(r4_c4)
r4_c4.place(relx=.76, rely=.76, relwidth=.24, relheight=.24)

'''
    Creates button options for type of board
'''
input_board_button = tk.Button(button_frame, font=("Comic Sans MS", 35), text="Input Board", bg='gray', fg='#c63420', command=lambda: input_board())
input_board_button.place(relheight=1, relwidth=0.49)

random_board_button = tk.Button(button_frame, font=("Comic Sans MS", 35), text="New Board", bg='gray', fg='#c63420', command=lambda: random_board())
random_board_button.place(relx=0.51, relheight=1, relwidth=0.49)

'''
    Creates questions button
'''
questions = tk.Button(right_side, text="?", command=lambda: instructions())
questions.place(relx=.94, rely=0.01, relwidth=.05, relheight=.05)

root.mainloop()
