from tkinter import*
root = Tk()
def keel():
    keeli=Tk()
    keeli.geometry("500x90")
    keele=Label(keeli, text="õpetaja: Mihhailova Ljudmila B 221", font="Calibri 26")
    keele.pack()
def keemia():
    keemi=Tk()
    keemi.geometry("500x90")
    keeme=Label(keemi, text="õpetaja: Pesetskaja Svetlana B 144", font="Calibri 26")
    keeme.pack()
def log():
    Logis=Tk()
    Logis.geometry("500x90")
    logi=Label(Logis, text="õpetaja: Klimanskaja Inessa B 002", font="Calibri 26")
    logi.pack()
def Ees_2():
    Eesti_2=Tk()
    Eesti_2.geometry("500x90")
    Eest_2=Label(Eesti_2, text="õpetaja: Ojamäe Olesja B 234", font="Calibri 26")
    Eest_2.pack()    
def mat():
    mate=Tk()
    mate.geometry("500x90")
    matem=Label(mate, text="õpetaja: Voronova Nadezda B 133", font="Calibri 26")
    matem.pack()    
def program():
    programi=Tk()
    programi.geometry("500x90")
    programe=Label(programi, text="õpetaja: Oleinik Marina E 07", font="Calibri 26")
    programe.pack()
def kunsti():
    kunstii=Tk()
    kunstii.geometry("500x90")
    kunstie=Label(kunstii, text="õpetaja: Norkevit Aleksandra B 232", font="Calibri 26")
    kunstie.pack()
def kehal():
    kehali=Tk()
    kehali.geometry("500x90")
    kehale=Label(kehali, text="õpetaja: Maksõmiv Maksim Võimla A", font="Calibri 26")
    kehale.pack()
def rakes():
    rakesi=Tk()
    rakesi.geometry("500x90")
    rakese=Label(rakesi, text="õpetaja: Merkulova Irina E 10", font="Calibri 26")
    rakese.pack()
def rüh():
    rühi=Tk()
    rühi.geometry("550x90")
    rühe=Label(rühi, text="õpetaja: olesja B 234", font="Calibri 26")
    rühe.pack()
def ingl():
    ingli=Tk()
    ingli.geometry("500x90")
    ingle=Label(ingli_2, text="õpetaja: Borodina Olga B 227", font="Calibri 26")
    ingle.pack()
