from tkinter import*
import random
from data import*

class left_panel:
    def __init__(self, root, frame):
        self.root = root
        self.frame = frame

        self.button_frame = Frame(frame, bg='#80c1ff', bd=5)
        self.button_frame.place(relx=0.0833, rely=0.07, relwidth=0.83, relheight=0.11)
        
        '''
            Create an empty board
        '''
        self.board = Frame(frame, bg='#80c1ff', bd=10)
        self.board.place(relx=0.0833, rely=0.214, relwidth=0.83, relheight=0.714)

        # Look up how to set default font!
        '''
            Sets font to OpenDyslexic Mono
        '''
        def set_font_open_dyslexic_cubes(self):
            font = "%(family)s %(size)i %(weight)s %(slant)s" % {'family': 'OpenDyslexicMono', 'size': 70, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}
            self.configure(font=font)

        
        '''
            Create an empty cube spaces
        '''
        self.r1_c1 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r1_c1)
        self.r1_c1.place(relx=.001,rely=.001, relwidth=.24, relheight=.24)

        self.r1_c2 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r1_c2)
        self.r1_c2.place(relx=.254, rely=.001, relwidth=.24, relheight=.24)

        self.r1_c3 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r1_c3)
        self.r1_c3.place(relx=.507, rely=.001, relwidth=.24, relheight=.24)

        self.r1_c4 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r1_c4)
        self.r1_c4.place(relx=.76, rely=.001, relwidth=.24, relheight=.24)

        self.r2_c1 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r2_c1)
        self.r2_c1.place(relx=.001,rely=.254, relwidth=.24, relheight=.24)

        self.r2_c2 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r2_c2)
        self.r2_c2.place(relx=.254, rely=.254, relwidth=.24, relheight=.24)

        self.r2_c3 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r2_c3)
        self.r2_c3.place(relx=.507, rely=.254, relwidth=.24, relheight=.24)

        self.r2_c4 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r2_c4)
        self.r2_c4.place(relx=.76, rely=.254, relwidth=.24, relheight=.24)

        self.r3_c1 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r3_c1)
        self.r3_c1.place(relx=.001,rely=.507, relwidth=.24, relheight=.24)

        self.r3_c2 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r3_c2)
        self.r3_c2.place(relx=.254, rely=.507, relwidth=.24, relheight=.24)

        self.r3_c3 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r3_c3)
        self.r3_c3.place(relx=.507, rely=.507, relwidth=.24, relheight=.24)

        self.r3_c4 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r3_c4)
        self.r3_c4.place(relx=.76, rely=.507, relwidth=.24, relheight=.24)

        self.r4_c1 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r4_c1)
        self.r4_c1.place(relx=.001,rely=.76, relwidth=.24, relheight=.24)

        self.r4_c2 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r4_c2)
        self.r4_c2.place(relx=.254, rely=.76, relwidth=.24, relheight=.24)

        self.r4_c3 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r4_c3)
        self.r4_c3.place(relx=.507, rely=.76, relwidth=.24, relheight=.24)

        self.r4_c4 = Label(self.board, bg='yellow')
        set_font_open_dyslexic_cubes(self.r4_c4)
        self.r4_c4.place(relx=.76, rely=.76, relwidth=.24, relheight=.24)


        '''
            Lets the user input their own letters
        '''
        def input_board():
            self.entry_board = Frame(frame, bg='#80c1ff', bd=10)
            self.entry_board.place(relx=0.0833, rely=0.214, relwidth=0.83, relheight=0.714)

            self.entry_button_frame = Frame(frame, bg='#80c1ff', bd=5)
            self.entry_button_frame.place(relx=0.0833, rely=0.07, relwidth=0.83, relheight=0.11)

            '''
                Lets the user exit out of "input mode"
            '''
            def double_check_quit():
                self.are_you_sure_frame = Frame(self.entry_board, bg='#80c1ff', bd=5)
                self.are_you_sure_frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

                self.double_check_question = Label(self.are_you_sure_frame, font=("Comic Sans MS", 35), text="Are you sure?", bg='#80c1ff')
                self.double_check_question.place(relwidth=1, relheight=0.49)

                def sure():
                    clear_letters()
                    self.r1_c1['text'] = ""
                    self.r1_c2['text'] = ""
                    self.r1_c3['text'] = ""
                    self.r1_c4['text'] = ""
                    self.r2_c1['text'] = ""
                    self.r2_c2['text'] = ""
                    self.r2_c3['text'] = ""
                    self.r2_c4['text'] = ""
                    self.r3_c1['text'] = ""
                    self.r3_c2['text'] = ""
                    self.r3_c3['text'] = ""
                    self.r3_c4['text'] = ""
                    self.r4_c1['text'] = ""
                    self.r4_c2['text'] = ""
                    self.r4_c3['text'] = ""
                    self.r4_c4['text'] = ""
                    
                    self.are_you_sure_frame.destroy()
                    self.entry_board.destroy()
                    self.entry_button_frame.destroy()

                def not_sure():
                    self.are_you_sure_frame.destroy()

                self.sure_button = Button(self.are_you_sure_frame, font=("Comic Sans MS", 35), text="Yes", bg='gray', fg='#c63420', command=lambda: sure())
                self.sure_button.place(rely=0.51, relwidth=0.49, relheight=0.49)

                self.not_sure_button = Button(self.are_you_sure_frame, font=("Comic Sans MS", 35), text="No", bg='gray', fg='#c63420', command=lambda: not_sure())
                self.not_sure_button.place(relx=0.51, rely=0.51, relwidth=0.49, relheight=0.49)

            '''
                Lets the user confirm their input is correct before setting the values of the cubes
            '''
            def double_check_confirm():
                self.are_you_sure_frame = Frame(self.entry_board, bg='#80c1ff', bd=5)
                self.are_you_sure_frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

                self.double_check_question = Label(self.are_you_sure_frame, font=("Comic Sans MS", 35), text="Are you sure?", bg='#80c1ff')
                self.double_check_question.place(relwidth=1, relheight=0.49)

                def sure():
                    set_letter(0, self.l1.get().upper())
                    set_letter(1, self.l2.get().upper())
                    set_letter(2, self.l3.get().upper())
                    set_letter(3, self.l4.get().upper())
                    set_letter(4, self.l5.get().upper())
                    set_letter(5, self.l6.get().upper())
                    set_letter(6, self.l7.get().upper())
                    set_letter(7, self.l8.get().upper())
                    set_letter(8, self.l9.get().upper())
                    set_letter(9, self.l10.get().upper())
                    set_letter(10, self.l11.get().upper())
                    set_letter(11, self.l12.get().upper())
                    set_letter(12, self.l13.get().upper())
                    set_letter(13, self.l14.get().upper())
                    set_letter(14, self.l15.get().upper())
                    set_letter(15, self.l16.get().upper())

                    if check_letters() == False:
                        self.are_you_sure_frame.destroy()
                        
                        self.incorrect_input = Frame(self.entry_board, bg='#80c1ff', bd=5)
                        self.incorrect_input.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.4)

                        self.try_again_input = Label(self.incorrect_input, font=("Comic Sans MS", 25), text="Something went wrong\n with your input.\nPlease try again?", bg='#80c1ff')
                        self.try_again_input.place(rely=.1, relwidth=1, relheight=.85)
                        
                        self.x_try_again = Button(self.incorrect_input, text="X", command=self.incorrect_input.destroy)
                        self.x_try_again.place(relx=.9, rely=0.07, relwidth=.1, relheight=.15)

                        # self.l1.delete(0, 'end')
                        # self.l2.delete(0, 'end')
                        # self.l3.delete(0, 'end')
                        # self.l4.delete(0, 'end')
                        # self.l5.delete(0, 'end')
                        # self.l6.delete(0, 'end')
                        # self.l7.delete(0, 'end')
                        # self.l8.delete(0, 'end')
                        # self.l9.delete(0, 'end')
                        # self.l10.delete(0, 'end')
                        # self.l11.delete(0, 'end')
                        # self.l12.delete(0, 'end')
                        # self.l13.delete(0, 'end')
                        # self.l14.delete(0, 'end')
                        # self.l15.delete(0, 'end')
                        # self.l16.delete(0, 'end')
                    else:
                        self.r1_c1['text'] = get_letter(0)
                        self.r1_c2['text'] = get_letter(1)
                        self.r1_c3['text'] = get_letter(2)
                        self.r1_c4['text'] = get_letter(3)
                        self.r2_c1['text'] = get_letter(4)
                        self.r2_c2['text'] = get_letter(5)
                        self.r2_c3['text'] = get_letter(6)
                        self.r2_c4['text'] = get_letter(7)
                        self.r3_c1['text'] = get_letter(8)
                        self.r3_c2['text'] = get_letter(9)
                        self.r3_c3['text'] = get_letter(10)
                        self.r3_c4['text'] = get_letter(11)
                        self.r4_c1['text'] = get_letter(12)
                        self.r4_c2['text'] = get_letter(13)
                        self.r4_c3['text'] = get_letter(14)
                        self.r4_c4['text'] = get_letter(15)

                        self.are_you_sure_frame.destroy()
                        self.entry_board.destroy()
                        self.entry_button_frame.destroy()

                def not_sure():
                    self.are_you_sure_frame.destroy()

                '''
                    Yes button
                '''
                self.sure_button = Button(self.are_you_sure_frame, font=("Comic Sans MS", 35), text="Yes", bg='gray', fg='#c63420', command=lambda: sure())
                self.sure_button.place(rely=0.51, relwidth=0.49, relheight=0.49)

                '''
                    No button
                '''
                self.not_sure_button = Button(self.are_you_sure_frame, font=("Comic Sans MS", 35), text="No", bg='gray', fg='#c63420', command=lambda: not_sure())
                self.not_sure_button.place(relx=0.51, rely=0.51, relwidth=0.49, relheight=0.49)

            '''
                    Confirm button
            '''
            self.confirm_button = Button(self.entry_button_frame, font=("Comic Sans MS", 35), text="Confirm", bg='gray', fg='#c63420', command=lambda: double_check_confirm())
            self.confirm_button.place(relheight=1, relwidth=0.49)

            '''
                Quit button
            '''
            self.quit_button = Button(self.entry_button_frame, font=("Comic Sans MS", 35), text="Quit", bg='gray', fg='#c63420', command=lambda: double_check_quit())
            self.quit_button.place(relx=0.51, relheight=1, relwidth=0.49)

            '''
                Creates entry boxes and allows the user to navigate using the arrow keys
            '''
            self.l1 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l1)
            self.l1.place(relx=.001,rely=.001, relwidth=.24, relheight=.24)

            self.l2 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l2)
            self.l2.place(relx=.254, rely=.001, relwidth=.24, relheight=.24)

            self.l3 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l3)
            self.l3.place(relx=.507, rely=.001, relwidth=.24, relheight=.24)

            self.l4 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l4)
            self.l4.place(relx=.76, rely=.001, relwidth=.24, relheight=.24)

            self.l5 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l5)
            self.l5.place(relx=.001,rely=.254, relwidth=.24, relheight=.24)

            self.l6 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l6)
            self.l6.place(relx=.254, rely=.254, relwidth=.24, relheight=.24)

            self.l7 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l7)
            self.l7.place(relx=.507, rely=.254, relwidth=.24, relheight=.24)

            self.l8 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l8)
            self.l8.place(relx=.76, rely=.254, relwidth=.24, relheight=.24)

            self.l9 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l9)
            self.l9.place(relx=.001,rely=.507, relwidth=.24, relheight=.24)

            self.l10 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l10)
            self.l10.place(relx=.254, rely=.507, relwidth=.24, relheight=.24)

            self.l11 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l11)
            self.l11.place(relx=.507, rely=.507, relwidth=.24, relheight=.24)

            self.l12 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l12)
            self.l12.place(relx=.76, rely=.507, relwidth=.24, relheight=.24)

            self.l13 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l13)
            self.l13.place(relx=.001,rely=.76, relwidth=.24, relheight=.24)

            self.l14 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l14)
            self.l14.place(relx=.254, rely=.76, relwidth=.24, relheight=.24)

            self.l15 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l15)
            self.l15.place(relx=.507, rely=.76, relwidth=.24, relheight=.24)

            self.l16 = Entry(self.entry_board, bg='yellow', justify='center')
            set_font_open_dyslexic_cubes(self.l16)
            self.l16.place(relx=.76, rely=.76, relwidth=.24, relheight=.24)

            '''
            ARROW KEYS
            '''
            def RIGHT(event):
                if self.root.focus_get() == self.l1:
                    self.l2.focus()
                elif self.root.focus_get() == self.l2:
                    self.l3.focus()
                elif self.root.focus_get() == self.l3:
                    self.l4.focus()
                elif self.root.focus_get() == self.l4:
                    self.l1.focus() #should this be l5?
                elif self.root.focus_get() == self.l5:
                    self.l6.focus()
                elif self.root.focus_get() == self.l6:
                    self.l7.focus()
                elif self.root.focus_get() == self.l7:
                    self.l8.focus()
                elif self.root.focus_get() == self.l8:
                    self.l5.focus() #should this be l9?
                elif self.root.focus_get() == self.l9:
                    self.l10.focus()
                elif self.root.focus_get() == self.l10:
                    self.l11.focus()
                elif self.root.focus_get() == self.l11:
                    self.l12.focus()
                elif self.root.focus_get() == self.l12:
                    self.l9.focus() #should this be l13?
                elif self.root.focus_get() == self.l13:
                    self.l14.focus()
                elif self.root.focus_get() == self.l14:
                    self.l15.focus()
                elif self.root.focus_get() == self.l15:
                    self.l16.focus()
                elif self.root.focus_get() == self.l16:
                    self.l13.focus() #should this be l1?

            def LEFT(event):
                if self.root.focus_get() == self.l1:
                    self.l4.focus()
                elif self.root.focus_get() == self.l2:
                    self.l1.focus()
                elif self.root.focus_get() == self.l3:
                    self.l2.focus()
                elif self.root.focus_get() == self.l4:
                    self.l3.focus()
                elif self.root.focus_get() == self.l5:
                    self.l8.focus()
                elif self.root.focus_get() == self.l6:
                    self.l5.focus()
                elif self.root.focus_get() == self.l7:
                    self.l6.focus()
                elif self.root.focus_get() == self.l8:
                    self.l7.focus()
                elif self.root.focus_get() == self.l9:
                    self.l12.focus()
                elif self.root.focus_get() == self.l10:
                    self.l9.focus()
                elif self.root.focus_get() == self.l11:
                    self.l10.focus()
                elif self.root.focus_get() == self.l12:
                    self.l11.focus()
                elif self.root.focus_get() == self.l13:
                    self.l16.focus()
                elif self.root.focus_get() == self.l14:
                    self.l13.focus()
                elif self.root.focus_get() == self.l15:
                    self.l14.focus()
                elif self.root.focus_get() == self.l16:
                    self.l15.focus()

            def UP(event):
                if self.root.focus_get() == self.l1:
                    self.l13.focus()
                elif self.root.focus_get() == self.l2:
                    self.l14.focus()
                elif self.root.focus_get() == self.l3:
                    self.l15.focus()
                elif self.root.focus_get() == self.l4:
                    self.l16.focus()
                elif self.root.focus_get() == self.l5:
                    self.l1.focus()
                elif self.root.focus_get() == self.l6:
                    self.l2.focus()
                elif self.root.focus_get() == self.l7:
                    self.l3.focus()
                elif self.root.focus_get() == self.l8:
                    self.l4.focus()
                elif self.root.focus_get() == self.l9:
                    self.l5.focus()
                elif self.root.focus_get() == self.l10:
                    self.l6.focus()
                elif self.root.focus_get() == self.l11:
                    self.l7.focus()
                elif self.root.focus_get() == self.l12:
                    self.l8.focus()
                elif self.root.focus_get() == self.l13:
                    self.l9.focus()
                elif self.root.focus_get() == self.l14:
                    self.l10.focus()
                elif self.root.focus_get() == self.l15:
                    self.l11.focus()
                elif self.root.focus_get() == self.l16:
                    self.l12.focus()

            def DOWN(event):
                if self.root.focus_get() == self.l1:
                    self.l5.focus()
                elif self.root.focus_get() == self.l2:
                    self.l6.focus()
                elif self.root.focus_get() == self.l3:
                    self.l7.focus()
                elif self.root.focus_get() == self.l4:
                    self.l8.focus()
                elif self.root.focus_get() == self.l5:
                    self.l9.focus()
                elif self.root.focus_get() == self.l6:
                    self.l10.focus()
                elif self.root.focus_get() == self.l7:
                    self.l11.focus()
                elif self.root.focus_get() == self.l8:
                    self.l12.focus()
                elif self.root.focus_get() == self.l9:
                    self.l13.focus()
                elif self.root.focus_get() == self.l10:
                    self.l14.focus()
                elif self.root.focus_get() == self.l11:
                    self.l15.focus()
                elif self.root.focus_get() == self.l12:
                    self.l16.focus()
                elif self.root.focus_get() == self.l13:
                    self.l1.focus()
                elif self.root.focus_get() == self.l14:
                    self.l2.focus()
                elif self.root.focus_get() == self.l15:
                    self.l3.focus()
                elif self.root.focus_get() == self.l16:
                    self.l4.focus()

            self.root.bind("<Right>", RIGHT)
            self.root.bind("<Left>", LEFT)
            self.root.bind("<Up>", UP)
            self.root.bind("<Down>", DOWN)
        
        '''
            Create button options for type of board
        '''
        self.input_board_button = Button(self.button_frame, font=("Comic Sans MS", 35), text="Input Board", bg='gray', fg='#c63420', command=lambda: input_board())
        self.input_board_button.place(relheight=1, relwidth=0.49)

        self.random_board_button = Button(self.button_frame, font=("Comic Sans MS", 35), text="New Board", bg='gray', fg='#c63420', command=lambda: random_board())
        self.random_board_button.place(relx=0.51, relheight=1, relwidth=0.49)

        '''
            Generate a random new board based on dice
        '''
        def random_board():
            random_values()

            self.r1_c1['text'] = get_letter(0)
            self.r1_c2['text'] = get_letter(1)
            self.r1_c3['text'] = get_letter(2)
            self.r1_c4['text'] = get_letter(3)
            self.r2_c1['text'] = get_letter(4)
            self.r2_c2['text'] = get_letter(5)
            self.r2_c3['text'] = get_letter(6)
            self.r2_c4['text'] = get_letter(7)
            self.r3_c1['text'] = get_letter(8)
            self.r3_c2['text'] = get_letter(9)
            self.r3_c3['text'] = get_letter(10)
            self.r3_c4['text'] = get_letter(11)
            self.r4_c1['text'] = get_letter(12)
            self.r4_c2['text'] = get_letter(13)
            self.r4_c3['text'] = get_letter(14)
            self.r4_c4['text'] = get_letter(15)

            clear_letters()
