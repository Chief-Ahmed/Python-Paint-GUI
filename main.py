from tkinter import *
from tkinter.ttk import Scale
from tkinter import colorchooser, filedialog, messagebox
import PIL.ImageGrab as ImageGrab

def check():
    print(height)
    print(width)
def startup():
    root = Tk()
    root.geometry("500x500")
    root.configure(background="#353535")

    global height
    global width
    
    height_entry = Entry(root, bd=0, bg="grey", fg="white", width=50, font=("Arial", 30))
    height_entry.insert(0, 'Height')
    height_entry.place(relx=0.25,rely=0.25, relwidth=0.5, relheight=0.1)

    width_entry = Entry(root, bd=0, bg="grey", fg="white", width=50, font=("Arial", 30))
    width_entry.insert(0, 'Width')
    width_entry.place(relx=0.25,rely=0.45, relwidth=0.5, relheight=0.1)

    create_button = Button(root, bd=0, bg="white", fg="black", text="Create")
    create_button.place(relx=0.35,rely=0.7,relwidth=0.3, relheight=0.06)

    root.mainloop()

def activate():
    class Paint():
        def __init__(self,root):
            self.root = root
            self.root.title("Paint")
            self.root.geometry("800x520")
            self.root.configure(background="#353535")
            self.root.resizable(0,0)

            self.pen_color = "black"
            self.eraser_color = "white"
            self.color_frame = LabelFrame(self.root,text="Color", font=("Arial", 15), bd=0, relief=RIDGE,bg="grey")
            self.color_frame.place(x=0,y=0,width=62,height=185)

            colors = ["#5CFF45", "#45F7FF", "#4561FF", "#FF4545", "#000000", "#EFFF32", "#FC32FF", "#FF9C32", "#382500", "#00FFC5", "#FF00BA", "#7E0000"]
            i=j=0
            for color in colors:
                Button(self.color_frame,bg=color, bd=0, relief=RIDGE,width=3, command=lambda col=color:self.select_color(col)).grid(row=i,column=j)
                i+=1
                if i==6:
                    i=0
                    j=1
            
            self.eraser_button = Button(self.root,text="Eraser", bd=0, bg="#FF6B91", command=self.eraser, width=8, relief=RIDGE)
            self.eraser_button.place(x=0,y=187)

            self.clear_button = Button(self.root,text="Clear", bd=0, bg="Red", command=lambda :self.canvas.delete("all"), width=8, relief=RIDGE)
            self.clear_button.place(x=0,y=217)

            self.canvas_color_button = Button(self.root,text="Fill", bd=0, bg="#6BFFA8", command=self.canvas_color, width=8, relief=RIDGE)
            self.canvas_color_button.place(x=0,y=247)

            self.save_button = Button(self.root,text="Save", bd=0, bg="#00AEFF", command=self.save_paint, width=8, relief=RIDGE)
            self.save_button.place(x=0,y=277)

            self.pen_size_scale_frame = LabelFrame(self.root, text="Size", bd="0", bg="grey", font=("Arial", 15), relief=RIDGE)
            self.pen_size_scale_frame.place(x=0,y=301,height=200,width=62)

            self.pen_size = Scale(self.pen_size_scale_frame,orient=VERTICAL, from_=50, to=0, length=170)
            self.pen_size.set(1)
            self.pen_size.grid(row=0, column=1, padx=15)

            self.canvas = Canvas(self.root,bg="white", bd=0, relief=GROOVE, height=500,width=700)
            self.canvas.place(x=80, y=5)

            self.canvas.bind("<B1-Motion>", self.paint)

        def paint(self, event):
            x1,y1 = (event.x-2),(event.y-2)
            x2,y2 = (event.x-2),(event.y-2)

            self.canvas.create_oval(x1,y1,x2,y2,fill=self.pen_color, outline=self.pen_color, width=self.pen_size.get())

        def select_color(self,col):
            self.pen_color = col

        def eraser(self):
            self.pen_color = "white"

        def canvas_color(self):
            color = colorchooser.askcolor()
            self.canvas.configure(background=color[1])

        def save_paint(self):
            try:
                filename = filedialog.asksaveasfilename(defaultextension='.jpg')

                x = self.root.winfo_rootx() + self.canvas.winfo_x()

                y = self.root.winfo_rooty() + self.canvas.winfo_y()

                x1 = x + self.canvas.winfo_width()

                y1 = y + self.canvas.winfo_height()

                ImageGrab.grab().crop((x, y, x1, y1)).save(filename)
                messagebox.showinfo("Image Saved:", str(filename))

            except:
                messagebox.showerror("Error: \nSomething went wrong :(")
    if __name__ == "__main__":
        root = Tk()
        p = Paint(root)
        root.mainloop()

activate() 