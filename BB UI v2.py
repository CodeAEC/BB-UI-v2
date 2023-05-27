from tkinter import *
from tkinter import messagebox
	
def play():
	play_window = Tk()
	play_window.geometry("500x250")
	play_window.title("Builder Buddies")
	play_window.config(background="light Green")
	main_window.destroy()

#   chat log button
	button = Button(play_window,
		            relief=RAISED,
		            bg="Black",
		            fg="black",
		            padx=100,
		            pady=7,)
	button.place(x=35,y=0)

#   button to enter the chat and talk
	button = Button(play_window,
		            bg="Grey",
		            fg="Grey",
		            padx=15,
		            pady=7,)
	button.place(x=0, y=0)

#   Button for gold or want to buy gold
	button = Button(play_window,
		            bg="Yellow",
		            fg="black",
		            padx=15,
		            pady=7,)
	button.place(x=465, y=0)

#   Button to check the gems or want to buy
	button = Button(play_window,
		            bg="Green",
		            fg="Black",
		            padx=15,
		            pady=7,)
	button.place(x=430, y=0)

#   button to move
	button = Button(play_window,
		            text="Move",
		            font=('Arial',15,'bold'),
		            bg="Black",
		            fg="White",
		            padx=25,
		            pady=30,)
	button.place(x=0, y=150)

#   button to enter shop
	button = Button(play_window,
		            text="Shop",
		            font=('Arial',13,'bold'),
		            bg="Grey",
		            fg="White",
		            padx=20,
		            pady=4)
	button.place(x=407, y=210)



	play_window.mainloop()
	



def ive():
     
    # Message box for icloud 
	def Cacc():
		messagebox.showinfo(title='Locating Account',
			                message='No account found in iCloud!')

    # Message box for Game Center
	def Gacc():
		messagebox.showinfo(title='Locating Account',
			                message='No account found in Game Center')


	def cancel():
		ive_window.destroy()



#   the Window to find the account that you used to play before
	ive_window = Tk()
	ive_window.geometry("500x250")
	ive_window.title("Builder Buddies")
	ive_window.config(background="Grey")


	label = Label(ive_window,
		          text="Restore Account",
		          font=('Arial',15,'bold'),
		          bg="Grey",
		          fg="White")
	label.pack()

	label = Label(ive_window,
		          text="Restore your account using one of these services.",
		          font=('Arial',15,'bold'),
		          bg="Grey",
		          fg="White")
	label.place(x=7,y=80)

#   button for checking icloud for an account
	button = Button(ive_window,
		            text="iCloud",
                    relief=RAISED,  
                    font=('Arial',15,'bold'),
		            bg="Grey",
		            fg="White",
		            command=Cacc,
		            padx=60,
		            pady=5)
	button.place(x=50,y=110)

#   button for checking is there an account in GameCenter
	button = Button(ive_window,
		            text="Game Center",
		            relief=RAISED,
		            bd=3,
		            font=('Arial',15,'bold'),
		            bg="Grey",
		            fg="White",
		            padx=25,
		            pady=5,
		            command=Gacc)
	button.place(x=255,y=110)

#   button to cancel the operation
	button = Button(ive_window,
		            text="Canel",
		            relief=RAISED,
		            bd=3,
		            font=('Arial',15,'bold'),
		            bg="Grey",
		            fg="White",
		            padx=60,
		            pady=5,
		            command=cancel,)
	button.place(x=155,y=167)

	ive_window.mainloop()





main_window = Tk()
main_window.geometry("500x250")
main_window.title("Builder Buddies")
main_window.config(background="Grey")


label = Label(main_window, 
	          text="BUILDER BUDDIES",
	          font=('Arial',20,'bold'),
	          bg='Grey',
	          fg='White')
label.pack(side=TOP)

label = Label(main_window,
	          text="Don Arifi LLC",
	          font=('Arial',12,'bold'),
	          bg="Grey",
	          fg="White",)
label.place(x=5,y=230)

label = Label(main_window,
	          text="v.1.0.1",
	          font=('Arial',12,'bold'),
	          bg="Grey",
	          fg="White",)
label.place(x=440,y=230)

# button to enter the game
button = Button(main_window,
	            text="Play",
	            font=('Arial',20,'bold'),
	            bg='Grey',
	            fg='White',
	            command=play,
	            padx=30,
	            relief=RAISED,
	            bd=5)
button.place(x=180,y=100)

# this button is for those  who played before
ive_button = Button(main_window,
	                text="I've Played Before",
	                font=('Arial',7,'bold'),
	                pady=5,
	                bg='Grey',
	                command=ive,
	                fg='White')
ive_button.place(x=5,y=200)



main_window.mainloop()
