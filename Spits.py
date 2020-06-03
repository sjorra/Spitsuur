#Dit bestand kan als af beschouwt worden omdat het de indeling van het bord projecteert. Het simuleren van stappen is de volgende stap van het geheel

import pandas as pd
import numpy  as np
import os
print(''' - Bord heeft 2 dimensies met unieke identificatie per auto
 - Unieke identificatie voor doelstelling (poortje)
 - Unieke identificatie voor de rode auto
 - Verticale orientatie van auto's
 - Horizontale orientatie van auto's 
 - Een blok kan niet door een ander blok
 - Alleen de rode auto kan door de poort
 - Het spel is over al de rode auto door de poort is''')
file_path='Borden/Rushhour6x6_3.csv'
inputboard=pd.read_csv(file_path) 																	#inlezen indeling bord

finished=False 																						#constraint voor beeindigen simulatie


dimension=int(file_path[-7]) 																		#definieer dimensie op basis van bestandsnaam
boarddummy=np.zeros((dimension+2,dimension+2), int).astype(str) 									#Creeer een array met nullen op basis van dimensie om vol te zetten met auto's

boarddummy[0]='|'																					#eerste rij van muren voorzien
boarddummy[-1]='|'																					#laatste rij van muren voorzien

for x in boarddummy:	
	x[0]='|'																						#eerste kolom van muren voorzien
	x[-1]='|'																						#laatste kolom van muren voorzien

boarddummy[(len(boarddummy)-int(len(boarddummy)/2)-1)][-1]='.'										#creer poortje aangegeven met '.'
print (inputboard)

def populateboard(inputboard):																		#Functie om het dummy bord op basis van de input van auto's te voorzien
	boardfilled=boarddummy
	for row in inputboard.itertuples():																#loop door input dataframe
		boardfilled[row.row][row.col]=boardfilled[row.row][row.col].replace('0',row.car)			#Vervang 0 met de relevante auto letter
		if row.orientation=='H':																	#check of de auto horizontaal of verticaal is georienteerd om te bepalen waar de volgende letter moet komen
			boardfilled[row.row][row.col-1]=boardfilled[row.row][row.col-1].replace('0',row.car)
			if row.length==3:																		#check hoe groot de auto is om te bepalen of er nog een derde letter bij moet komen
				boardfilled[row.row][row.col-2]=boardfilled[row.row][row.col-2].replace('0',row.car)
		if row.orientation=='V':
			boardfilled[row.row-1][row.col]=boardfilled[row.row-1][row.col].replace('0',row.car)
			if row.length==3:
				boardfilled[row.row-2][row.col]=boardfilled[row.row-2][row.col].replace('0',row.car)
	return boardfilled
print(populateboard(inputboard))
