import pandas as pd
import numpy  as np
print(''' - The board will be represented by a two dimensional matrix that contains unique identifiers for each block.
 - The board will have a unique identifier which represents the goal.
 - The board will have a unique identifier which represents the red block or main block.
 - A block that is longer lengthwise than heightwise can only be moved horizontally one space or more.
 - A block that is longer heightwise than lengthwise can only be moved vertically one space or more.
 - A block that is equal in length and height cannot exist. 
 - A block can not be moved through another block.
 - Only the main block can take the spot of the goal on the board.
 - The game will end when the player has managed to slide the main block into the goal.''')
df=pd.read_csv('Borden/Rushhour6x6_3.csv')

finished=False
dimensionx=6
dimensiony=6
board=np.arange(dimensionx,dimensiony)