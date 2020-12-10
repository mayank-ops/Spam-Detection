from tkinter import *
import spam as sp

def GetResult():
    email=str(inp.get("1.0",END))
    if(len(email)>1):
        res=sp.detect_spam(email)
        out.delete("1.0",END)
        out.insert("1.0",res)

if __name__ == "__main__":
    sp.load_saved_artifacts()

    root = Tk()
    root.title("Spam Detection")

    Label(root, text="Enter Email: ").grid(row=0)

    inp = Text(root, width="35", height="2", bd=2)
    inp.grid(row=0, column=1, columnspan=1, rowspan=1, padx=20, pady=20)

    detect_Button = Button(root, text="Get Result", command=GetResult, padx=10, pady=5)
    detect_Button.grid(row=1, column=1)

    out = Text(root, width="35", height="2", bd=2)
    out.grid(row=2, column=1, columnspan=1, rowspan=1, padx=20, pady=20)

    root.mainloop()