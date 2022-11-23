#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:24:11 2019

@author: david.thomas
"""

# built on John Zelle's graphics.py
# https://mcsp.wartburg.edu/zelle/python/graphics.py

from graphics import *
from timeit import default_timer as timer
import random

def playGame():
    
    point1=Point(140,140)
    point2=Point(300,140)
    point3=Point(460,140)
    point4=Point(140,300)
    point5=Point(300,300)
    point6=Point(460,300)
    point7=Point(140,460)
    point8=Point(300,460)
    point9=Point(460,460)
    
    vLine1=Line(Point(60,140),Point(540,140))
    vLine2=Line(Point(60,300),Point(540,300))
    vLine3=Line(Point(60,460),Point(540,460))
    vLine4=Line(Point(140,60),Point(140,540))
    vLine5=Line(Point(300,60),Point(300,540))
    vLine6=Line(Point(460,60),Point(460,540))
    vLine7=Line(Point(60,60),Point(540,540))
    vLine8=Line(Point(60,540),Point(540,60))
    vLinesList=[vLine1,vLine2,vLine3,vLine4,vLine5,vLine6,vLine7,vLine8]
    for vLine in vLinesList:
        vLine.setWidth(10)

    gameBoard=[[" "," "," "],[" "," "," "],[" "," "," "]]
    numTurns=0
    randDict={0:"X",1:"O"}
    whoseTurn=randDict[random.randint(0,1)]
    nextTurn={"X":"O","O":"X"}
    turnColor={"X":'red',"O":'blue'}
    squareDict={point1:[0,0],point2:[0,1],point3:[0,2],point4:[1,0],point5:[1,1],point6:[1,2],point7:[2,0],point8:[2,1],point9:[2,2]}    
    

    def drawX(point):
        cross1=Line(Point(point.getX()-60,point.getY()-60),Point(point.getX()+60,point.getY()+60))
        cross2=Line(Point(point.getX()-60,point.getY()+60),Point(point.getX()+60,point.getY()-60))
        cross1.setWidth(5)
        cross2.setWidth(5)
        cross1.setOutline('red')
        cross2.setOutline('red')
        cross1.draw(win)
        cross2.draw(win)
        
    def drawO(point):
        circle=Circle(point,60)
        circle.setWidth(5)
        circle.setOutline('blue')
        circle.draw(win)
    
    def userClick():
        clickedColumn=0
        clickedRow=0
        selectedSquare=0
        while selectedSquare==0:
            clickedPoint=win.getMouse()
            if clickedPoint.getX()>70 and clickedPoint.getX()<210:
                clickedColumn=1
            if clickedPoint.getX()>230 and clickedPoint.getX()<370:
                clickedColumn=2
            if clickedPoint.getX()>390 and clickedPoint.getX()<530:
                clickedColumn=3
            if clickedPoint.getY()>70 and clickedPoint.getY()<210:
                clickedRow=1
            if clickedPoint.getY()>230 and clickedPoint.getY()<370:
                clickedRow=2
            if clickedPoint.getY()>390 and clickedPoint.getY()<530:
                clickedRow=3
            if clickedRow==1 and clickedColumn==1:
                selectedSquare=point1
            if clickedRow==1 and clickedColumn==2:
                selectedSquare=point2
            if clickedRow==1 and clickedColumn==3:
                selectedSquare=point3
            if clickedRow==2 and clickedColumn==1:
                selectedSquare=point4
            if clickedRow==2 and clickedColumn==2:
                selectedSquare=point5
            if clickedRow==2 and clickedColumn==3:
                selectedSquare=point6
            if clickedRow==3 and clickedColumn==1:
                selectedSquare=point7
            if clickedRow==3 and clickedColumn==2:
                selectedSquare=point8
            if clickedRow==3 and clickedColumn==3:
                selectedSquare=point9
            if clickedPoint.getX()>590 and clickedPoint.getX()<597 and clickedPoint.getY()>3 and clickedPoint.getY()<10:
                win.close()
                return "quit"
                break
        return selectedSquare 
    
    def playerOturn():
        textMessage.setText("Player O's turn.")
        textMessage.setFill('blue')
        
    def playerXturn():
        textMessage.setText("Player X's turn.")
        textMessage.setFill('red')
            
    def whoWon(board):
        if board[0][0]==board[0][1]==board[0][2]!=" ":
            try:
                vLine1.draw(win)
            except:
                pass
            return(board[0][0])
        elif board[1][0]==board[1][1]==board[1][2]!=" ":
            try:
                vLine2.draw(win)
            except:
                pass            
            return(board[1][0])
        elif board[2][0]==board[2][1]==board[2][2]!=" ":
            try:
                vLine3.draw(win)
            except:
                pass            
            return(board[2][0])
        elif board[0][0]==board[1][0]==board[2][0]!=" ":
            try:
                vLine4.draw(win)
            except:
                pass            
            return(board[0][0])
        elif board[0][1]==board[1][1]==board[2][1]!=" ":
            try:
                vLine5.draw(win)
            except:
                pass            
            return(board[0][1])
        elif board[0][2]==board[1][2]==board[2][2]!=" ":
            try:
                vLine6.draw(win)
            except:
                pass            
            return(board[0][2])
        elif board[0][0]==board[1][1]==board[2][2]!=" ":
            try:
                vLine7.draw(win)
            except:
                pass            
            return(board[0][0])
        elif board[0][2]==board[1][1]==board[2][0]!=" ":
            try:
                vLine8.draw(win)
            except:
                pass            
            return(board[0][2])


    win=GraphWin("Tic-Tac-Toe",600,620)
    line1=Line(Point(60,220),Point(540,220))
    line2=Line(Point(60,380),Point(540,380))
    line3=Line(Point(220,60),Point(220,540))
    line4=Line(Point(380,60),Point(380,540))
    line1.setWidth(3)
    line2.setWidth(3)
    line3.setWidth(3)
    line4.setWidth(3)
    line1.draw(win)
    line2.draw(win)
    line3.draw(win)
    line4.draw(win)
    quitBox=Rectangle(Point(597,3),Point(590,10))
    quitBox.setFill('red')
    quitBox.draw(win)
    if whoseTurn=="X":
        textMessage=Text(Point(300,580),"Player X's turn")
        textMessage.setFill('red')
    if whoseTurn=="O":
        textMessage=Text(Point(300,580),"Player O's turn")
        textMessage.setFill('blue')
    textMessage.setSize(36)
    textMessage.draw(win)
    
    while numTurns<9:
        thisMove=userClick()
        if thisMove=="quit":
            break
        if gameBoard[int(squareDict[thisMove][0])][int(squareDict[thisMove][1])]==" ":
            gameBoard[int(squareDict[thisMove][0])][int(squareDict[thisMove][1])]=whoseTurn
            if whoseTurn=="X":
                drawX(thisMove)
                playerOturn()
            if whoseTurn=="O":
                drawO(thisMove)
                playerXturn()
            for vLine in vLinesList:
                vLine.setFill(turnColor[whoseTurn])
            numTurns+=1
            whoseTurn=nextTurn[whoseTurn]
        if whoWon(gameBoard)=="X" or whoWon(gameBoard)=="O":
            break
    
    if whoWon(gameBoard)!="X" and whoWon(gameBoard)!="O":
        textMessage.setText("It's a draw.")
        textMessage.setFill('black')
    elif whoWon(gameBoard)=="X":
        textMessage.setText("Player X wins!")
        textMessage.setFill('red')
    elif whoWon(gameBoard)=='O':
        textMessage.setText("Player O wins!")
        textMessage.setFill('blue')
    
    start=timer()
    while True:
        end=timer()
        if end-start>5:
            win.close()
            break
        

playGame()