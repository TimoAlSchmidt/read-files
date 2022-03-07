import tkinter, yaml
from tkinter import ttk

def removeWidgets():
    for widget in window.winfo_children():
        widget.destroy()

def removeSpecificWidgets():
    for widget in window.winfo_children():
        if "Welke smaak" in widget.cget("text") or type(widget) is ttk.Button or type(widget) is ttk.Radiobutton:
            widget.destroy()

def labelMaker(texter):
    label = ttk.Label(window, text=texter)
    label.grid()

def entryMaker(texter=None):
    entry = ttk.Entry(window, text=texter)
    entry.grid()

def buttonMaker(texter, comma, stater="enabled"):
    button = ttk.Button(window, text=texter, command=comma, state=stater)
    button.grid()

def buttonEnabler():
    for widget in window.winfo_children():
        if type(widget) is ttk.Button:
            widget.configure(state="enabled")

def yesOrNo(yes, no, var, quest, comma=None):
    labelMaker(quest)
    g = ttk.Radiobutton(window, value=yes, text=yes,variable=var,command=comma)
    g.grid()
    g = ttk.Radiobutton(window, value=no, text=no,variable=var,command=comma)
    g.grid()

def printError():
    print("Sorry dat is geen optie die we aanbieden...")

def vraagOmNummer(completeVraag):
    while True:
        try:
            nummer = int(input(completeVraag+"\n"))
            return nummer
        except:
            printError()    

def vraagOmTekst(completeVraag, keuzes):
    while True:
        try:
            woord = input(completeVraag+"\n")
            if woord in keuzes:
                return woord
        except: 
            printError()

def stapEen():
    removeWidgets()
    if particulier.get() == "Particulier":
        particulierEen()
    else:
        zakelijkEen()

def particulierEen():
    removeWidgets()
    labelMaker("Hoeveel bolletjes wilt u?")
    entryMaker(bolletjes)
    buttonMaker("Verder gaan", lambda:particulierTwee())

def particulierTwee():
    global bakje, bakjesAantal, smaken, bolletjesTotaal, bolletjesAantal
    removeWidgets()
    bolletjesAantal = int(bolletjes.get())
    bolletjesTotaal += bolletjesAantal
    smaken = bolletjesAantal
    if bolletjesAantal > 3 and bolletjesAantal <= 8:
        bakje = True
        bakjesAantal += 1
        labelMaker("Dan krijgt u van mij een bakje met "+str(bolletjesAantal)+" bolletjes.")
    elif bolletjesAantal > 8:
        labelMaker("Sorry, zulke grote bakjes hebben we niet.")
        return particulierEen()
    particulierDrie()

def particulierDrie():
    global smaken, bolletjesAantal
    if smaken > 0:
        removeSpecificWidgets()
        smaken -= 1
        labelMaker("Welke smaak wilt u voor bolletje nummer "+str(bolletjesAantal-smaken)+"?")
        g = ttk.Radiobutton(window, value="Aardbei", text="Aardbei",variable=smakenen,command=particulierDrie)
        g.grid()
        g = ttk.Radiobutton(window, value="Chocolade", text="Chocolade",variable=smakenen,command=particulierDrie)
        g.grid()
        g = ttk.Radiobutton(window, value="Vanille", text="Vanille",variable=smakenen,command=particulierDrie)
        g.grid()
    else:
        particulierVier()

def particulierVier():
    removeWidgets()
    if not bakje:
        print("Not bakje")
        yesOrNo("Hoorntje","Bakje", hoor, "Wilt u deze "+str(bolletjesAantal)+" bolletje(s) in een hoorntje of een bakje?", lambda:buttonEnabler())
        buttonMaker("Verder gaan", lambda:particulierVijf(), "disabled")
    else:
        hoor.set("")
        particulierVijf()

def particulierVijf():
    global bakjesAantal, horrentjesAantal
    removeWidgets()
    if hoor.get == "Hoorntje":
        bakjesAantal += 1
        bakje = True
    else:
        horrentjesAantal += 1
        bakje = False
    labelMaker("Wat voor topping wilt u:")
    g = ttk.Radiobutton(window, value="A", text="Geen",variable=topping,command=particulierZes)
    g.grid()
    g = ttk.Radiobutton(window, value="B", text="Slagroom",variable=topping,command=particulierZes)
    g.grid()
    g = ttk.Radiobutton(window, value="C", text="Sprinkels",variable=topping,command=particulierZes)
    g.grid()
    g = ttk.Radiobutton(window, value="D", text="Caramel Saus",variable=topping,command=particulierZes)
    g.grid()

def particulierZes():
    global toppingPrijzen, toppingTotaalPrijs
    removeWidgets()
    nummer = ord(topping.get())-66
    if nummer >= 0:
        toppingTotaalPrijs += toppingPrijzen[nummer]

    bakje = False
    houder = ("hoorntje", "bakje")[bakje]
    yesOrNo("Yes", "No", bestellen, "Hier is uw "+houder+" met "+str(bolletjesAantal)+" bolletje(s). Wilt u nog iets bestellen?", lambda: particulierZeven())

