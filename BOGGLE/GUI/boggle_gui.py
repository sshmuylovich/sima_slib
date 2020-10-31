import tkinter as tk
from tkinter import *
import random
import os
# import player
# from player import *

HEIGHT = 700
WIDTH = 1200

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

def play_game():
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
    

def test_function(entry):
    print("This is the entry: ", entry)
    # label['text'] = entry


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


frame = tk.Frame(left_side, bg='#80c1ff', bd=5)
frame.place(relx=0.0833, rely=0.07, relwidth=0.83, relheight=0.11)

board = tk.Frame(left_side, bg='#80c1ff', bd=10)
board.place(relx=0.0833, rely=0.214, relwidth=0.83, relheight=0.714)

r1_c1 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70))
r1_c1.place(relx=.001,rely=.001, relwidth=.24, relheight=.24)

r1_c2 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r1_c2.place(relx=.254, rely=.001, relwidth=.24, relheight=.24)

r1_c3 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r1_c3.place(relx=.507, rely=.001, relwidth=.24, relheight=.24)

r1_c4 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r1_c4.place(relx=.76, rely=.001, relwidth=.24, relheight=.24)

r2_c1 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70))
r2_c1.place(relx=.001,rely=.254, relwidth=.24, relheight=.24)

r2_c2 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r2_c2.place(relx=.254, rely=.254, relwidth=.24, relheight=.24)

r2_c3 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r2_c3.place(relx=.507, rely=.254, relwidth=.24, relheight=.24)

r2_c4 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r2_c4.place(relx=.76, rely=.254, relwidth=.24, relheight=.24)

r3_c1 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70))
r3_c1.place(relx=.001,rely=.507, relwidth=.24, relheight=.24)

r3_c2 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r3_c2.place(relx=.254, rely=.507, relwidth=.24, relheight=.24)

r3_c3 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r3_c3.place(relx=.507, rely=.507, relwidth=.24, relheight=.24)

r3_c4 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r3_c4.place(relx=.76, rely=.507, relwidth=.24, relheight=.24)

r4_c1 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70))
r4_c1.place(relx=.001,rely=.76, relwidth=.24, relheight=.24)

r4_c2 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r4_c2.place(relx=.254, rely=.76, relwidth=.24, relheight=.24)

r4_c3 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r4_c3.place(relx=.507, rely=.76, relwidth=.24, relheight=.24)

r4_c4 = tk.Label(board, bg='yellow', font=('Comic Sans MS',70)) 
r4_c4.place(relx=.76, rely=.76, relwidth=.24, relheight=.24)

start_button = tk.Button(frame, text="Generate New Board", bg='gray', fg='#c63420', command=lambda: play_game())
start_button.place(relx=0.7, relheight=1, relwidth=0.3)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.685, relheight=1)
entry.insert(0, " Enter Board Letters: ")

# button = tk.Button(frame, text="Get Input", bg='gray', fg='blue', font=40, command=lambda: test_function(entry.get()))
# button.place(relx=0.7, relheight=1, relwidth=0.3)

root.mainloop()
