
# Tkinter window class
class GUI(Tk):

    def __init__(self, options, joys):

        super().__init__()
        self.title("Anyshift")
        self.iconbitmap("any_ico.ico")
        self.resizable(False, False)
        
        # Create frame
        self.frame = Frame()
        self.frame.pack()

        # Joystick selection
        self.joystick_frame = LabelFrame(self.frame, text = "Joysticks selection")
        self.joystick_frame.grid(row = 0, column = 0, padx= 10, pady = 5)
        
        # No joystick connected check
        try:
            self.shifter_label = Label(self.joystick_frame, text="Shifter")
            se