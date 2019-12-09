from tkinter import *
 
root = Tk()
root.title("Графическая программа на Python")
root.geometry("400x300")
btn = Button(text="Knopka",          
             background="#700",     
             foreground="#ccc",
             padx="100",             
             pady="50",              
             font="16"              
             )
btn.pack() 
root.mainloop()
#import random
#def lox(n) :
#    n = 2
#    n = random.uniform(0, n)
#    if n < 1 :
#        print("Alihan lox " + str(n))
#    else :
#        print("Beka lox " + str(n))
#n = int
#lox(n)