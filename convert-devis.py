import tkinter
import tkinter as tk
from tkinter import ttk
from conversion import taux_de_conversion

def convertir_devises():
  try:
    montant = float(entree_montant.get())
    devise_source = devise_source_variable.get()
    devise_cible = devise_cible_variable.get()

    # Calculer le taux de conversion
    taux_conversion = taux_de_conversion[devise_cible] / taux_de_conversion[devise_source]
    # Convertir le montant
    montant_converti = montant * taux_conversion

    # Ajouter l'historique de la conversion
    historique.insert(tk.END, f"{montant} {devise_source} = {montant_converti:.2f} {devise_cible}")

    print(f"{montant} {devise_source} équivaut à {montant_converti:.2f} {devise_cible}")

    label_resultat.config(text=f"{montant_converti:.2f} {devise_cible}")
  except ValueError:
    label_resultat.config(text="Veuillez entrer un montant valide.")
  except KeyError:
    label_resultat.config(text="Devise source ou cible invalide.")

def effacer_historique():
  historique.delete(0, tk.END)

root = tkinter.Tk()
root.title("convertisseur de devise")
root.configure(background="#091821")
root.geometry("612x350")
root.resizable(False, False)

# Fonction pour créer la page "À propos"
def ouvrir_page_a_propos():
    # Créer une nouvelle fenêtre pour la page "À propos"
    fenetre_a_propos = tk.Toplevel(root)
    fenetre_a_propos.title("À propos")
    fenetre_a_propos.geometry("350x300")
    fenetre_a_propos.maxsize(width=350, height=300), fenetre_a_propos.minsize(width=350, height=300)
    fenetre_a_propos.attributes("-alpha", 0.8)

    # Ajouter du contenu à la page "À propos"
    label_a_propos = tk.Label(fenetre_a_propos, text="""
    **Convertisseur de devises**

    Ce convertisseur de devises est le fruit de ma passion pour 
    le langage Python. Je l'ai développé pour explorer les 
    possibilités de ce langage puissant et pour créer un outil 
    utile au quotidien. 

    J'espère que vous trouverez cette application simple 
    et efficace. N'hésitez pas à me faire part de vos 
    remarques et suggestions pour l'améliorer.

    """, font=("Arial", 12), justify="center",)
    label_a_propos.pack(side="left", pady=10)

label_titre = tkinter.Label(root, text="❲$₣❳Convertisseur de devises❲¥€❳", font=("Roboto", 35), relief="groove")
label_titre.config(bg="#091821", fg="white")
label_titre.pack()

# Créer un Frame
frame1 = tk.Frame(root, bg="#091821")
frame1.pack(pady=10)

# Créer le bouton "À propos"
bouton_a_propos = tk.Button(frame1, text="➫➬À propos", command=ouvrir_page_a_propos, width=10, height=1,
                            highlightbackground="#091821",
                            font=("Arial", 10))
bouton_a_propos.grid(row=0, column=2)

# Champ de saisie du montant
montant = tk.Label(frame1, text="Montant☞", font=("impact", 20), bg="#091821", fg="white")
montant.grid(row=1, column=0, padx=10, pady=10)
entree_montant = tk.Entry(frame1, bg='white', fg='black', highlightbackground="white", width=22)
entree_montant.grid(row=1, column=1, padx=10, pady=10)
# Combobox pour la devise source
label_devise_source = tkinter.Label(frame1, text="devise source☞", font=("impact", 20), bg="#091821", fg="white")
label_devise_source.grid(row=2, column=0, padx=10, pady=10)
devise_source_variable = tk.StringVar(root)
devise_source = ttk.Combobox(frame1, textvariable=devise_source_variable, values = list(taux_de_conversion.keys()))
devise_source.grid(row=2, column=1, padx=10, pady=10)
# Combobox pour la devise cible
label_devise_cible = tkinter.Label(frame1, text="devise sible☞", font=("impact", 20), bg="#091821", fg="white")
label_devise_cible.grid(row=3, column=0, padx=10, pady=10)
devise_cible_variable = tk.StringVar(root)
devise_cibleee = ttk.Combobox(frame1, textvariable=devise_cible_variable, values = list(taux_de_conversion.keys()))
devise_cibleee.grid(row=3, column=1, padx=10, pady=10)

botton_convertir = tkinter.Button(frame1, text="CONVERTIR", width=20, height=1,
                            highlightbackground="#091821",
                            font=("Arial", 15), command=convertir_devises)
botton_convertir.grid(row=9, column=1)

# Créer un label pour afficher le résultat
label_resultat =tkinter.Label(frame1, text="", bg="white", fg='black', font=("italic", 13))
label_resultat.grid(row=6, column=1)
"""    
quitter = tkinter.Button(frame1, text='QUITTER', width=10, height=1,
                            highlightbackground="#091821",
                            font=("Arial", 10), command=root.quit)
quitter.grid(row=9, column=0)"""

# Listbox pour afficher l'historique des conversions
historique = tk.Listbox(frame1, width=30, height=5, font=("Arial", 12),
                        selectbackground="#007bff", fg="black", bg="white", relief="ridge")
historique.grid(row=2, column=2, padx=0, pady=0)
# Bouton pour effacer l'historique
bouton_effacer = tk.Button(frame1, text="Effacer historique", command=effacer_historique, width=10, height=1,
                            highlightbackground="#091821",
                            font=("Arial", 10))
bouton_effacer.grid(row=3, column=2)

root.mainloop()

