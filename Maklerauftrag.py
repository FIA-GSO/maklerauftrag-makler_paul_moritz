# Definiere eine Funktion, um die Fläche eines Raumes zu berechnen.
def berechne_raumflaeche(laenge, breite):
    return laenge * breite  # Berechnung der Fläche

# Definiere eine leere Liste, um die Informationen der Räume zu speichern.
raeume = []

# Eine Schleife, die so lange läuft, bis der Benutzer entscheidet, sie zu beenden.
while True:
    # Eingabe der Raumbezeichnung
    bezeichnung = input("Bitte geben Sie die Raumbezeichnung ein (oder 'ende' zum Beenden): ")
    if bezeichnung.lower() == 'ende':  # Prüfe, ob der Benutzer das Programm beenden möchte.
        break
    
    # Eingabe der Maße des Raumes
    laenge = float(input("Bitte geben Sie die Länge des Raums in Metern ein: "))
    breite = float(input("Bitte geben Sie die Breite des Raums in Metern ein: "))
    
    # Berechne die Fläche des Raumes und füge sie zur Liste hinzu.
    flaeche = berechne_raumflaeche(laenge, breite)
    raeume.append({'Bezeichnung': bezeichnung, 'Fläche': flaeche})

# Initialisiere eine Variable für die Gesamtfläche.
gesamtflaeche = 0

# Gib die Informationen jedes Raumes aus und summiere die Gesamtfläche.
print("\nRaumübersicht:")
for raum in raeume:
    print(f"Raumbezeichnung: {raum['Bezeichnung']}, Fläche: {raum['Fläche']} m²")
    gesamtflaeche += raum['Fläche']  # Addiere die Fläche des Raums zur Gesamtfläche.

# Gib die Gesamtfläche aller Räume aus.
print(f"\nGesamtfläche aller Räume: {gesamtflaeche} m²")