Label(text="0:").grid(row=0, column=1)
Label(text="1:").grid(row=0, column=2)
Label(text="2:").grid(row=0, column=3)
Label(text="3:").grid(row=0, column=4)
Label(text="4:").grid(row=0, column=5)
Label(text="5:").grid(row=0, column=6)
Label(text="6:").grid(row=0, column=7)
Label(text="7:").grid(row=0, column=8)
Label(text="8:").grid(row=0, column=9)
Label(text="9:").grid(row=0, column=10)
Label(text="10:").grid(row=0, column=11)
Label(text=" ").grid(row=0, column=0)
Label(text="Esmaspäev").grid(row=1, column=0)
Label(text="Teisipäev ").grid(row=2, column=0)
Label(text="Kolmapäev ").grid(row=3, column=0)
Label(text="Neljapäev ").grid(row=4, column=0)
Label(text="Reede ").grid(row=5, column=0)
Label(text=" ",font="Arial,50",width=10,height=3,bg="white",relief=RIDGE).grid(row=1, column=1,sticky=W+E+N+S,)
Button(text=" eesti ",font="Arial,50",width=10,height=3,bg="grey",relief=RIDGE,command=Ees_2).grid(row=1, column=2,sticky=W+E+N+S,)
Button(text="Logistika teenused ",font="Arial,50",width=20,height=3,bg="green",relief=RIDGE,command=log).grid(row=1, column=3,columnspan=2,sticky=W+E+N+S,)
Button(text="Matemaatika ",font="Arial,50",width=10,height=3,bg="pink",relief=RIDGE,command=mat).grid(row=1, column=5,sticky=W+E+N+S,)
Button(text="Matemaatika ",font="Arial,50",width=10,height=3,bg="pink",relief=RIDGE,command=mat).grid(row=1, column=6,sticky=W+E+N+S)
Button(text=" ",font="Arial,50",width=10,height=3,bg="white",relief=RIDGE).grid(row=1, column=7,sticky=W+E+N+S)
Button(text="keel ja\n kirjandus ",font="Arial,50",width=10,height=3,bg="lightgreen",relief=RIDGE,command=keel).grid(row=1, column=8,sticky=W+E+N+S)
Button(text="keel ja\n kirjandus ",font="Arial,50",width=10,height=3,bg="lightgreen",relief=RIDGE,command=keel).grid(row=1, column=9,sticky=W+E+N+S)
Button(text="tugiõppe\nmatemaatika ",font="Arial,50",width=10,height=3,bg="pink",relief=RIDGE,command=mat).grid(row=1, column=10,sticky=W+E+N+S)
Button(text=" ",font="Arial,50",width=20,height=3,bg="white",relief=RIDGE).grid(row=2, column=1,sticky=W+E+N+S)
Button(text="tugiõppe ",font="Arial,50",width=10,height=3,bg="purple",relief=RIDGE,command=keemia).grid(row=2, column=2,sticky=W+E+N+S)
Button(text="Programmeerimise alused ",font="Arial,50",width=30,height=3,bg="lightblue",relief=RIDGE,command=program).grid(row=2, column=4,columnspan=1,sticky=W+E+N+S)
Button(text=" ").grid(row=2, column=5,sticky=W+E+N+S)
Button(text="Füüsika ",font="Arial,50",width=20,height=3,bg="pink",relief=RIDGE,command=mat).grid(row=2, column=6,columnspan=2,sticky=W+E+N+S)
Button(text=" ").grid(row=3, column=1,sticky=W+E+N+S)
Button(text="tugiõppe ",font="Arial,50",width=10,height=3,bg="purple",relief=RIDGE,command=Ees_2).grid(row=3, column=2,sticky=W+E+N+S)
Button(text="kunstiained ",font="Arial,50",width=20,height=3,bg="purple",relief=RIDGE,command=kunsti).grid(row=3, column=3,columnspan=2,sticky=W+E+N+S)
Button(text=" ").grid(row=3, column=5,sticky=W+E+N+S)
Button(text="Kehaline kasvatus ",font="Arial,50",width=20,height=3,bg="purple",relief=RIDGE,command=kehal).grid(row=3, column=6,columnspan=2,sticky=W+E+N+S)
Button(text=" ").grid(row=3, column=8,sticky=W+E+N+S)
Button(text=" ").grid(row=3, column=9,sticky=W+E+N+S)
Button(text=" ").grid(row=3, column=10,sticky=W+E+N+S)
Button(text="Logistika\nteenused ",font="Arial,50",width=20,height=3,bg="green",relief=RIDGE,command=log).grid(row=4, column=1,columnspan=2,sticky=W+E+N+S)
Button(text=" ").grid(row=4, column=3,sticky=W+E+N+S)
Button(text="Programmerimise\nalused ",font="Arial,50",width=20,height=3,bg="lightblue",relief=RIDGE,command=program).grid(row=4, column=4,columnspan=2,sticky=W+E+N+S)
Button(text="rakes ",font="Arial,50",width=20,height=3,bg="red",relief=RIDGE,command=rakes).grid(row=4, column=6,columnspan=2,sticky=W+E+N+S)
Button(text="Eesti keel ",font="Arial,50",width=20,height=3,bg="grey",relief=RIDGE,command=Ees_2).grid(row=4, column=8,columnspan=2)
Button(text=" ").grid(row=4, column=9,)
Button(text=" ").grid(row=5, column=0,sticky=W+E+N+S)
Button(text="Rakes ",font="Arial,50",width=40,height=3,bg="red",relief=RIDGE,command=rakes).grid(row=5, column=1,columnspan=2,sticky=W+E+N+S)
Button(text="Programmerimise alused(eesti keeles) ",font="Arial,50",width=65,height=3,bg="lightblue",relief=RIDGE,command=program).grid(row=5, column=3,columnspan=7,sticky=W+E+N+S)
Button(text="Inglise keel",font="Arial,50",width=20,height=3,bg="lightgreen",relief=RIDGE,command=ingl).grid(row=5, column=9,columnspan=2,)
Button(text=" ").grid(row=5, column=10,)













root.mainloop()




