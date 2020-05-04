from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import re

# Set the colors
colorBg = "#dbb6fc"
colorTxt = "#7909ba"
colorAns = "#9186db"

# Set the window
root= Tk()
root.title("Aplicatie de dubla cifrare")
root.geometry("650x325")
root['background']= colorBg

# Top frame
Tops = Frame(root, width = 600,height=50, bg=colorBg) 
Tops.pack(side = TOP) 

 
f1 = Frame(root, width = 220, height = 280, relief = SUNKEN,bg=colorBg) 
f1.pack(side = LEFT) 

f2 = Frame(root, width = 480, height = 280, relief = SUNKEN,bg=colorBg) 
f2.pack(side = LEFT) 


lblTitle = Label(Tops, font = ('times', 20, 'bold'), text = "CRIPTOGRAFIE SI SECURITATE \n Aplicatie de dubla cifrare",
				fg = colorTxt, bd = 10, anchor='w',bg=colorBg) 
lblTitle.grid(row = 0, column = 0) 

lblQ1 = Label(f1, font=("times",15,"bold"), text = "Cifrul utilizat este:", fg=colorTxt, anchor = "n", bg =colorBg )
lblQ1.pack(side=TOP)

Label(f1,font=("times",3,"bold"),text="  ",bg=colorBg).pack()



optionCipher= StringVar()
optionCipher.set("Cifrul Cezar")
values = {"Cifrul Cezar":"Cifrul Cezar","Cifrul Polybius":"Cifrul Polybius"}
for text, option in values.items():
	Radiobutton(f1, font=("times",12,"bold"), text = text, variable = optionCipher, value = option, fg=colorAns, bg =colorBg,anchor = "w",activebackground=colorBg,activeforeground=colorTxt).pack(side = TOP, ipady = 5) 

global flag
flag = False


def Reset():
	caesar.delete(0,END)
	polybius.delete(0,END)
	numefisier.pack_forget()
	flag =False

global numefisier

def openFct():
	global numefisier
	global data
	global name
	global flag
	name = askopenfilename(initialdir="C:/Users/Spinu/Desktop/GUI",title = "Choose a file.",filetypes =(("Text File", "*.txt"),("All Files","*.*")))
	print (name)
	with open(name) as file:  
		data = file.read()
	print(data)
	regex = re.compile('[@_!#$%^&*()<>0123456789?/\\|}{~:]') 
	OptAleasa=optionCipher.get()
	print(OptAleasa) 
	if(OptAleasa=="Cifrul Cezar"):
		if(regex.search(data) == None): 
			print("String is accepted")
			flag=True
		else: 
			print("String is not accepted.")
			messagebox.showerror("Eroare","Fisierul ales contine caractere necorespunzatoare!\nEste necesara alegerea unui alt fisier!")
	else:
		flag=True
	if flag== True:
		numefisier=Label(f1,font=("times",8,"bold"),text=name,fg = colorTxt,bg=colorBg)
		numefisier.pack()
		
		
def afisFct():
	if flag ==True:
		window = Toplevel(root)
		window.title(name)
		window.geometry("300x50")
		window['background']= colorBg
		Label(window,font=("times",12,"bold"),text=data,fg = colorTxt,bg=colorBg).pack()
	else:
		messagebox.showwarning("Warning","Nu a fost selectat un fisier valid inca !")


Label(f1,font=("times",6,"bold"),text="  ",bg=colorBg).pack()

InputF_btn = Button(f1,font=("times",12,"bold"),text="Alege fisier!    ",fg=colorAns, bg =colorTxt,anchor = "e",bd=5,padx=32,activebackground=colorAns,activeforeground=colorBg,command= openFct).pack(padx=3,pady=3)
InputF_btn = Button(f1,font=("times",12,"bold"),text="Afiseaza inputul!",fg=colorAns, bg =colorTxt,anchor = "w",bd=5,padx=25,activebackground=colorAns,activeforeground=colorBg,command= afisFct).pack(padx=3,pady=3)



