from tkinter import *
import tkinter.messagebox

class DataInOut:
    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('300x150+0+0')

        frame1 = Frame(self.root)
        frame1.grid()

        frame2 = Frame(frame1)
        frame2.grid(row=0, column=0)

        frame3 = Frame(frame1)
        frame3.grid(row=2, column=1)

        self.FirstNum = StringVar()
        self.SecondNum = StringVar()
        self.HasilNum = StringVar()

        self.lblFirstNum = Label(frame2, text='Enter First Number')
        self.lblFirstNum.grid(row=0, column=0) 
        self.txtFirstNum = Entry(frame2, textvariable=self.FirstNum)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum = Label(frame2, text='Enter Second Number')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum = Entry(frame2, textvariable=self.SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

        self.lblHasil = Label(frame2, text='Hasil')
        self.lblHasil.grid(row=2, column=0)
        self.txtHasil = Entry(frame2, textvariable=self.HasilNum)
        self.txtHasil.grid(row=2, column=1)

        self.btnJumlahkan = Button(frame3, text='Jumlahkan', command=self.jumlahkan)
        self.btnJumlahkan.grid(row=2, column=0)
        
        self.btnReset = Button(frame3, text='Reset', command=self.reset)
        self.btnReset.grid(row=2, column=1)
        
        self.btnKeluar = Button(frame3, text='Keluar', command=self.keluar)
        self.btnKeluar.grid(row=2, column=2)

    def jumlahkan(self):
        try:
            pertama = float(self.FirstNum.get())
            kedua = float(self.SecondNum.get())
            hasil = pertama + kedua
            self.HasilNum.set(hasil)
        except ValueError:
            tkinter.messagebox.showerror("Error", "Invalid input, please enter numeric values.")

    def reset(self):
        self.FirstNum.set("")
        self.SecondNum.set("")
        self.HasilNum.set("")

    def keluar(self):
        self.root.quit()

if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()
