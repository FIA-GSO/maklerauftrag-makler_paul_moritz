# Funktion, um die Flaeche eines Raumes zu berechnen
def berechne_raumflaeche(laenge, breite):
    return laenge * breite  # Berechnung der Flaeche

# Leere Liste, um die Informationen der Raeume zu speichern.
raeume = []

# Schleife die laeuft, bis zur Eingabe von 'ende'
while True:
    # Eingabe der Raumbezeichnung
    bezeichnung = input("Bitte geben Sie die Raumbezeichnung ein (oder 'ende' zum Beenden): ")
    if bezeichnung.lower() == 'ende':  # Pruefe, ob der Benutzer das Programm beenden moechte
        break
    
    # Eingabe der Masse des Raumes
    laenge = float(input("Bitte geben Sie die Länge des Raums in Metern ein: "))
    breite = float(input("Bitte geben Sie die Breite des Raums in Metern ein: "))
    
    # Flaechenberechnung des Raumes und Hinzufuegen zur Liste
    flaeche = berechne_raumflaeche(laenge, breite)
    raeume.append({'Bezeichnung': bezeichnung, 'Fläche': flaeche})

# Variable fuer Gesamtflaeche initialisieren
gesamtflaeche = 0

# Gib die Informationen jedes Raumes aus und summiere die Gesamtflaeche
print("\nRaumübersicht:")
for raum in raeume:
    print(f"Raumbezeichnung: {raum['Bezeichnung']}, Fläche: {raum['Fläche']} m²")
    gesamtflaeche += raum['Fläche']  # Addiere die Fläche des Raums zur Gesamtfläche.

# Gib die Gesamtflaeche aller Raeume aus.
print(f"\nGesamtfläche aller Räume: {gesamtflaeche} m²")   