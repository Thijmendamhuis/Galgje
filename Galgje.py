import tkinter as tk
from tkinter import messagebox

# Globale variabelen om de spelstatus bij te houden
geraden_letters = [] # Lijst om bij te houden welke letters zijn geraden
punten = 0  # Score van de speler
levens = 10  # Aantal resterende levens
geheimwoord_str = ''  # Het geheime woord dat geraden moet worden



# Functie om het geheime woord op te halen
def geheimwoord():
    global geheimwoord_str
    geheimwoord_str = woord_entry.get().upper()  # Haal het ingevoerde woord op en converteer naar hoofdletters
    # Controleer of het ingevoerde woord alleen uit letters bestaat
    if not geheimwoord_str.isalpha():
        # Toon een waarschuwing als het ingevoerde woord ongeldig is
        tk.messagebox.showwarning("Ongeldige invoer", "Voer een geldig woord in.")
        return None
    return geheimwoord_str

# Functie om te controleren of het spel is gewonnen
def check_win():
    # Controleer of alle letters van het geheime woord zijn geraden
    return all(letter in geraden_letters for letter in geheimwoord())
        

# Functie om de juiste afbeelding van de galg te tonen op basis van het aantal resterende levens
def nieuwe_foto():
    global levens
    if levens >= 1:
        nieuwe_foto_label.config(image=leven_afbeeldingen[levens])
    else:
        nieuwe_foto_label.config(image=leven_afbeeldingen[0])


# Functie om het scorebord bij te werken
def scoreboard():
    # Update de labels voor de score en de geraden letters
    scoreboard_punten_label.config(text=f'Score: {punten}')
    scoreboard_geradenletters_label.config(text=f'Geraden Letters: ' + str(geraden_letters))
# Functie om het woord te tonen als het woord niet geraden is 



# Functie om de GUI bij te werken op basis van de spelstatus
def update_display(event=None):
    global levens
    # maken van de tekst die het geheime woord en de geraden letters weergeeft
    display_text = ' '.join(letter if letter in geraden_letters else '_' for letter in geheimwoord())
    # Update het label om het geheime woord en de geraden letters weer te geven
    display_label.config(text=display_text)
    gok_entry.delete(0, 'end')
    # Verberg widgets die niet meer nodig zijn nadat het spel is gestart
    welkom_frame.grid_forget()
    label.grid_forget()
    woord_entry.grid_forget()
    welkom_button.grid_forget()
    scoreboard_punten_label.grid(padx=100, pady=0)
    label2.grid(padx=100, pady=0)
    nieuwe_foto_label.grid(padx=100, pady=0)
    display_label.grid(padx=100, pady=0)
    gok_entry.grid(padx=100, pady=0)
    raad_button.grid(padx=100, pady=0)
    scoreboard_geradenletters_label.grid(padx=100, pady=0)
    
# Functie om een nieuw spel te starten
def nieuwe_game(event=None):
    global punten, levens, geheimwoord_str, geraden_letters
    # Reset de score, het aantal levens en de lijst met geraden letters
    punten = 0
    levens = 10
    geraden_letters = [] # Reset de lijst met geraden letters
    # Wis de invoervelden voor het woord en de gok
    woord_entry.delete(0, 'end')
    gok_entry.delete(0, 'end')
    # Reset de positie van de welkom-widgets
    welkom_frame.grid(row=0, column=0, padx=100, pady=0)
    label.grid(row=1, column=0, padx=100, pady=0)
    woord_entry.grid(row=2, column=0, padx=100, pady=0)
    welkom_button.grid(row=3, column=0, padx=100, pady=0)
    # Verberg widgets die niet nodig zijn bij een nieuw spel
    label2.grid_forget()
    scoreboard_punten_label.grid_forget()
    scoreboard_geradenletters_label.grid_forget()
    display_label.grid_forget()
    gok_entry.grid_forget()
    raad_button.grid_forget()
    nieuwe_foto_label.grid_forget()
    nieuwe_game_button.grid_forget()
    vorige_woord_label.grid_forget()
    geheimwoord_str = ''
    nieuwe_foto()

def toon_geheimwoord():
    global geraden_letters
    vorige_woord_label.config(text=f"Het woord was: {geheimwoord_str.lower()}")
    vorige_woord_label.grid_configure()
    geraden_letters = []

