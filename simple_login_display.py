from tkinter import*
from PIL import ImageTk
from tkinter import messagebox

class Login:
      def __init__(self,root):

            # creating pop up window
            self.root = root
            self.root.title("Login System")
            self.root.geometry("900x700+100+50")
            self.root.resizable(False,False)

            #Imposing Background Image
            self.bg = ImageTk.PhotoImage(file= "Images/Naruto.png")
            self.bg_image = Label(self.root,image = self.bg).place(x=0,y=0,relwidth=1,relheight=1)

            #Making a white frame
            Frame_login = Frame(self.root, cursor ="hand1", bg = "white")
            Frame_login.place(x=260,y=350,height=300,width=430)

            #labeling texts
            title = Label(Frame_login,text="Login here",font=("Impact",35,"bold"),fg='#d77337',bg = "white").place(x=50,y=10)
            desc = Label(Frame_login,text="Employee login area",font=("Goudy old style",15,"bold"),bg = "white").place(x=50,y=80)
            lbl_user = Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg='grey',bg = "white").place(x=50,y=120)   

            #Entry Field

            self.txt_user = Entry(Frame_login,font=("times new roman",15),bg = 'lightgray')
            self.txt_user.place(x=50,y=150,width=350,height=35)

            #label and entry field for password
            lbl_pass = Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg='grey',bg = "white").place(x=50,y=190)   
            self.txt_pass = Entry(Frame_login,font=("times new roman",15),bg = 'lightgray')
            self.txt_pass.place(x=50,y=220,width=350,height=35)

            #forget pass and login button
            forget_btn = Button(Frame_login, cursor ="hand2", text = "Forgot Password?",bg = 'white', fg = '#d77337', bd = 0, font=("times new roman", 10)).place(x =50, y = 255) 
            login_btn = Button(self.root, command = self.login_func, cursor ="hand2", text = "Login", fg = 'white', bg = '#d77337', font=("times new roman", 20)).place(x =390, y = 630, width = 180, height = 40) 
      
      def login_func(self):
            if self.txt_pass.get() == "" or self.txt_user.get() == "":
                  messagebox.showerror("Error", "All fields are required",parent = self.root)
            elif self.txt_pass.get() != "12345" or self.txt_user.get() != "Aakash":
                  messagebox.showerror("Error", "Invalid User",parent = self.root)
            else:
                  messagebox.showinfo("Welcome",f"Welcome {self.txt_user.get()}")

root = Tk()
obj = Login(root)
root.mainloop()
