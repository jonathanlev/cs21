#Jonathan Leventhal
#cs21 assignment#11
#program temp convert

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        
        #create frames
        self.frame_1 = tkinter.Frame(self.main_window)
        self.frame_2 = tkinter.Frame(self.main_window)
        self.frame_3 = tkinter.Frame(self.main_window)

        #create widget for frame 1
        self.cels_text = tkinter.Label(self.frame_1, text='Enter the Celsius Temperature:')
        self.cels_input = tkinter.Entry(self.frame_1,width = 10)
        #pack frame 1 widgets
        self.cels_text.pack(side='top')
        self.cels_input.pack(side='bottom')

        #create widget for frame 2
        self.fahr_text = tkinter.Label(self.frame_2, text='Fahrenheit Temperature:')
        #pack frame 2 widgets
        self.fahr_text.pack(side='top')

        self.value = tkinter.StringVar()
        #create widget for frame 2
        self.output = tkinter.Label(self.frame_2, textvariable=self.value)
        #pack frame 2 widget
        self.output.pack(side='bottom')   
        
        
        #create convert button for frame 3
        self.convert_button = tkinter.Button(self.frame_3, text='Convert to Fahrenheit',command=self.convert_button_press)
        #pack frame 3 widget
        self.convert_button.pack(side='top')

        #create quit button for frame 3
        self.quit_button = tkinter.Button(self.frame_3, text='Quit',command=self.main_window.destroy)
        #pack frame 3 widget
        self.quit_button.pack(side='bottom')
        
        #pack frames
        self.frame_1.pack(side='left')
        self.frame_2.pack(side='left')
        self.frame_3.pack(side='right')

        #enter loop
        tkinter.mainloop()
        
    def convert_button_press(self):
        
        if self.cels_input.get() == '':
            self.value.set('Invalid input')
            
        elif self.cels_input.get() != '': 
            c = self.cels_input.get()
            c = float(c)
            f = format(float(9/5)*c + 32.0,'0.2f')
            self.value.set(f)
        
        
            

    

        
my_gui = MyGUI()
#entry widgets
#num of gallons
#num of miles
#when calc MPG button is clicked, display num miles driven/gallon of gas