Label(f2, font=("times",15,"bold"), text = " Cheie cifrul Cezar", anchor = "center",fg=colorTxt, bg =colorBg ).grid(row=0,column=0)
caesar= Entry(f2,font=("times",15,"bold"),bd=5,bg=colorTxt,fg=colorAns,width=20)
caesar.grid(row=0,column=1)

Label(f2, font=("times",2,"bold"), text = " ", anchor = "center",fg=colorTxt, bg =colorBg ).grid(row=1,column=0)


Label(f2, font=("times",15,"bold"), text = " Cheie cifrul Polybius", anchor = "center",fg=colorTxt, bg =colorBg ).grid(row=2,column=0)
polybius= Entry(f2,font=("times",15,"bold"),bd=5,bg=colorTxt,fg=colorAns,width=20)
polybius.grid(row=2,column=1)


def Valideaza():
	OptAleasa=optionCipher.get()
	print(OptAleasa) 
	if(OptAleasa=="Cifrul Cezar"):
		if(caesar.get().isnumeric() and (int(caesar.get())>=0 and int(caesar.get())<=25)):
			print("cheia este ok")
			messagebox.showinfo("Info","Cheia aleasa este corecta!")
		else:
			messagebox.showerror("Eroare","Cheia introdusa trebuie sa fie un numar\ncu valori intre 0 si 25")
			caesar.delete(0,END)
	elif(OptAleasa=="Cifrul Polybius"):
		regex = re.compile('[@_!#$%^&*()<>0123456789?/\\| }{~:]') 
		if(regex.search(polybius.get()) == None): 
			print("cheia este ok")
			messagebox.showinfo("Info","Cheia aleasa este corecta!")
		else:
			messagebox.showerror("Eroare","Cheia introdusa nu este valida")
			polybius.delete(0,END)

Label(f2, font=("times",1,"bold"), text = " ", anchor = "center",fg=colorTxt, bg =colorBg ).grid(row=3,column=0)
validBtn=Button(f2,font=("times",12,"bold"),text="Valideaza cheia",fg=colorAns, bg =colorTxt,anchor = "e",bd=5,padx=32,activebackground=colorAns,activeforeground=colorBg,command= Valideaza).grid(row=4,column=0,columnspan=2,padx=3,pady=3)



def Encrypt():
	OptAleasa=optionCipher.get()
	print(OptAleasa) 
	if(OptAleasa=="Cifrul Cezar"):
		result=""
		for i in range(len(data)):
			char = data[i]
			if (char.isupper()):
				if(char==" "):
					result+=""
				else:
					result += chr((ord(char) + int(caesar.get())-65) % 26 + 65)
			else:
				if(char==" "):
					result+=""
				else:
					letter = chr((ord(char) + int(caesar.get()) - 97) % 26 + 97)
					result +=chr(ord(letter)-32)
		print("rezultatul este  "+result)
		f = open("outCrC.txt", "w")
		f.write(result)
		f.close()
	elif(OptAleasa=="Cifrul Polybius"):
		alpha = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
		key=polybius.get().upper()
		new_alphabet=""
		for i in key:
			for j in alpha:
				if (i==j):
					new_alphabet+=i
					alpha=alpha.replace(j,"")
					print(alpha)
		print("alfa ramas"+ alpha)
		new_alphabet+=alpha
		print("alfabet   "+new_alphabet)
		matrix = [	[new_alphabet[0],new_alphabet[1],new_alphabet[2],new_alphabet[3],new_alphabet[4]],
					[new_alphabet[5],new_alphabet[6],new_alphabet[7],new_alphabet[8],new_alphabet[9]],
					[new_alphabet[10],new_alphabet[11],new_alphabet[12],new_alphabet[13],new_alphabet[14]],
					[new_alphabet[15],new_alphabet[16],new_alphabet[17],new_alphabet[18],new_alphabet[19]],
					[new_alphabet[20],new_alphabet[21],new_alphabet[22],new_alphabet[23],new_alphabet[24]]
				]
		print(matrix)
		datanoi=data.replace(" ","")
		datanoi=datanoi.upper()
		datanoi=datanoi.replace("I","J")

		result=""
		for char in datanoi:
			for index, row in enumerate(matrix):
				if char in row:
					result+=str(index+1)+str(row.index(char)+1)
		print("rezultatul este  "+result)
		f = open("outCrP.txt", "w")
		f.write(result)
		f.close()



	
