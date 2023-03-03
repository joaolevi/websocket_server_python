import tkinter

from test_client import ClientAccess
from asyncio import create_task

class ClientWindow:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Lista")
        self.window.geometry("320x200")
        self.window.maxsize(width=690, height=720)

        ### Client window label
        self.client_frame = tkinter.Frame(self.window, height=30)
        self.client_frame.pack(fill='x')

        self.client_label = tkinter.Label(self.client_frame, text="Client")
        self.client_label.pack()

        ### Name box
        self.name_frame = tkinter.Frame(self.window, height=30)
        self.name_frame.pack(fill='x')

        self.name_label = tkinter.Label(self.name_frame, text="Name: ")
        self.name_label.pack(side="left")

        self.name_textbox = tkinter.Entry(self.name_frame)
        self.name_textbox.pack(side="right", padx=20)

        ### Age box    
        self.age_frame = tkinter.Frame(self.window, height=30)
        self.age_frame.pack(fill='x')

        self.age_label = tkinter.Label(self.age_frame, text="Age: ")
        self.age_label.pack(side="left")

        self.age_textbox = tkinter.Entry(self.age_frame)
        self.age_textbox.pack(side="right", padx=20)

        ### Register box
        self.reg_frame = tkinter.Frame(self.window, height=30)
        self.reg_frame.pack(fill='x')

        self.reg_label = tkinter.Label(self.reg_frame, text="Register Number: ")
        self.reg_label.pack(side="left")

        self.reg_textbox = tkinter.Entry(self.reg_frame)
        self.reg_textbox.pack(side="right", padx=20)

        ### Send button
        self.send_frame = tkinter.Frame(self.window, height=30)
        self.send_frame.pack(fill='y')

        self.send_btn = tkinter.Button(self.send_frame, text="Send", command=lambda: self.start_client())
        self.send_btn.pack(pady=5)

        self.window.mainloop()

    def start_client(self):
        self.ClientAccess = ClientAccess()
        create_task(self.ClientAccess.start())

if __name__== '__main__':
    ClientWindow()