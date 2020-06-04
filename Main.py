from Boards.CSVInterpreting import importcsv
from Boards.Populateboard import createboard, populateboard


filename = 'Rushhour6x6_1.csv'
car_setup = importcsv(filename)
empty_board = createboard(filename)

print(populateboard(car_setup, empty_board))