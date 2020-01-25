# -*- coding: utf-8 -*-
"""
Created on Sunday January 12 2020

@author: hovekama
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = testUtility.get_player_names();

#number of curses and victory cards
nV = testUtility.get_nV(player_names)
nC = testUtility.get_nC(player_names)

nV = 0;  # we introduce a bug where nV is set to zero

#Define box
box = testUtility.get_boxes(nV)

supply_order = testUtility.get_supply_order()

supply = testUtility.supply_init(box, player_names, nV, nC)



#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.get_players(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)


#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.min()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
