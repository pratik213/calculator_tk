from tkinter import *
class Calculator(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x455")
        self.configure(bg="grey")

    
    def click(self,event):
        text = event.widget.cget("text")
        if text=="=":
            val=eval(self.uservalue.get())
            self.uservalue.set(val)


        elif text=="AC":
            self.uservalue.set("")

        else:
            self.uservalue.set(self.uservalue.get()+text)



    def entry(self):
        self.uservalue = StringVar()
        self.userentry = Entry(textvariable=self.uservalue, font="aerial 35 bold").grid(row=0, column=0, columnspan=175, padx = 1, pady=7)


    def buttons(self):
        Button(text = "7", font = "2",height=2,width=7).grid(row = 1, column  = 0, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text="4", font="2", height=2, width=7).grid(row=2, column=0, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text="1", font="2", height=2, width=7).grid(row=3, column=0, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text="0", font="2", height=2, width=7).grid(row=4, column=0, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)

        Button(text="8", font="2", height=2, width=7).grid(row=1, column=1, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text="5", font="2", height=2, width=7).grid(row=2, column=1, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text="2", font="2", height=2, width=7).grid(row=3, column=1,padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text=".", font="2", height=2, width=7).grid(row=4, column=1, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)

        Button(text="9", font="2", height=2, width=7).grid(row=1, column=2, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text="6", font="2", height=2, width=7).grid(row=2, column=2, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text="3", font="2", height=2, width=7).grid(row=3, column=2, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text="=", font="2", height=2, width=7).grid(row=4, column=2, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)

        Button(text="/", font="2", height=2, width=7).grid(row=1, column=3, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text="*", font="2", height=2, width=7).grid(row=2, column=3, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text="-", font="2", height=2, width=7).grid(row=3, column=3, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)
        Button(text="+", font="2", height=2, width=7).grid(row=4, column=3, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)

        Button(text="AC", font="2", height=1, width=10).grid(row=5, column=1, padx = 10, pady = 10)
        self.bind("<Button-1>", self.click)




if __name__ == '__main__':
    window=Calculator()
    window.entry()
    window.buttons()
    window.mainloop()
