import tkinter
from tkinter.constants import DISABLED, END, NORMAL

win=tkinter.Tk();
win.title("Calculator");


def calculate(s):

    # result=eval(s);
    # return result
    try:
        result=eval(s);
        return result
    
    except Exception as e:
        if isinstance(e,ZeroDivisionError):
            return "Division By Zero"
        if isinstance(e,NameError):
            return "char not allowed"


def OnClick(n):
    inputField.config(state=NORMAL);
    if(n=="ce"):
        inputField.delete(0,END);
    elif(n=="c"):
        inputField.delete(0);
    elif(n=="="):
        
        result=calculate(inputField.get())
        inputField.delete(0,END)
        inputField.insert(0,result);

    else:
        inputField.insert(END,n);
    inputField.config(state=DISABLED);

def createNumButtons():
    tkinter.Button(win,text=9,padx=42,pady=30,command=lambda:OnClick(9)).grid(row=1,column=0);
    tkinter.Button(win,text=8,padx=42,pady=30,command=lambda:OnClick(8)).grid(row=1,column=1);
    tkinter.Button(win,text=7,padx=42,pady=30,command=lambda:OnClick(7)).grid(row=1,column=2);
    tkinter.Button(win,text=6,padx=42,pady=30,command=lambda:OnClick(6)).grid(row=2,column=0);
    tkinter.Button(win,text=5,padx=42,pady=30,command=lambda:OnClick(5)).grid(row=2,column=1);
    tkinter.Button(win,text=4,padx=42,pady=30,command=lambda:OnClick(4)).grid(row=2,column=2);
    tkinter.Button(win,text=3,padx=42,pady=30,command=lambda:OnClick(3)).grid(row=3,column=0);
    tkinter.Button(win,text=2,padx=42,pady=30,command=lambda:OnClick(2)).grid(row=3,column=1);
    tkinter.Button(win,text=1,padx=42,pady=30,command=lambda:OnClick(1)).grid(row=3,column=2);
    tkinter.Button(win,text=0,padx=42,pady=30,command=lambda:OnClick(0)).grid(row=4,column=0);


def createFuncButtons():
    
    bEqual=tkinter.Button(win,text="=",padx=92,pady=30,command=lambda:OnClick("=")).grid(row=4,column=2,columnspan=2);
    bAdd=b9=tkinter.Button(win,text="+",padx=42,pady=30,command=lambda:OnClick("+")).grid(row=1,column=3);
    bSub=b9=tkinter.Button(win,text="-",padx=45,pady=30,command=lambda:OnClick("-")).grid(row=2,column=3);
    bDiv=b9=tkinter.Button(win,text="/",padx=45,pady=30,command=lambda:OnClick("/")).grid(row=3,column=3);
    bMul=b9=tkinter.Button(win,text="x",padx=42,pady=30,command=lambda:OnClick("*")).grid(row=4,column=1);
    bDecimal=tkinter.Button(win,text=".",padx=44,pady=30,command=lambda:OnClick(".")).grid(row=5,column=0);
    bC=tkinter.Button(win,text="C",padx=42,pady=30,command=lambda:OnClick('c')).grid(row=5,column=1);
    bCE=tkinter.Button(win,text="Clear All",padx=70,pady=30,command=lambda:OnClick("ce")).grid(row=5,column=2,columnspan=2);

inputField=tkinter.Entry(win,width=20,borderwidth=2,fg="#696969",bg="#d3d3d3",highlightbackground="#d8d8d8",font=("Arial",26),state=DISABLED,disabledforeground="#696969");
inputField.grid(row=0,column=0,columnspan=4,padx=5,pady=10);
    
if __name__=="__main__":
    
    createNumButtons();
    createFuncButtons();

    win.mainloop();