def particulierZeven():
    global toppingTotaalPrijs
    removeWidgets()
    if bestellen.get() == "Yes":
        particulier.set("")
        bolletjes.set("0")
        smakenen.set("")
        hoor.set("")
        topping.set("")
        bestellen.set("")
        particulierEen()
    else:
        bolletjesTotaalPrijs = round(bolletjesTotaal * bolletjesPrijs, 2)
        horrentjesTotaalPrijs = round(horrentjesAantal * horrentjesPrijs, 2)
        bakjesTotaalPrijs = round(bakjesAantal * bakjesPrijs, 2)
        toppingTotaalPrijs = round(toppingTotaalPrijs, 2)
        labelMaker("------[\"Papi Gelato\"]------\n")
        if bolletjesTotaal > 0:
            labelMaker("Bolletjes    "+str(bolletjesTotaal)+" x €"+str(bolletjesPrijs)+"  = €"+str(bolletjesTotaalPrijs))
        
        if horrentjesAantal > 0:
            labelMaker("Horrentjes    "+str(horrentjesAantal)+" x €"+str(horrentjesPrijs)+"  = €"+str(horrentjesTotaalPrijs))
        
        if bakjesAantal > 0:
            labelMaker("Bakjes    "+str(bakjesAantal)+" x €"+str(bakjesPrijs)+"  = €"+str(bakjesTotaalPrijs))

        if toppingTotaalPrijs > 0:
            labelMaker("Topping      1 x €"+str(toppingTotaalPrijs)+"  = €"+str(toppingTotaalPrijs))


        labelMaker("Bedankt en tot ziens!")

def zakelijkEen():
    global smaken
    removeWidgets()
    labelMaker("Hoeveel liters wilt u?")
    entryMaker(bolletjes)
    buttonMaker("Verder gaan", lambda: zakelijkAnderhalf())

def zakelijkAnderhalf():    
    global smaken, bolletjesAantal
    bolletjesAantal = int(bolletjes.get())
    smaken = bolletjesAantal
    zakelijkTwee()

def zakelijkTwee():
    global smaken, bolletjesAantal
    if smaken > 0:
        removeWidgets()
        smaken -= 1
        labelMaker("Welke smaak wilt u voor liter nummer "+str(bolletjesAantal-smaken)+"?")
        g = ttk.Radiobutton(window, value="Aardbei", text="Aardbei",variable=smakenen,command=zakelijkTwee)
        g.grid()
        g = ttk.Radiobutton(window, value="Chocolade", text="Chocolade",variable=smakenen,command=zakelijkTwee)
        g.grid()
        g = ttk.Radiobutton(window, value="Vanille", text="Vanille",variable=smakenen,command=zakelijkTwee)
        g.grid()
    else:
        zakelijkDrie()

def zakelijkDrie():
    removeWidgets()
    litersTotaalPrijs = round(bolletjesAantal*litersPrijs, 2)
    labelMaker("---------[\"Papi Gelato\"]---------\n")
    labelMaker("Liter                "+str(bolletjesAantal)+" x "+str(litersPrijs)+" = €"+str(litersTotaalPrijs))
    labelMaker("                            ------")
    labelMaker("Totaal                      = €"+str(litersTotaalPrijs))
    labelMaker("BTW (9%)                    = €"+str(round(litersTotaalPrijs*btwPercent, 2)))

with open("settings.yml", "r") as file:
    settings = yaml.safe_load(file)

print(settings)
print(type)

window = tkinter.Tk()
window.title("Papi Gelato")

bakje = False
bolletjesTotaal = 0
bolletjesAantal = 0
bolletjesPrijs = settings["bolletjes"]
horrentjesAantal = 0
horrentjesPrijs = settings["hoorentjes"]
bakjesAantal = 0
bakjesPrijs = settings["bakjes"]
toppingTotaalPrijs = 0
toppingPrijzen = (settings["toppings"]["slagroom"], settings["toppings"]["bottetjes"], settings["toppings"]["caramel"]["hoorentje"], settings["toppings"]["caramel"]["bakje"])
litersAantal = 0
litersPrijs = settings["liter"]
btwPercent = settings["btw"]/100

particulier = tkinter.StringVar()
bolletjes = tkinter.IntVar()
smakenen = tkinter.StringVar()
hoor = tkinter.StringVar()
topping = tkinter.StringVar()
bestellen = tkinter.StringVar()


labelMaker("Welkom Bij Papi Gelato")
yesOrNo("Particulier", "Zakelijk",particulier, "Bent u particulier of zakelijk?", lambda:buttonEnabler())

buttonMaker("Verder gaan", lambda:stapEen(), "disabled")


window.mainloop()