def Decrypt():
	OptAleasa=optionCipher.get()
	print(OptAleasa) 
	if(OptAleasa=="Cifrul Cezar"):
		message = data.upper()
		alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		space = " "
		output=""
		for i in message:
			if i in alpha:
				letter_index = (alpha.find(i)-int(caesar.get()))%len(alpha)
				result= result+alpha[letter_index]
			elif (i==space):
				result+=""

		print("rezultatul este  "+result)
		f = open("outdecC.txt", "w")
		f.write(result)
		f.close()
	elif(OptAleasa=="Cifrul Polybius"):
		message=data
		alpha = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
		key=polybius.get().upper()
		new_alphabet=""
		for i in key:
			for j in alpha:
				if (i==j):
					new_alphabet+=i
					alpha=alpha.replace(j,"")
					print(alpha)
		print("alfa ramas"+ alpha)
		new_alphabet+=alpha
		print("alfabet   "+new_alphabet)
		matrix = [	[new_alphabet[0],new_alphabet[1],new_alphabet[2],new_alphabet[3],new_alphabet[4]],
					[new_alphabet[5],new_alphabet[6],new_alphabet[7],new_alphabet[8],new_alphabet[9]],
					[new_alphabet[10],new_alphabet[11],new_alphabet[12],new_alphabet[13],new_alphabet[14]],
					[new_alphabet[15],new_alphabet[16],new_alphabet[17],new_alphabet[18],new_alphabet[19]],
					[new_alphabet[20],new_alphabet[21],new_alphabet[22],new_alphabet[23],new_alphabet[24]]
				]
		print(matrix)
		message=str(message)
		print(len(message))
		print("message "+message)

		result=""
		for i in range(len(message)):
		    if (i%2==0):
		    	result+=matrix[int(message[i])-1][int(message[i+1])-1]


		print("rezultatul este  "+result)
		f = open("outDecP.txt", "w")
		f.write(result)
		f.close()
		




def ShowOut():
	window = Toplevel(root)
	window.title("Fereastra Output")
	window.geometry("400x50")
	window['background']= colorBg
	name2 = askopenfilename(initialdir="C:/Users/Spinu/Desktop/GUI",title = "Choose a file.",filetypes =(("Text File", "*.txt"),("All Files","*.*")))
	print (name2)
	with open(name2) as file:  
		dataOut = file.read()
	print(dataOut)
	Label(window,font=("times",12,"bold"),text=dataOut,fg = colorTxt,bg=colorBg).pack()
	

encryptBtn=Button(f2,font=("times",12,"bold"),text="Encrypt",fg=colorAns, bg =colorTxt,anchor = "e",bd=5,width=20,activebackground=colorAns,activeforeground=colorBg,command= Encrypt).grid(row=6,column=0,padx=3,pady=3)
decryptBtn=Button(f2,font=("times",12,"bold"),text="Decrypt",fg=colorAns, bg =colorTxt,anchor = "e",bd=5,width=20,activebackground=colorAns,activeforeground=colorBg,command= Decrypt).grid(row=6,column=1,padx=3,pady=3)


ShowOutBtn=Button(f2,font=("times",12,"bold"),text="Afiseaza outputul",fg=colorAns, bg =colorTxt,anchor = "e",bd=5,width=20,activebackground=colorAns,activeforeground=colorBg,command= ShowOut).grid(row=8,column=0,padx=3,pady=3)
ResetBtn=Button(f2,font=("times",12,"bold"),text="Reset",fg=colorAns, bg =colorTxt,anchor = "e",bd=5,width=20,activebackground=colorAns,activeforeground=colorBg,command= Reset).grid(row=8,column=1,padx=3,pady=3)




root.mainloop()