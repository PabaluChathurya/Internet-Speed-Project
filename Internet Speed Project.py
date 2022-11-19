from tkinter import *
import speedtest


def speedcheck():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str( round(sp.download()/(10**6),3))+ " Mbps"
    up = str( round(sp.download()/(10**6),3))+ " Mbps"
    lap_down.config(text=down)
    lap_up.config(text=up)
    
    
sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("600x550")
sp.config(bg="Blue")

lap =Label(sp,text="Internet Speed Test", font=("Time New Roman",20, "bold"))
lap.place(x=60,y=40,height=30,width=380)

lap =Label(sp,text="Download Speed", font=("Time New Roman",20, "bold"))
lap.place(x=60,y=130,height=50,width=380)

lap_down =Label(sp,text="00", font=("Time New Roman",30, "bold"))
lap_down.place(x=60,y=200,height=50,width=380)

lap =Label(sp,text="Upload Test", font=("Time New Roman",30, "bold"))
lap.place(x=60,y=290,height=50,width=380)

lap_up =Label(sp,text="00", font=("Time New Roman",30, "bold"))
lap_up.place(x=60,y=360,height=50,width=380)

button = Button(sp,text="CHECH SPEED",font=("Time New Roman",30,"bold"),relief=RAISED,bg="red",command=speedcheck)
button.place(x=60,y=460,height=50,width=380)

sp.mainloop()