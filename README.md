# doom_balance_board

Interfacing eines Adafruit BNO08x Sensor und einem Raspberry Pi Pico über Circuit Python für ein Balance Board.
Steuerung für Doom oder ähnliche Spiele (WASD und Maus-Bewegung in x-Richtung) und Trackmania Nations Forever (Pfeiltasten).
PDF --> Ordner enthält die aus TEX kompilierte PDF-Datei der Belegarbeit
TEX --> TEX-Dateien der Belegarbeit
python_code --> Source Code 

Installation:
-------------

1.: Raspberry Pi Pico vorbereiten:

1.1: Adafruit Circuit Python Firmware 8 downloaden: https://circuitpython.org/board/raspberry_pi_pico/
1.2: Adarfuit Circuit Python Bundle für Firmware 8.x downloaden: https://circuitpython.org/libraries

1.3: Raspberry Pi Pico bei gedrückter BOTSEL-Taste an den PC anschließen, sodass er in den Bootloader wechselt. Der Pico erscheint als Massenspeichermedium.
1.4: Die Firmware auf den Pico kopieren. Dieser startet sich anschließend neu.
1.5: Das zuvor gedownloadete Library Bundle nach den Bibliotheken "adafruit_bno08x_rvc.mpy" und "adafruit_hid" und durchsuchen.
1.6: Beide Bibliotheken in den "lib"-Ordner des Raspberry Pi Pico kopieren
1.7: code.py in das Root-Verzeichnis des Raspberry Pi Pico kopieren

2.: PC vorbereiten
2.1: Mu downloaden: https://codewith.mu/
2.2: Mu installieren und den Modus "Circuit Python" auswählen
2.3: DosBox downloaden: https://www.dosbox.com/download.php?main=1
2.4: DosBox installieren
2.5: Doom downloaden: https://archive.org/details/doom_20231012
2.6: Doom in ein Verzeichnis entpacken
2.7: DosBox Configuration File aufrufen: C:\Users\[USERNAME]\AppData\Local\DOSBox
2.8: Folgenden Eintrag in der File editieren: fullscreen=true (Vollbild bei Start von DosBox)
2.9: unter [autoexec] folgende Zeilen hinzufügen:
                                                                    mount c [Pfad_zum_doom_ordner]            // mountet den Doom-Ordner als virtuelles Laufwerk c in DosBox
                                                                    c:                                        // wechselt auf das virtuelle Laufwerk c
                                                                    doom                                      // startet doom
                                                                    exit                                      // Beendet DosBox, wenn Doom beendet wurd
2.10: Trackmania Nations Forever downloaden:  https://www.chip.de/downloads/TrackMania-Nations-Forever_31482232.html
2.11: Trackmania Nations Forever installieren
2.12: Die hier bereitsgestellte Strecke "PAES_Rundkurs.Challenge.Gbx" downloaden und in den Ordner C:\Users\[USERNAME]\Documents\TmForever\Tracks\Challenges\My Challenges kopieren

3.: Balance Board vorbereiten
3.1: Mu starten und mit dem Button "Seriell" das REPL öffnen
3.2: Balance Board über USB mit dem PC verbinden
3.3: Das Balance Board müsste jetzt eine Begrüßung über das REPL ausgeben. Falls das nicht der Fall ist, bei Mu auf "Speichern" gehen und Neustart des RaspBerry Pi Pico abwarten
3.4: Bei der Spielabfrage im REPL die entsprechende Taste betätigen
3.5: Balance Board ausrichten und eine beliebige Taste zur Justierung drücken

4.: Spielen!

--> Doom: Balance Board nach links / rechts drehen ^^ im Spiel nach links / rechts drehen
          Balance Board nach links / rechts neigen ^^ im Spiel Strafe links / rechts
          Balance Board nach vorn / hinten neigen ^^ im Spiel vorwärts / rückwärts laufen

--> Trackmania: Balance Board nach links / rechts drehen ^^ im Spiel nach links / rechts lenken
                Balance Board nach vorn / hinten neigen ^^ im Spiel beschleunigen / bremsen (bzw. Rückwärtsgang)

Information: Wenn das Spiel gewechselt wird, muss das Balance Board ab- und wieder angeschlossen werden. Nur so geht der Inhalt der Variablen im Programm verloren und das Balance Board landet wieder in der Spielauswahl. Ein Soft Reset reicht nicht aus.
