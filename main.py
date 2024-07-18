import tkinter;
from tkinter import *;
from tkinter import ttk;

blackColor = "#444466"; 
whiteColor = "#feffff";
blueColor = "#6f9fbd";

dayColor = "#6cc4cc";
nightColor = "#484f60";
afternoonColor = "#bfb86d";
backgroundColor = dayColor;

window = Tk();
window.title('');
window.geometry('320x350');
window.configure(bg=backgroundColor);

ttk.Separator(window, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157);

window.mainloop();
