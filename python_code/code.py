print("Justins Doom- und Trackmania-Steuerung")
print("(d)oom oder (t)rackmania?")
# Import der Bibliotheken
import sys
import time
import board
import busio
import usb_hid
from adafruit_hid.mouse import Mouse
m = Mouse(usb_hid.devices) # Einrichtung der emulierten Maus, Benennung als "m"
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
kbd = Keyboard(usb_hid.devices) # Einrichtung der emulierten Tastatur, Benennung als "kbd"
game = "" # Variable für Spielauswahl
dump = "" # Dump-Variable
yaw_start = 0 # Referenzvariablen, in denen später die beim Start des Sensors übermittelten Werte gesichert werden
pitch_start = 0
roll_start = 0
yaw_aktuell = 0
pitch_aktuell = 0
roll_aktuell = 0
w_flushed = True # Hilfsvariablen um zu ueberpruefen, ob der Keyboard-Buffer bereits geleert wurde
s_flushed = True
w_pressed = False # Hilfsvariablen um zu ueberpruefen, ob der entsprechende Tastendruck bereits emuliert wurde (um mehrere Triggerungen und einen Ueberlauf des Keyboard-Buffers zu vermeiden)
s_pressed = False
a_flushed = True
d_flushed = True
a_pressed = False
d_pressed = False
up_flushed = True
up_pressed = False
down_flushed = True
down_pressed = False
right_flushed = True
right_pressed = False
left_flushed = True
left_pressed = False

uart = busio.UART(tx=board.GP4, rx=board.GP5, baudrate=115200, receiver_buffer_size=2048) # Konfiguration der UART-Verbindung zwischen Raspberry Pi Pico und BNO08x

spiel = "" # Variable für Spielauswahl
spiel+=(sys.stdin.read(1))
if spiel == "d":
    game = "doom"
if spiel == "t":
    game = "trackmania"
print("Ausgewählt: ", game)
print("Balance-Board ausrichten, beliebige Taste für Justierung drücken!")
dump+=(sys.stdin.read(1)) # Input der beliebigen Taste dumpen

from adafruit_bno08x_rvc import BNO08x_RVC  # Bibliothek für den BNO08x-Sensor importieren

rvc = BNO08x_RVC(uart) # Dem Sensor die oben konfigurierte UART-Verbindung zuweisen

