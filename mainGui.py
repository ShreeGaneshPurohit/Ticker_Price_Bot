import tkinter as tk

if __name__ == '__main__' :
    window = tk.Tk()
    window.title("Invest Guru Price Notifier")
    window.geometry("650x650")
    window.resizable(0,0)

    #canvas_1 Title 
    tittle_Canvas = tk.Canvas().pack()
    client_Id_Label = tk.Label().grid(row=0,column=0)
    client_Id_TextField = tk.Label().grid(row=0,column=0)
    #canvas_2 Client_Info
    client_Canvas = tk.Canvas().pack()
    #canvas_3 Buttons
    button_Canvas = tk.Canvas().pack()
    #canvas_4 Terminal_Display
    Terminal_Canvas = tk.Canvas().pack()



    window.mainloop()
    
