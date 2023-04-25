C_speed = 1000  #vitesse 
C_position_first_tool = 44  #position de C quand la fraise est en place dans le tourniquet a la position outil 1
C_position_last_tool = 355 #position de C quand la fraise est en place dans le tourniquet a la position du dernier outil
Tool_count = 8  #nombre d'outil max
C = 5  

hold_tool = d.getSpindleToolNumber()  #recupère le numero de l'ancien outil
position = d.getPosition(CoordMode.Machine) #récupère la positon machine

if 1 <= hold_tool <= Tool_count: #vérifi que l'outil n'est pas zero ou plus que tool_count
    hold_tool_position_C = ((C_position_last_tool - C_position_first_tool) / (Tool_count - 1) * (hold_tool-1)) + C_position_first_tool #calcul de l'écatement etre chaques rangement.
else:
    print(f"Le numéro de l'outil actuel ({hold_tool}) dépasse le nombre maximal d'outils autorisé ({Tool_count})")

print(f"La position de l'outil actuel est : {hold_tool_position_C}")

#mouvement A en position d'outil hold_tool 
position[C] = hold_tool_position_C
d.moveToPosition(CoordMode.Machine, position,C_speed)