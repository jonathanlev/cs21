#Jonathan Leventhal
#cs21 assignment#11
#program mpg

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        #create frames
        self.frame_1 = tkinter.Frame(self.main_window)
        self.frame_2 = tkinter.Frame(self.main_window)
        self.frame_3 = tkinter.Frame(self.main_window)
        self.frame_4 = tkinter.Frame(self.main_window)

        #create widget for frame 1
        self.label_1 = tkinter.Label(self.frame_1, text='Enter number of Gallons:')
        self.user_entry_1 = tkinter.Entry(self.frame_1,width = 10)
        #pack frame 1 widgets
        self.label_1.pack(side='left')
        self.user_entry_1.pack(side='left')

        
        #create widget for frame 2
        self.label_2 = tkinter.Label(self.frame_2, text='Enter number of Miles:')
        self.user_entry_2 = tkinter.Entry(self.frame_2,width = 10)
        #pack frame 2 widgets
        self.label_2.pack(side='left')
        self.user_entry_2.pack(side='left')

        
        #create widget for frame 3
        self.label_3 = tkinter.Label(self.frame_3, text='Miles Per Gallon = ')
        #pack frame 3 widget
        self.label_3.pack(side='left')

        self.value = tkinter.StringVar()
        #create widget for frame 3
        self.output = tkinter.Label(self.frame_3, textvariable=self.value)
        #pack frame 3 widget
        self.output.pack()
        
        #create calc button for frame 4
        self.calc_button = tkinter.Button(self.frame_4, text='Calculate MPG',command=self.calc_button_press)
        #pack frame 4 widget
        self.calc_button.pack(side='left')

        #create quit button for frame 4
        self.quit_button = tkinter.Button(self.frame_4, text='Quit',command=self.main_window.destroy)
        #pack frame 4 widget
        self.quit_button.pack()
        
        #pack frames
        self.frame_1.pack(side='top')
        self.frame_2.pack(side='top')
        self.frame_3.pack(side='top')
        self.frame_4.pack(side='bottom')

        #enter loop
        tkinter.mainloop()
        
    def calc_button_press(self):
        
        if self.user_entry_1.get() == '' or self.user_entry_2.get() == '':
            self.value.set('Invalid input')
        elif self.user_entry_1.get() != '' or self.user_entry_2.get() != '':
            gallons = self.user_entry_1.get()
            miles = self.user_entry_2.get()
            mpg = format(int(miles)/int(gallons),'0.2f')
            self.value.set(mpg)
        
        
            

    

        
my_gui = MyGUI()
#entry widgets
#num of gallons
#num of miles
#when calc MPG button is clicked, display num miles driven/gallon of gas
