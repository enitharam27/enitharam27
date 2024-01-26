from tkinter import *
from tkinter import messagebox
import ast
root=Tk()
root.title("SignUp")
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def signup():
    username=user.get()
    password=code.get()
    conform_password=conform_code.get()
    if password==conform_password:
        try:
            file=open('datasheet.txt','r+')
            d=file.read()
            r.ast.literal_eval(d)
            dict2={username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()
            file=open('datasheet.txt','w')
            w=file.write(str(r))
            messagebox.showinfo('signup','successfully sign up')
        except:
                file=open('datasheet.txt','w')
                pp=str({'username':'password'})
                file.write(pp)
                file.close()

        else:
                messagebox.showerror('Invalid',"both password should match")
            

img=PhotoImage(file="C:/Users/vignesh/Downloads/images.png")
Label(root,image=img,border=50,bg='white').place(x=10,y=100)
frame=Frame(root,width=350,height=390,bg="#fff")
frame.place(x=480,y=70)
heading=Label(frame,text='sign up',fg='#57a1f8',bg='white',font=('Microsoft yaHei UI Light',23,'bold'))
heading.place(x=100,y=5)
def on_enter(e):
    conform_code.delete(0,'end')
def on_leave(e):
    if conform_code.get()=='':
        conform_code.insert(0,'Username')
    if conform_code.get()=='':
        conform_code.insert(0,'password')
    if conform_code.get()=='':
        conform_code.insert(0,'conform password')

conform_code=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
conform_code.place(x=30,y=80)
conform_code.insert(0,'Username')
conform_code=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
conform_code.place(x=30,y=130)
conform_code.insert(1,'password')
conform_code=Entry(frame,width=25,fg='black',border=2,bg='white',font=('Microsoft Yahei UI Light',11))
conform_code.place(x=30,y=180)
conform_code.insert(1,'conform password')
conform_code.bind("<FocusIn>",on_enter)
conform_code.bind("<FocusOut>",on_leave)
Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)
Button(frame,width=39,pady=7,text='sign up',bg='#57a1f8',fg='white',border=0).place(x=35,y=280)
label=Label(frame,text='I have an account',fg='black',bg='white',font=('Microsoft yaHei UI Light',9))
label.place(x=90,y=340)
signin=Button(frame,width=6,text='sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8')
signin.place(x=200,y=340)
root.mainloop()
