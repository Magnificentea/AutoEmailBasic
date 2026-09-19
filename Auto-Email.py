while True:
    absender = input("Wer ist der Absender? ")
    print("")
    empfänger = input("An wen soll diese E-Mail gehen? ")
    print("")
    gender = input("Ist die Person männlich oder weiblich? ")
    if gender.lower() == "männlich":
        titel = f"geehrter Herr {empfänger},"
    elif gender.lower() == "weiblich":
        titel = f"geehrte Frau {empfänger},"
    else:
        titel = "geehrte Damen und Herren,"
    print(f"Sehr {titel}")
    print("")
    print(f"mein Name ist {absender} und ich bin auf der Suche nach einem Ausbildungsplatz als Fachinformatiker.")
    print("Wichtige Unterlagen finden Sie im Anhang dieser E-Mail als PDF für die Bewerbung.")
    print("")
    print("Sollten Rückfragen entstanden sein, bitte ich Sie, mich per E-Mail oder Mobil Telefon zu erreichen.")
    print("")
    print("")
    print("Mit freundlichen Grüßen,")
    print(f"{absender}")
    print("")
    input("Eingabe machen, um eine weitere E-Mail zu verfassen.")
print("")
