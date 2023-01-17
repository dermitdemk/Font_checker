# Font_checker
ist dafür da zu überprüfen ob die Fonts auf der Westen stimmen
Um das Programm zu starten, muss man sich von dieser Seite den passenden Chrome Driver downloaden
https://chromedriver.chromium.org/downloads
Seine Chrome Version findet man bei:
Einstellungen
Über Google Chrome (das ist ganz unten)
das ZIP muss entpackt werden und den passenden Driver entweder in C:\Windows\chromedriver.exe
abgespeichert werden oder der Driver Pfad muss in der datei font_checker.py geändert werden

Nun kann man das Programm einfach mit Python ausführen. 
Es wird empfohlen dieses in einen eignen Ordner zu legen, da es 2 neue Dateien erstellen kann, welche sonst eventuell untergehen könnten.
Die URL kann auf jede andere angepasst werden
In font_cheker.csv werden die verschiedenen Font arten der einzelnen Text abschnitten abgespeichert
In fort_error_log.csv werden die Fehlermeldungen gespeichert 
nach dem Laufen des Programmes sollte man schauen ob es das font_error_log.csv gibt und ob etwas in ihm steht.
