# -*- coding: iso-8859-1 -*-

import random
import tkinter as tk

class StacjaPogody:
    def __init__(self):
        self.kierunek_wiatru = "N"
        self.predkosc_wiatru = 0
        self.wilgotnosc = 0
        self.temperatura = 0
        self.cisnienie = 0

    def losuj_pomiary(self):
        self.kierunek_wiatru = random.choice(["N", "NE", "E", "SE", "S", "SW", "W", "NW"])
        self.predkosc_wiatru = random.randint(0, 30)
        self.wilgotnosc = random.randint(0, 100)
        self.temperatura = random.uniform(-20, 40)
        self.cisnienie = random.uniform(900, 1100)

    def skoryguj_wartosc(self, wartosc, korekta):
        return wartosc + korekta

class AplikacjaPogodowa:
    def __init__(self, root):
        self.root = root
        self.stacja_pogody = StacjaPogody()

        self.frame_dane_pogodowe = tk.Frame(root)
        self.frame_dane_pogodowe.pack(pady=10)

        self.label_tytul = tk.Label(self.frame_dane_pogodowe, text="Mobilna Stacja Pogodowa", font=("Arial", 16))
        self.label_tytul.pack()

        self.kierunek_wiatru_label = tk.Label(self.frame_dane_pogodowe, text="Kierunek wiatru: ", font=("Arial", 12))
        self.kierunek_wiatru_label.pack()

        self.predkosc_wiatru_label = tk.Label(self.frame_dane_pogodowe, text="Predkosc wiatru: ", font=("Arial", 12))
        self.predkosc_wiatru_label.pack()

        self.wilgotnosc_label = tk.Label(self.frame_dane_pogodowe, text="Wilgotnosc: ", font=("Arial", 12))
        self.wilgotnosc_label.pack()

        self.temperatura_label = tk.Label(self.frame_dane_pogodowe, text="Temperatura: ", font=("Arial", 12))
        self.temperatura_label.pack()

        self.cisnienie_label = tk.Label(self.frame_dane_pogodowe, text="Cisnienie: ", font=("Arial", 12))
        self.cisnienie_label.pack()

        self.odswiez_pomiary()

        self.frame_korekta = tk.Frame(root)
        self.frame_korekta.pack(pady=10)

        self.label_korekta = tk.Label(self.frame_korekta, text="Korekta: ", font=("Arial", 12))
        self.label_korekta.grid(row=0, column=0)

        self.korekta_entry = tk.Entry(self.frame_korekta, font=("Arial", 12), width=10)
        self.korekta_entry.grid(row=0, column=1)

        self.korekta_button = tk.Button(self.frame_korekta, text="Skoryguj", font=("Arial", 12), command=self.skoryguj_pomiary)
        self.korekta_button.grid(row=0, column=2)

        self.frame_panel_administratora = tk.Frame(root)
        self.frame_panel_administratora.pack(pady=10)

        self.label_przed_korekta = tk.Label(self.frame_panel_administratora, text="Predkosc wiatru przed korekta: ", font=("Arial", 12))
        self.label_przed_korekta.grid(row=0, column=0)

        self.label_po_korekta = tk.Label(self.frame_panel_administratora, text="Predkosc wiatru po korekcie: ", font=("Arial", 12))
        self.label_po_korekta.grid(row=1, column=0)

    def odswiez_pomiary(self):
        self.stacja_pogody.losuj_pomiary()

        self.kierunek_wiatru_label.config(text="Kierunek wiatru: " + self.stacja_pogody.kierunek_wiatru)
        self.predkosc_wiatru_label.config(text="Predkosc wiatru: " + str(self.stacja_pogody.predkosc_wiatru) + " km/h")
        self.wilgotnosc_label.config(text="Wilgotnosc: " + str(self.stacja_pogody.wilgotnosc) + "%")
        self.temperatura_label.config(text="Temperatura: " + str(round(self.stacja_pogody.temperatura, 2)) + " C")
        self.cisnienie_label.config(text="Cisnienie: " + str(round(self.stacja_pogody.cisnienie, 2)) + " hPa")

    def skoryguj_pomiary(self):
        try:
            korekta = float(self.korekta_entry.get())
            przed_korekta = self.stacja_pogody.predkosc_wiatru
            nowa_predkosc_wiatru = self.stacja_pogody.skoryguj_wartosc(przed_korekta, korekta)
            self.stacja_pogody.predkosc_wiatru = nowa_predkosc_wiatru
            self.label_przed_korekta.config(text="Predkosc wiatru przed korekta: " + str(przed_korekta) + " km/h")
            self.label_po_korekta.config(text="Predkosc wiatru po korekcie: " + str(nowa_predkosc_wiatru) + " km/h")
        except ValueError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Mobilna Stacja Pogodowa")
    root.geometry("400x400")

    aplikacja = AplikacjaPogodowa(root)

    def aktualizuj_pomiary():
        aplikacja.odswiez_pomiary()
        root.after(1000, aktualizuj_pomiary)

    aktualizuj_pomiary()

    root.mainloop()
