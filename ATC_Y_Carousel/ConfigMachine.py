# Disclaimer: The provided code is open-source and free to use, modify, and distribute. 
# The author shall not be held responsible for any injury, damage, or loss resulting from the use of this code.
# By using this code, you agree to assume all responsibility and risk associated with the use of the code.

# Change tool script for SIMCNC & Csmio-s 
# Erwan Le Foll 24/04/2022   version 0.6   https://youtube.com/@erwan3953

# Script de changement d'outil automatique pour un chargeur d'outil avec TOURNIQUET
# ici le moteur du tourniquet est sur l'axe C en degrés (ou Lineair mm.) pour les Axes en degré comfigurer> axes> C> RotaryType (1->360) permet de prendre le chemain le plus court


#-----------------------------------------------------------
# INfos sur la machine (Machine informations)
#-----------------------------------------------------------

# vitesse (speed)
Z_speed_down = 1000                 # vitesse Z en décente 
Z_speed_up = 2000                   # viteese de lever du Z (speed to lift Z)
Y_speed = 2000                      # Vitesse  y (speed of 
Y_speed_final = 300                 # Vitesse  y d'aproche finale pour ranger l'outil
C_speed = 1000                      # vitesse de C "porte outils"

# positions
time_spindle_stop = 8               # temps en seconde  de l'arrete de votre broche avec l'outil le plus lourd (time in seconds for the stop of your spindel with the heaviest tool)
Y_approch = -230                    # position y de la broche avant de rentrer l'outil de la port outil
Y_tool_clamp= -300                  # position y final de la broche dans un porte outil
Z_position_clean = -120             # distance a la quel le z descent pour nettoyage du cone
Z_position_tools = -150             # emplacement Z ou l'outil est libéré (location where the tool is released)

#Carouselle                         # Important, le homming du carouselle doit etre 0,00 ou < que C_position_first_tool 
C_position_first_tool = 40          # position de C quand la fraise est en place dans le tourniquet a la position 1
C_position_last_tool = 355          # position de C quand la fraise est en place dans le tourniquet a la position du dernier outil

# numeros d'entrée/sorties
Tool_Count = 8                      # Nombre max. d'outils dans le port outils
check_tool_in_spindel = None #S3    # Numéro de l'entrée numérique qui gère le détecteur d'outil inséré  None=desactivé (Digital input number managing the tool detection sensor)
check_clamp_status = None    #S2    # Numéro de l'entrée numérique qui gère le détecteur d'ouverture de la griffe du conne None=desactivé (Digital input number managing the cone clamp open sensor)
valve_collet = 13                   # Numéro de la sortie numérique qui gère la valve pour le changement d'outil (Digital output number managing the valve for tool change)
valve_clean_cone = 15               # Numéro de la sortie numérique qui gère la valve pour le nettoyage du cone du porte outil (Digital output number managing the valve for tool holder cone cleaning)
valve_blower = 12                   # Numéro de la sortie numérique qui gère la valve de la soufflette None=desactivé (Digital output number managing the valve for the blower)
valve_dor = 11                      # Numéro de la sortie numérique qui gère la valve d'ouverture porte du tourniquet None=desactivé
valve_dust_colector = 14            # Numéro de la sortie numérique qui gère la valve du levage de récupérateur de poussières None=desactivé
blowing_time = 0.5                  # temps en seconde du coup de soufflette a la dépose d'un outil ou a la mesure (Time in seconds of the blower at the tool drop or measurement).

#-----------------------------------------------------------
# Infos sur le Contacteur de palpage (probing infos)
#-----------------------------------------------------------

do_i_have_prob = False              # True = mesure d'outil activée. False = mesure d'outil desactivée
every_time_get_measure = True       # true = mesure a tous les coups, false = mesure que si la table d'outil est a zero (attention a chaques changements de fraise, c'est a vous de reset la table d'outil a Zero)
probeStartAbsPos = {'Y_probe': -85, 'Z_probe': -80} # Coordonnées de placement au dessus du prob [Y_probe, Z_probe] votre outil le plus long doit passer avec ce Z! (Placement coordinates above the probe [Y_probe, Y_probe, Z_probe] Your longest tool must pass with this Z!)
probeIndex = 0                      # corespond a l'entrée que vous avez configuré dans les settings de simcnc (0,1,2 ou 3 possible)
zEndPosition = -250                 # l'axe z ne descendra pas plus loint! (The Z-axis will not go down any further!)
refToolProbePos = -143.67           # hauteur a la quelle votre outil de reférénce touche le prob, (si votre outil de référence touche a Z-100mm et que vous indiquez - 100mm ici, alors il sera référencé 0mm) (Height at which your reference tool touches the probe (if your reference tool touches at Z-100mm and you indicate - 100mm here, then it will be referenced to 0mm))
fastProbeVel = 700                  # vitesse de la premiere mesure, rapide (units/min) (Speed of the first, fast measurement (units/min))
slowProbeVel = 250                  # vitesse du deuxieme mesure, lente (units/min) (Speed of the second, slow measurement (units/min))
goUpDist = 6                        # remontée en mm de Z entre les deux mesures (Z-axis up travel in mm between the two measurements)
fineProbingDelay = 0.2              # temps en secondes entre les deux mesures (Time in seconds between the two measurements)
checkFineProbingDiff = False        # ne pas changer (Do not change)
fineProbeMaxAllowedDiff = 0.1       # tolerence entre les deux mesures (tolerance between the two measurements)
moveX = True                        # ne pas changer (Do not change)
moveY = True                        # ne pas changer (Do not change)