yaw, pitch, roll, x_accel, y_accel, z_accel = rvc.heading # Vom Sensor übermittelte Werte abfragen
yaw_start = yaw # Diese Werte in den oben erstellten Referenzvariablen speichern. Diese dienen im Laufe des Hauptprogramms als Bezugsvariablen um den aktuellen yaw, roll und pitch auszurechnen
pitch_start = pitch
roll_start = roll
mausgeschwindigkeit_links = 0 # Zwischenspeicher für die berechnete Mausgeschwindigkeit in Abhängigkeit der Balance-Board-Neigung
mausgeschwindigkeit_rechts = 0
print("Justierung erfolgreich!") # Wird nur gedruckt, wenn eine Verbindung zum Sensor hergestellt werden konnte, sonst taucht im REPL eine Fehlermeldung auf
while True: # Unendliche Programmschleife, solang Controller aktiv
    yaw, pitch, roll, x_accel, y_accel, z_accel = rvc.heading # Kontinuierliches Auslesen der aktuellen Sensorwerte
    yaw_aktuell = yaw_start - yaw # Berechnung der aktuellen Werte in Bezug auf die Startwerte (um die eigentliche Neigungsdifferenz des Sensors ermitteln zu können).
    pitch_aktuell = pitch_start - pitch
    roll_aktuell = roll_start - roll
    yaw_aktuell = int(yaw_aktuell)
    pitch_aktuell = int(pitch_aktuell)
    roll_aktuell = int(roll_aktuell)
    if roll_aktuell < -5 and game == "doom" and w_pressed == False: # Einrichtung von Totpunkten um den Nullpunkt des Balance-Boardes herum, Kontrolle des gewählten Spiels und WICHTIG: Kontrolle ob die Taste im letzten Zyklus nicht bereits gesendet wurde: Vermeidung von Keyboard-Buffer-Overflows!
        kbd.press(Keycode.W)
        w_flushed = False
        w_pressed = True
    if roll_aktuell < -5 and game == "trackmania" and up_pressed == False:
            kbd.press(Keycode.UP_ARROW)
            up_flushed = False
            up_pressed =True
    if roll_aktuell > 5 and game == "doom" and s_pressed == False:
        kbd.press(Keycode.S)
        s_flushed = False
        s_pressed = True
    if roll_aktuell > 5 and game == "trackmania" and down_pressed == False:
            kbd.press(Keycode.DOWN_ARROW)
            down_flushed = False
            down_pressed = True
    if pitch_aktuell < -5 and game == "doom" and d_pressed == False:
        kbd.press(Keycode.D)
        d_flushed = False
        d_pressed = True
    if pitch_aktuell > 5 and game == "doom" and a_pressed == False:
        kbd.press(Keycode.A)
        a_flushed = False
        a_pressed = True
    if yaw_aktuell > 2 and game == "doom": # Bewegung der Maus bei Doom, wenn das Balance-Board in der x-y-Ebene gedreht wird mit der berechneten Mausgeschwindigkeit (siehe Ende des Source Codes)
      m.move(int(mausgeschwindigkeit_links),0,0)
    if yaw_aktuell > 10 and game == "trackmania" and left_pressed == False:
        kbd.press(Keycode.LEFT_ARROW)
        left_flushed = False
        left_pressed = True
    if yaw_aktuell < -2 and game == "doom":
      m.move(int(mausgeschwindigkeit_rechts),0,0)
    if yaw_aktuell < -10 and game == "trackmania" and right_pressed == False:
      kbd.press(Keycode.RIGHT_ARROW)
      right_flushed = False
      right_pressed = True
    if roll_aktuell > -5 and roll_aktuell < 0 and w_flushed == False: # Code snippets die sicherstellen, dass im Totpunkt die entsprechend emulierten Taster wieder losgelassen werden
      kbd.release(Keycode.W)
      w_flushed = True
      w_pressed = False
    if roll_aktuell > 0 and roll_aktuell < 5 and s_flushed == False:
      kbd.release(Keycode.S)
      s_flushed = True
      s_pressed = False
    if pitch_aktuell > 0 and pitch_aktuell < 5 and d_flushed == False:
      kbd.release(Keycode.D)
      d_flushed = True
      d_pressed = False
    if pitch_aktuell > 0 and pitch_aktuell < 5 and a_flushed == False:
      kbd.release(Keycode.A)
      a_flushed = True
      a_pressed = False
    if roll_aktuell > -5 and roll_aktuell < 0 and up_flushed == False:
      kbd.release(Keycode.UP_ARROW)
      up_flushed = True
      up_pressed = False
    if roll_aktuell > 0 and roll_aktuell < 5 and down_flushed == False:
      kbd.release(Keycode.DOWN_ARROW)
      down_flushed = True
      down_pressed = False
    if yaw_aktuell > 0 and yaw_aktuell < 10 and right_flushed == False:
      kbd.release(Keycode.RIGHT_ARROW)
      right_flushed = True
      right_pressed = False
    if yaw_aktuell < 0 and yaw_aktuell > -10 and left_flushed == False:
      kbd.release(Keycode.LEFT_ARROW)
      left_flushed = True
      left_pressed = False
    mausgeschwindigkeit_links = -(5/4) * yaw_aktuell + (5/2) # Berechnung der Mausgeschwindigkeit für links und rechts in Abhängigkeit des Drehwinkels vom Balance-Board (zwei lineare Funktionen, die zwischeneinander um den Koordinatenursprung herum einen Totpunkt bilden)
    mausgeschwindigkeit_rechts = -(5/4) * yaw_aktuell - (5/2)
