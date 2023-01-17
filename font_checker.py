from cgi import print_arguments
from cmath import exp
from locale import locale_encoding_alias
from re import U
import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import csv
from datetime import datetime

## hier kann man den Pfad zu seimen driver definiren 
driver = webdriver.Chrome('C:\Windows\chromedriver.exe') 

## hier kann man die Url angeben welche getestet werden soll
url = 'https://stage.derwesten.de/panorama/vermischtes/hochzeit-news-reddit-freundin-schwanger-braut-id300112218.html'



## öfnet einmal font_error_log.csv um es zu erzeugen
with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
    file_object.close()
try:    
    driver.get(url);
    # Maximiere das Fenster
    driver.maximize_window()
    
except:
    driver_error = 'der Driver konnte nicht gefunden werden'
    error_time = datetime.now()
    url = "Error"
    with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
        
        writer = csv.writer(file_object, delimiter = ";")
        writer.writerow([driver_error, error_time, url])
        file_object.close()
    


# Warte 30 Sekunden, bis der Shadow-root druch das element cmpwrapper da ist
try:
    element = WebDriverWait(driver, 30).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cmpwrapper"))
    )
    
    # Geht in den shadow-root
    shadow = driver.find_element(By.CLASS_NAME,"cmpwrapper")
    script = 'return arguments[0].shadowRoot'
    shadow_root = driver.execute_script(script, shadow)
    # Klick auf den Link "Alle akzeptieren"
    shadow_root.find_element(By.LINK_TEXT, "Alle akzeptieren").click()

    t_akzeptiern_der_cookie = int(time.time())*1000
    
# Falls das Element nicht gefunden werden kann
except:
    print ('test3')
    # Schreibe eine Fehlermeldung
    cookie_error = 'nach 30 Sekunden konnte man die cookies immer noch nicht akzeptieren'
    error_time = datetime.now()
    url = driver.current_url
    # Schreibe die Fehlermeldung, die Fehlerzeit und die URL in eine CSV-Datei
    with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
        
        writer = csv.writer(file_object, delimiter = ";")
        writer.writerow([cookie_error, error_time, url])
        file_object.close()

try:        
    # Finde das erste Element mit dem CSS-Selektor ".entry-title"  
    headline = driver.find_element(By.CSS_SELECTOR,".entry-title")
    # Wenn die Länge des gefundenen Elements größer als 5 ist    
    if len(headline.text) > 5:

        type = 'ueberschrift'

        ueberschrift_font = headline.value_of_css_property('font-family')
        ueberschrift_font_size = headline.value_of_css_property('font-size')
        # Öffne eine CSV-Datei und schreibe die Informationen in eine neue Zeile
        with open("font_checker.csv", "a", encoding='utf-8') as file_object:

            writer = csv.writer(file_object, delimiter = ";")
            writer.writerow([type, ueberschrift_font, ueberschrift_font_size])
            file_object.close()
            # Wenn die Schriftart des Elements nicht "League Spartan", Georgia, "serif" ist
            if ueberschrift_font != '"League Spartan", Georgia, "serif"':
                # Schreibe eine Fehlermeldung
                ueberschrft_error = 'die ueberschrift font ist falsch'

                error_time = datetime.now()
                url = driver.current_url
                with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
                    writer = csv.writer(file_object, delimiter = ";")
                    writer.writerow([ueberschrft_error, error_time, url])
                    file_object.close()

    # Wenn die Länge des gefundenen Elements kleiner oder gleich 5 ist
    else:
        # Schreibe eine Fehlermeldung
        ueberschrift_error = 'ueberschrift ist ungewöhnlich kurz'
        error_time = datetime.now()
        url = driver.current_url
        with open("font_error_log.csv", "a", encoding='utf-8') as file_object:

            writer = csv.writer(file_object, delimiter = ";")
            writer.writerow([ueberschrift_error, error_time, url])
            file_object.close()
# Wenn überschrift nicht gefunden wird
except:
    # Schreibe eine Fehlermeldung
    ueberschrift_error = 'ueberschrift nicht gefunden'
    error_time = datetime.now()
    url = driver.current_url
    with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
        writer = csv.writer(file_object, delimiter = ";")
        writer.writerow([ueberschrift_error, error_time, url])
        file_object.close()  


# Prüfe, ob das Element mit dem CSS-Selektor '.entry-subhead' angezeigt wird, was die Autor*innen informationen sind
if driver.find_element(By.CSS_SELECTOR, '.entry-subhead').is_displayed():
    type = 'autor_info'
    autor_in_font = driver.find_element(By.CSS_SELECTOR, '.url.fn.n').value_of_css_property('font-family')
    autor_in_font_size = driver.find_element(By.CSS_SELECTOR, '.url.fn.n').value_of_css_property('font-size')
    
    with open("font_checker.csv", "a", encoding='utf-8') as file_object:
        
        writer = csv.writer(file_object, delimiter = ";")
        writer.writerow([type, autor_in_font, autor_in_font_size])
        file_object.close()
        if not autor_in_font == '"League Spartan", Georgia, "serif"':
            autor_in_error = 'die autor_innen font ist falsch'
            error_time = datetime.now()
            url = driver.current_url
            with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
            
                writer = csv.writer(file_object, delimiter = ";")
                writer.writerow([autor_in_error, error_time, url])
                file_object.close()
# Wenn das Element nicht angezeigt wird
            
else:
    autor_in_error = 'es wird kein_e autor_in angezeigt'
    error_time = datetime.now()
    url = driver.current_url
    with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
        
        writer = csv.writer(file_object, delimiter = ";")
        writer.writerow([autor_in_error, error_time, url])
        file_object.close()

