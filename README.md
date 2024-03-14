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

2.: PC vorbereiten
2.1: Mu downloaden: https://codewith.mu/
2.2: Mu installieren
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
2.10: Trackmania Nations Forever downloaden:  
