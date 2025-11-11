import tkinter as tk

win = tk.Tk()
win.title("Railway Announcement System")

main = tk.PhotoImage(file="railway.png")

frame1 = tk.Frame(win,width=850,height=400,background="red")
label = tk.Label(frame1,image=main)
label.pack()
frame1.place(x=0,y=0)

win.mainloop()