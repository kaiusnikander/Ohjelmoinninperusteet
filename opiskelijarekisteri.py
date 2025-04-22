import statistics

# Lisää uusi opiskelija sanakirjaan
def lisaa_opiskelija(opiskelijat: dict, id: str, nimi: str, ika: int):
    opiskelijat[id] = {"nimi": nimi, "ika": ika, "kurssit": []}
    print(f"Opiskelija {nimi} lisätty ID:llä {id}.")

# Lisää tai päivittää opiskelijan suoritus
def lisaa_suoritus(opiskelijat: dict, id: str, suoritus: tuple):
    if id in opiskelijat:
        for i, j in enumerate(opiskelijat[id]["kurssit"]):
            if j[0] == suoritus[0]:  # Tarkistetaan, onko kurssi jo olemassa
                if suoritus[1] > j[1]:  # Päivitetään, jos uusi arvosana on parempi
                    opiskelijat[id]["kurssit"][i] = suoritus
                return
        opiskelijat[id]["kurssit"].append(suoritus)  # Lisätään uusi suoritus
        print(f"Suoritus {suoritus[0]} lisätty opiskelijalle ID:llä {id}.")
    else:
        print(f"Opiskelijaa ID:llä {id} ei löytynyt.")

# Tulostaa kaikki opiskelijat ja heidän tietonsa
def tulosta_kaikki(opiskelijat: dict):
    if not opiskelijat:
        print("Ei opiskelijoita.")
        return
    for id, tiedot in opiskelijat.items():
        print(f"ID: {id}, Nimi: {tiedot['nimi']}, Ikä: {tiedot['ika']}")
        if tiedot["kurssit"]:
            print(" Kurssit ja arvosanat:")
            for kurssi, arvosana in tiedot["kurssit"]:
                print(f"  {kurssi}: {arvosana}")
        else:
            print(" Ei suorituksia.")

# Tulostaa yksittäisen opiskelijan tiedot
def tulosta_opiskelija(opiskelijat: dict, id: str):
    if id in opiskelijat:
        tiedot = opiskelijat[id]
        print(f"ID: {id}, Nimi: {tiedot['nimi']}, Ikä: {tiedot['ika']}")
        if tiedot["kurssit"]:
            print(" Kurssit ja arvosanat:")
            for kurssi, arvosana in tiedot["kurssit"]:
                print(f"  {kurssi}: {arvosana}")
        else:
            print(" Ei suorituksia.")
    else:
        print(f"Opiskelijaa ID:llä {id} ei löytynyt.")

# Hakee opiskelijan ID:n tai nimen perusteella
def hae_opiskelija(opiskelijat: dict, hakutermi: str):
    for id, tiedot in opiskelijat.items():
        if id == hakutermi or tiedot["nimi"].lower() == hakutermi.lower():
            tulosta_opiskelija(opiskelijat, id)
            return
    print(f"Opiskelijaa hakutermillä '{hakutermi}' ei löytynyt.")

# Poistaa opiskelijan ID:n perusteella
def poista_opiskelija(opiskelijat: dict, id: str):
    if id in opiskelijat:
        del opiskelijat[id]
        print(f"Opiskelija ID:llä {id} poistettu.")
    else:
        print(f"Opiskelijaa ID:llä {id} ei löytynyt.")

# Hakee opiskelijan, jolla on paras mediaaniarvosana
def hae_paras_opiskelija(opiskelijat: dict):
    paras_opiskelija = None
    paras_mediaani = -1

    for id, tiedot in opiskelijat.items():
        if tiedot["kurssit"]:
            arvosanat = [arvosana for _, arvosana in tiedot["kurssit"]]
            mediaani = statistics.median(arvosanat)  # Lasketaan mediaani
            if mediaani > paras_mediaani:
                paras_mediaani = mediaani
                paras_opiskelija = (id, tiedot["nimi"], mediaani)

    return paras_opiskelija

# Pääohjelma, joka tarjoaa valikon käyttäjälle
def main():
    opiskelijat = {}
    while True:
        print("\nValitse toiminto:")
        print("1. Lisää opiskelija")
        print("2. Lisää suoritus")
        print("3. Näytä kaikki opiskelijat")
        print("4. Hae opiskelijaa")
        print("5. Poista opiskelija")
        print("6. Lopeta")
        valinta = input("Valintasi: ")

        if valinta == "1":
            id = input("Anna opiskelijan ID: ")
            nimi = input("Anna opiskelijan nimi: ")
            ika = int(input("Anna opiskelijan ikä: "))
            lisaa_opiskelija(opiskelijat, id, nimi, ika)
        elif valinta == "2":
            id = input("Anna opiskelijan ID: ")
            kurssi = input("Anna kurssin nimi: ")
            arvosana = int(input("Anna arvosana: "))
            lisaa_suoritus(opiskelijat, id, (kurssi, arvosana))
        elif valinta == "3":
            tulosta_kaikki(opiskelijat)
        elif valinta == "4":
            hakutermi = input("Anna opiskelijan ID tai nimi: ")
            hae_opiskelija(opiskelijat, hakutermi)
        elif valinta == "5":
            id = input("Anna poistettavan opiskelijan ID: ")
            poista_opiskelija(opiskelijat, id)
        elif valinta == "6":
            paras_opiskelija = hae_paras_opiskelija(opiskelijat)
            if paras_opiskelija:
                print(f"\nParas opiskelija on {paras_opiskelija[1]} (ID: {paras_opiskelija[0]}) "
                      f"mediaaniarvosanalla {paras_opiskelija[2]:.1f}.")
            else:
                print("\nEi opiskelijoita, joilla olisi suorituksia.")
            print("Ohjelma lopetettu.")
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")

# Suoritetaan ohjelma, jos tiedostoa ajetaan suoraan
if __name__ == "__main__":
    main()