# Functie om de gok van de speler te verwerken
def gok(event=None):
    global punten, levens
    # Haal de gok van de speler op en converteer naar hoofdletters
    gok = gok_entry.get().upper()
    # controlleer of de letter al geprobeerd is. 
    if gok not in geraden_letters:
        if levens >= 1:
            
            # Controleer of de gok een enkele letter is
            if gok.isalpha() and len(gok) == 1:
                # Voeg de gok toe aan de lijst met geraden letters
                geraden_letters.append(gok)
                # Werk de GUI bij om de geraden letters weer te geven
                update_display()
                # Controleer of het spel is gewonnen
                if check_win():
                    # Toon een melding als het spel is gewonnen
                    tk.messagebox.showinfo("Gefeliciteerd!", "Je hebt het woord geraden!")
                    # Verhoog de score, reset het aantal levens en werk het scorebord bij
                    punten += 1
                    levens = 10
                    scoreboard()
                    # Toon de knop voor het starten van een nieuw spel en wat het geheimwoord was
                    nieuwe_game_button.grid_configure()
                    toon_geheimwoord()
                      
                else:
                    # Verlaag het aantal resterende levens als de gok fout is
                    if gok not in geheimwoord_str:
                        levens -= 1
                        scoreboard()
                        nieuwe_foto()

            # Controleer of de gok een volledig woord is
            elif gok.isalpha() and len(gok) > 1:
                if gok == geheimwoord_str:
                    tk.messagebox.showinfo("Gefeliciteerd!", "Je hebt het woord geraden!")
                    punten += 1
                    scoreboard()
                    # Toon de knop voor het starten van een nieuw spel en wat het geheimwoord was
                    nieuwe_game_button.grid_configure()
                    toon_geheimwoord()
                    
                    
                else:
                    tk.messagebox.showwarning("Ongeldige invoer", "Het ingevoerde woord is niet correct.")
                    levens -= 1
                    nieuwe_foto()
            else:
                tk.messagebox.showwarning("Ongeldige invoer", "Voer één geldige letter in.")
                punten += 0
            # Werk het scorebord bij
            scoreboard()
        else:
            # Toon een melding als het spel verloren is
            tk.messagebox.showwarning("Game over", "Je hebt helaas geen levens meer over")
            # Toon de knop voor het starten van een nieuw spel en wat het geheimwoord was
            nieuwe_game_button.grid_configure()
            toon_geheimwoord()
            
            
    else: 
        tk.messagebox.showwarning("Waarschuwing", "Je heb deze letter al geprobeerd") 
        return None
    
# Maak het hoofdvenster van de applicatie
root = tk.Tk()
root.title("Galgje")
root.geometry("350x400")

# Lijst met afbeeldingen van de galg
leven_afbeeldingen = [
    tk.PhotoImage(file="foto's/galg0.png"),
    tk.PhotoImage(file="foto's/galg1.png"),
    tk.PhotoImage(file="foto's/galg2.png"),
    tk.PhotoImage(file="foto's/galg3.png"),
    tk.PhotoImage(file="foto's/galg4.png"),
    tk.PhotoImage(file="foto's/galg5.png"),
    tk.PhotoImage(file="foto's/galg6.png"),
    tk.PhotoImage(file="foto's/galg7.png"),
    tk.PhotoImage(file="foto's/galg8.png"),
    tk.PhotoImage(file="foto's/galg9.png"),
    tk.PhotoImage(file="foto's/galg10.png")
]

# Welkom-frame voor de begin om het woord in te vullen
welkom_frame = tk.Frame(root)

# Label voor het weergeven van de score
scoreboard_punten_label = tk.Label(root, text='Score: 0')
# Label voor het weergeven van de geraden letters
scoreboard_geradenletters_label = tk.Label(root, text='Geraden Letters: ')

# Label voor de instructie om een woord in te voeren
label = tk.Label(root, text="Voer een woord in:")
# Label voor de instructie om het woord te raden
label2 = tk.Label(root, text="Probeer het woord te raden")
# Label voor het weergeven van het geheime woord
display_label = tk.Label(root, text="")

# Entry-widget voor het invoeren van het geheime woord
woord_entry = tk.Entry(root)
# Bind de Return-toets aan de functie update_display()
woord_entry.bind("<Return>", update_display)
# Entry-widget voor het invoeren van een gok door de speler
gok_entry = tk.Entry(root)
# Bind de Return-toets aan de functie gok()
gok_entry.bind("<Return>", gok)

# Knop om het spel te starten
welkom_button = tk.Button(root, text="Begin het spel", command=update_display)
# Knop om een gok te maken
raad_button = tk.Button(root, text="Raad", command=gok)
# Knop om een nieuw spel te starten
nieuwe_game_button = tk.Button(root, text="Nieuwe game", command=nieuwe_game)

# Label voor het weergeven van de afbeelding van de galg
nieuwe_foto_label = tk.Label(root, image=leven_afbeeldingen[10])

# Plaats het welkom-frame in het venster
welkom_frame.grid(padx=100, pady=0)
# Plaats het label voor het invoeren van het woord in het venster
label.grid(padx=100, pady=0)
# Plaats de entry-widget voor het invoeren van het woord in het venster
woord_entry.grid(padx=100, pady=0)
# Plaats de welkomstknop in het venster
welkom_button.grid(padx=100, pady=0)

vorige_woord_label = tk.Label(root, text='')


# Start de hoofdlus van de GUI
root.mainloop()