try:
    
    # Der Code sucht nach dem div mit der Klasse "lead"
    lead = driver.find_element(By.CSS_SELECTOR, '.lead')
    # Wenn der Inhalt des divs länger als 10 Zeichen ist, wird die Schriftart und Schriftgröße überprüft
    if len(lead.text) > 10:
        type = 'text_lead'
        lead_font = lead.value_of_css_property('font-family')
        lead_font_size = lead.value_of_css_property('font-size')
         # Die Informationen werden in eine CSV-Datei geschrieben
        with open("font_checker.csv", "a", encoding='utf-8') as file_object:

            writer = csv.writer(file_object, delimiter = ";")
            writer.writerow([type, lead_font, lead_font_size])
            file_object.close()
        # Wenn die Schriftart des Elements nicht "Noto Sans, Georgia, serif" ist
        if lead_font != '"Noto Sans", Georgia, "serif"':
            # Schreibe eine Fehlermeldung
            lead_error = 'die lead font ist falsch'
            error_time = datetime.now()
            url = driver.current_url
            with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
                writer = csv.writer(file_object, delimiter = ";")
                writer.writerow([lead_error, error_time, url])
                file_object.close()
    # Wenn der Inhalt des divs kürzer als 10 Zeichen ist, schreibe eine Fehlermeldung
    else: 
        lead_error = ' lead ist ungewöhnlich kurz'
        error_time = datetime.now()
        url = driver.current_url
        with open("font_error_log.csv", "a", encoding='utf-8') as file_object:

            writer = csv.writer(file_object, delimiter = ";")
            writer.writerow([lead_error, error_time, url])
            file_object.close()
# Wenn lead nicht gefuden wurde 
except:
    # Schreiben von Fehlermeldung
    lead_error = ' text lead wurde nicht gefunden'
    error_time = datetime.now()
    url = driver.current_url
    with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
        writer = csv.writer(file_object, delimiter = ";")
        writer.writerow([lead_error, error_time, url])
        file_object.close()    


try:
    # Finden des Elements mit der Klasse "article-body"
    body = driver.find_element(By.CSS_SELECTOR, '.article-body')

    # Überprüfen, ob die Textlänge des Elements größer als 10 ist
    if len(body.text)>10:


        type = 'Body' 
        body_font = body.value_of_css_property('font-family')
        body_font_size= body.value_of_css_property('font-size')

        # Die Informationen werden in eine CSV-Datei geschrieben

        with open("font_checker.csv", "a", encoding='utf-8') as file_object:

            writer = csv.writer(file_object, delimiter = ";")
            writer.writerow([type, body_font, body_font_size])
            file_object.close()
        # Überprüfen, ob die Schriftart des Elements nicht "Noto Sans", Georgia, "serif" entspricht
        if not body_font == '"Noto Sans", Georgia, "serif"':
            # Schreibt eine Fehlermeldung
            body_error = 'die body font ist falsch'
            error_time = datetime.now()
            url = driver.current_url
            with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
                writer = csv.writer(file_object, delimiter = ";")
                writer.writerow([body_error, error_time, url])
                file_object.close()
    # Wenn die Textlänge des Elements kleiner oder gleich 10 ist
    else:
        # Schreibt ein Fehlermeldung
        body_error = ' es wird keine body angezeigt'
        error_time = datetime.now()
        url = driver.current_url
        with open("font_error_log.csv", "a", encoding='utf-8') as file_object:

            writer = csv.writer(file_object, delimiter = ";")
            writer.writerow([body_error, error_time, url])
            file_object.close()

except:
    # Schreibt ein Fehlermeldung
    body_error = ' es wird keine body angezeigt'
    error_time = datetime.now()
    url = driver.current_url
    with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
        writer = csv.writer(file_object, delimiter = ";")
        writer.writerow([body_error, error_time, url])
        file_object.close()
        


# Testen der Zwischenüberschriften auf ihre Schriftart

try: 
    # Versuchen das Element mit dem Tag-Namen 'h2' im Body zu finden
    body.find_element(By.TAG_NAME,'h2')
    zw = body.find_element(By.TAG_NAME,'h2')
    type = 'zwischen_ueberschrift'
    zw_font = zw.value_of_css_property('font-family')
    zw_font_size = zw.value_of_css_property('font-size')
    # Die Informationen werden in eine CSV-Datei geschrieben
    with open("font_checker.csv", "a", encoding='utf-8') as file_object:
        
        writer = csv.writer(file_object, delimiter = ";")
        writer.writerow([type, zw_font, zw_font_size])
        file_object.close()
    if not zw_font == '"League Spartan", Georgia, "serif"':
        zw_error = 'die lead font ist falsch'
        error_time = datetime.now()
        url = driver.current_url
        # Schreibt ein Fehlermeldung
        with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
            writer = csv.writer(file_object, delimiter = ";")
            writer.writerow([zw_error, error_time, url])
            file_object.close()
# Wenn das Element mit dem Tag-Namen 'h2' nicht gefunden werden kann    
except:
    zw_error = ' es wird keine zwischenüberschfit angezeigt'
    error_time = datetime.now()
    url = driver.current_url
    with open("font_error_log.csv", "a", encoding='utf-8') as file_object:
        
        writer = csv.writer(file_object, delimiter = ";")
        writer.writerow([zw_error, error_time, url])
        file_object.close()
# Schließen des Browserfensters
driver.quit()