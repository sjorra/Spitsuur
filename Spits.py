import pandas as pd
import numpy  as np
print(''' - Bord heeft 2 dimensies met unieke identificatie per auto
 - Unieke identificatie voor doelstelling (poortje)
 - Unieke identificatie voor de rode auto
 - Verticale orientatie van auto's
 - Horizontale orientatie van auto's 
 - Een blok kan niet door een ander blok
 - Alleen de rode auto kan door de poort
 - Het spel is over al de rode auto door de poort is''')
inputboard=pd.read_csv('Borden/Rushhour6x6_3.csv')

finished=False
dimensionx=6
dimensiony=6
boarddummy=np.zeros((dimensionx+2,dimensiony+2), int).astype(str)

boarddummy[0]='|'
boarddummy[-1]='|'

for x in boarddummy:
	x[0]='|'
	x[-1]='|'
boarddummy[(len(boarddummy)-int(len(boarddummy)/2)-1)][-1]='.'
print (inputboard)
def populateboard(inputboard):
	boardfilled=boarddummy
	for row in inputboard.itertuples():

		boardfilled[row.row][row.col]=boardfilled[row.row][row.col].replace('0',row.car)
		if row.orientation=='H':
			boardfilled[row.row][row.col-1]=boardfilled[row.row][row.col-1].replace('0',row.car)
			if row.length==3:
				boardfilled[row.row][row.col-2]=boardfilled[row.row][row.col-2].replace('0',row.car)
		if row.orientation=='V':
			boardfilled[row.row-1][row.col]=boardfilled[row.row-1][row.col].replace('0',row.car)
			if row.length==3:
				boardfilled[row.row-2][row.col]=boardfilled[row.row-2][row.col].replace('0',row.car)
	return boardfilled
print(populateboard(inputboard))
