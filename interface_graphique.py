 

from tkinter import *
window = Tk()
window.title("mini_projet_python")
window.geometry("1080x720")
window.iconbitmap("logo.ico")
window.config(background="#41B77F")
frame = Frame(window, bg="#41B77F")
label_title = Label(frame, text="Bienvenue sur notre mini projet ", font=("Courrier", 40), bg="#41B77F", fg='white')
label_title.pack()
label_title = Label(frame, text=" Hey salut à tous ", font=("Courrier", 25), bg="#41B77F", fg='white')
label_title.pack()


def complet():
    # création de la fenetre + paramétrage
    fg = Tk()
    fg.title("Mots_Complet")
    fg.geometry("720x720")
    fg.iconbitmap("logo.ico")
    label1 = Label(fg,
                   text="compter le nombre d’occurrences\n d'un mot dans les séquences\n  Déterminez  quel mot est le plus fréquent\n dans le protéome humain.  ",
                   font=("Courrier", 20), bg="white", fg="#000000")
    label1.pack()
    fg.mainloop()

def LM():


    # création de la fenetre + paramétrage
    fe = Tk()
    fe.title("Listes_Mots")
    fe.geometry("720x720")

    fe.iconbitmap("logo.ico")
    label1 = Label(fe,
                   text=" liste contenant les mots\n convertis en majuscule \n et composés de 3 caractères ou plus ",
                   font=("Courrier", 20), bg="white", fg="#000000")
    label1.pack()




    fe.mainloop()


def mseq():
    # création de la fenetre + paramétrage
    fk = Tk()
    fk.title("Mots_Sequences")
    fk.geometry("720x720")
    fk.iconbitmap("logo.ico")
    label1 = Label(fk,
                   text=" un dictionnaire dont les\n clefs sont les mots et les valeurs\n le nombre de séquences qui contiennent ces mot  ",
                   font=("Courrier", 20), bg="white", fg="#000000")

    label1.pack()
    fk.mainloop()


def seq():
    # création de la fenetre + paramétrage
    fq = Tk()
    fq.title("Dict_sequences")
    fq.geometry("720x720")
    fq.iconbitmap("logo.ico")
    label1 = Label(fq,
                   text=" dictionnaire dont les clefs\n sont les identifiants des protéines \n(par exemple, O95139, O75438) et \n dont les valeurs associées sont les séquences.  ",
                   font=("Courrier", 20), bg="white", fg="#000000")
    label1.pack()

    fq.mainloop()


def second_win():
    fen = Tk()
    fen.title("détails du projet")
    fen.geometry("1080x720")

    fen.iconbitmap("logo.ico")
    fen.config(background="#41B77F")
    # créer la frame
    frame = Frame(fen, bg="#41B77F")
    label_01 = Label(fen, text='Mots anglais dans le protéome humain ', font=("Courrier", 40), bg="#41B77F", fg='white')
    label_01.pack(expand=YES)

    menuBar = Menu(fen)
    # craetion des menus principale
    menuMots = Menu(menuBar, tearoff=0)
    menuseq = Menu(menuBar, tearoff=0)
    menuMotseq = Menu(menuBar, tearoff=0)
    menuMotcomp = Menu(menuBar, tearoff=0)
    # ajout des menus principales à la barre de menu
    menuBar.add_cascade(label="Listes_Mots", menu=menuMots)
    menuBar.add_cascade(label="Dict_Sequences", menu=menuseq)
    menuBar.add_cascade(label="Mots_Sequences", menu=menuMotseq)
    menuBar.add_cascade(label="Mots_Complet", menu=menuMotcomp)
    # ajout de commande au menu principale
    menuMots.add_command(label="ouvrir", command=LM)
    menuMots.add_command(label="quitter", command=quit)
    menuseq.add_command(label="ouvrir", command=seq)
    menuseq.add_command(label="quitter", command=quit)
    menuMotseq.add_command(label="ouvrir", command=mseq)
    menuMotseq.add_command(label="quitter", command=quit)
    menuMotcomp.add_command(label="ouvrir", command=complet)
    menuMotcomp.add_command(label="quitter", command=quit)
    fen.config(menu=menuBar)
    fen.mainloop()


# ajouter un bouton

button = Button(frame, text="Découvrir", font=("Courrier", 25), fg="#41B77F", bg="white", command=second_win)
button.pack(pady=25, fill=X)
# ajouter frame
frame.pack(expand=YES)

# afficher
window.mainloop()
