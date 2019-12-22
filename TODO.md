Hallo erstmal an alle,
hier werden wir das Projekt maintainen und hier wird alles besprochen etc.

2019/12/20:
Hallo, hier ein paar Guides zur Struktur und Dokumentierung unseres Projekts:
https://www.datacamp.com/community/tutorials/docstrings-python#third-head <br>

https://dev.to/dstarner/using-pythons-type-annotations-4cfe
https://realpython.com/documenting-python-code/


Die allgemeine Struktur:

zombie.py:
Klasse 'World' stellt die Simulation dar
Map.py:
Klasse 'Map' stellt die Karte dar
SimObject.py:
verkoerpert die Standardeigenschaften eines Objektes auf der Karte
klasseneigene fukntion 'go' aendert die Koordinaten in der KLasse selbst und gibt die geaenderte Karte zurueck