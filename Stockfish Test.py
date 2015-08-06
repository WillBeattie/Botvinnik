# -*- coding: utf-8 -*-
"""
Created on Thu Aug 06 09:58:04 2015

@author: Will
"""

import os
import subprocess
import time

os.chdir("C:/Users/Will/My Documents/Botvinnik/Stockfish")

#Sends a command to the engine process and prints the command to the console
def put(command):
    #print('\nYou: \n\t'+command)
    engine.stdin.write(command+'\n')

#Receives the response lines from the engine process.  The engine will only respond to 'isready' when it's done thinking (except for thinking in infinite mode)
def get():
    engine.stdin.write('isready\n')
    #print('\nEngine:')
    while True:
        text=engine.stdout.readline().strip()
        if text=='readyok':
            break
        if text!='':
            print('\t'+text)
            
def getMove():
    put('stop')
    while True:
        text=engine.stdout.readline().strip()
        if text[0:8]=="bestmove":  #Stockfish spits out a bunch of lines before declaring the best move
            move=text.split(' ')[1]            
            print 'The engine plays: '+move
            return move
            break   

engine=subprocess.Popen(
    'stockfish-6-32.exe',
    universal_newlines=True,
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    )
    
position='position startpos moves'
get() #Stockfish writes a line on startup.  This confirms the process is running

while True:
    print "Game position: "+" ".join(position.split(' ')[3:]) +'\n'
    move=raw_input("Enter your move: ")
    position+=' '+move    
    put(position)
    get()
    put('go infinite')
    time.sleep(2)
    move=getMove()
    position += ' '+move
