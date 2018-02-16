#CSCI220-F15-Assign5-JS-py
#Jake Schwarztrauber
#Hang Man

from random import randrange
from graphics import*

#gets words form .txt document and puts them in a list
def wordList():
    infile = open("CSCI220-F15-Assign5.wordList.txt","r")
    wordList = []
    for line in infile:         
        wordList.append(line.rstrip('\n'))
    #end for
    return wordList
#end main

#gets list of words and picks a random word from the list.
def randomWordPick(listOfWords):
    count = 0
    for index in listOfWords:         
        count = count + 1
    #end for
    randomPick = randrange(0,count)   
    randomWord = listOfWords[randomPick]
    return randomWord.lower()
#end randomWordPick

#gets a word and turns it to blank spaces "_ _ _ _"
def displayWord(word):
    letterCount = 0
    for letter in word:
        letterCount = letterCount + 1
    #end for
    blank = "_"*letterCount
    return blank
#end displayWord

#undraws Hangman body parts
def undrawAll(head,body,LArm,rArm,LLeg,rLeg):
    head.undraw()
    body.undraw()
    LArm.undraw()
    rArm.undraw()
    LLeg.undraw()
    rLeg.undraw()
    
#plays HangMan with a word
def playHangman(word,win):
    #define hang man body parts position and color. Head, Body, Arms, Legs, Eyes
##############################################################################
    head = Polygon(Point(292,80),Point(283,79),Point(278,87),Point(275,90)
            ,Point(273,96),Point(271,100),Point(273,101),Point(279,110)
            ,Point(286,112),Point(292,110),Point(301,111),Point(314,109)
            ,Point(314,105),Point(313,93),Point(309,86),Point(306,84)
            ,Point(303,83),Point(299,82))
    head.setFill("yellow")
    
    body = Polygon(Point(306,111),Point(305,110),Point(300,110),Point(298,110)
                   ,Point(297,112),Point(293,112),Point(286,113),Point(284,113)
                   ,Point(278,112),Point(278,112),Point(276,112),Point(272,114)
                   ,Point(270,116),Point(261,121),Point(260,121),Point(265,129)
                   ,Point(270,132),Point(272,132),Point(277,135),Point(277,135)
                   ,Point(277,136),Point(276,143),Point(276,143),Point(276,151)
                   ,Point(283,150),Point(290,152),Point(295,152),Point(302,151)
                   ,Point(304,151),Point(305,141),Point(305,139),Point(304,135)
                   ,Point(304,131),Point(307,127),Point(319,131),Point(320,131)
                   ,Point(320,132),Point(322,121),Point(324,114),Point(322,114)
                   ,Point(316,115),Point(312,113))
    body.setFill("blue")
    
    LArm = Polygon(Point(263,126),Point(254,137),Point(249,141),Point(253,148)
                   ,Point(253,148),Point(257,147),Point(259,144),Point(260,140)
                   ,Point(260,139),Point(267,130))
    LArm.setFill("yellow")
    rArm = Polygon(Point(322,127),Point(333,132),Point(334,136),Point(338,137)
                   ,Point(345,135),Point(347,133),Point(347,128),Point(347,126)
                   ,Point(347,125),Point(341,123),Point(338,125),Point(324,120))
    rArm.setFill("yellow")
    
    LLeg = Polygon(Point(277,151),Point(269,182),Point(283,182),Point(290,164)
                   ,Point(289,153))
    LLeg.setFill("brown")
    
    rLeg = Polygon(Point(304,152),Point(312,183),Point(299,180),Point(293,164)
                    ,Point(290,161),Point(289,153))
    rLeg.setFill("brown")
    
    leftEye = Line(Point(280,88),Point(287,97))
    leftEye2 = Line(Point(287,89),Point(280,95))
    rightEye = Line(Point(298,87),Point(305,96))
    rightEye2 = Line(Point(307,88),Point(297,93))
###############################################################################
    blanks = displayWord(word)
    blanksList = list(blanks)
    numberOfWrongGuesses = 0
    usedChars = []
    #set variables for game
    wordGuessed = False
    #messages used in program
    charGuessText = Text(Point(351,360),"Enter a Letter:")
    charGuessEntry = Entry(Point(415,360),2)
    submitButton = Rectangle(Point(307,388),Point(388,415))
    submitButton.setFill("white")
    submitText = Text(Point(347,402),"Submit")
    AlreadyMessage = Text(Point(351,320),"You already guessed that letter")
    AlphaMessage = Text(Point(351,320),"You have to guess a letter.")
    blankEntryMessage = Text(Point(351,320),"Enter a letter.")
    oneText=Text(Point(351,320),"Only guess one letter at a time. Try again.")
    diedText = Text(Point(351,320),"You died. Your word was '"+word+"'")
    winMessage=Text(Point(351,320),"Congratulations! You escaped the gallows!")
    #gets word and turns it into blanks
    #body parts used switched to unsued. False = not drawn, True = Already drawn
    headSwitch = False 
    bodySwitch = False
    LArmSwitch = False
    rArmSwitch = False
    LLegSwitch = False
    rLegSwitch = False
    faceSwitch = False
    #plays hangman with word while word is not guessed and number of wrong
    #guesses is less then 7
    while (numberOfWrongGuesses < 7) and (wordGuessed == False):
        #varibles to use in loop 
        correctGuess = False
        positionInWord = 0
#//////////////////////////////////////////////////////////////////////////////        
        #draws body parts for its respected number for respected wrong entry
        #and turns on body part so it only draws it once.
        if (numberOfWrongGuesses == 1) and (headSwitch == False):
            head.draw(win)
            headSwitch = True
        if (numberOfWrongGuesses == 2) and (bodySwitch == False):
            body.draw(win)
            bodySwitch = True
        if (numberOfWrongGuesses == 3) and (LArmSwitch == False):
            LArm.draw(win)
            LArmSwitch = True
        if (numberOfWrongGuesses == 4) and (rArmSwitch == False):
            rArm.draw(win)
            rArmSwitch = True
        if (numberOfWrongGuesses == 5) and (LLegSwitch == False):
            LLeg.draw(win)
            LLegSwitch = True
        if (numberOfWrongGuesses == 6) and (rLegSwitch == False):
            rLeg.draw(win)
            rLegSwitch = True
#//////////////////////////////////////////////////////////////////////////////
        #draw blanks for word in window
        displayBlanks = Text(Point(351,270)," ".join(blanksList))
        displayBlanks.draw(win)

        #Displays Text and number of wrong guesses
        gamePrompt = Text(Point(351,300),"Number of wrong guesses: "
                      +str(numberOfWrongGuesses))
        gamePrompt.draw(win)
        
        #Displays Text and Letters Used
        lettersUsedDisplay = Text(Point(351,330),"Letters Used: "
                                  +" ".join(usedChars))
        lettersUsedDisplay.draw(win)

        #Display "Enter a Letter" and Entry box to input a single letter
        charGuessText.draw(win)
        charGuessEntry.draw(win)

        #Submit [BUTTON]
        submitButton.draw(win)
        submitText.draw(win)
        submitButtonClicked = False
        #keep clicking until click lands on Submit [BUTTON]
        while submitButtonClicked == False:
            lookForSubmit = win.getMouse()
            X = lookForSubmit.getX()
            Y = lookForSubmit.getY()
            int(X)
            int(Y)
            #Submit [BUTTON] clicked
            if (X>307) and (X<388) and (Y>388) and (Y<415):
                submitButtonClicked = True
                submitButton.undraw()
                submitText.undraw()
            #end if
        #Gets Text from Entry box
        charGuess = charGuessEntry.getText().lower()
        charGuessEntry.setText("")
        #Undraw Prompts     
        gamePrompt.undraw()
        displayBlanks.undraw()
        lettersUsedDisplay.undraw()
        charGuessText.undraw()
        charGuessEntry.undraw()

        #if guess char was correct but guessed already. Prompt user
        if blanksList.count(charGuess) >=1:
            AlreadyMessage.draw(win)
            win.getMouse()
            AlreadyMessage.undraw()
        #end if
            
        #If one char was Entered in Entry box
        if (len(list(charGuess)) == 1):
            
            #checks to see if char guessed was a Alapha char
            if(ord(charGuess)>=ord("a") and ord(charGuess)<=ord("z")):
                
                #compares guessed char to each char in Game Word
                for ch in word:
                    
                    #if char guessed and char in game word match then
                    #mark as True and move to
                    #next position
                    if charGuess == ch:     
                        blanksList[positionInWord] = ch
                        correctGuess = True
                        positionInWord +=1
                    #end if
                            
                    #if chars do not match then move to the next positon
                    else:
                        positionInWord +=1
                    #end else
                #end for ch in word
                
                #User already guessed that incorrect letter
                if(usedChars.count(charGuess)==1):
                    AlreadyMessage.draw(win)
                    win.getMouse()
                    AlreadyMessage.undraw()
                #end if
                #User did not guess letter correctly and has not been guessed
                #before. Add letter to usedChars and +1 numberOfWrongGuesses
                if (correctGuess == False)and(usedChars.count(charGuess) == 0):
                    usedChars.append(charGuess)
                    numberOfWrongGuesses += 1
                #end if
                #if there are no more blanks in word then the
                #word was guessed correctly
                if blanksList.count("_") == 0:
                    wordGuessed = True
                #end if
            #end if
            #If they submit a non Alphabit char. Prompt them to try again.
            else:
                AlphaMessage.draw(win)
                win.getMouse()
                AlphaMessage.undraw()
            #end while
        #If no char was Entered . Prompt message and try again.
        elif (len(list(charGuess)) == 0):
            blankEntryMessage.draw(win)
            win.getMouse()
            blankEntryMessage.undraw()
        #end elif
        #If more than one char was Entered. Prompt message and try agian.
        else:
            oneText.draw(win)
            win.getMouse()
            oneText.undraw()
        #end else
    #They ran out of attempts to guess the word and lost. Tell them the correct
    #word and prompt them with message. Undraw Hangman
    if wordGuessed == False:
        #message
        diedText.draw(win)
        #Draw Eyes and then undraw them.
        leftEye.draw(win)
        leftEye2.draw(win)
        rightEye.draw(win)
        rightEye2.draw(win)
        win.getMouse()
        leftEye.undraw()
        leftEye2.undraw()
        rightEye.undraw()
        rightEye2.undraw()
        diedText.undraw()
        undrawAll(head,body,LArm,rArm,LLeg,rLeg)
    #end if
        
    #They guessed the word in 7 trys. Prompt them. Undraw Hangman
    else:
        correctWordText = Text(Point(351,270)," ".join(word))
        correctWordText.draw(win)
        winMessage.draw(win)
        win.getMouse()
        correctWordText.undraw()
        winMessage.undraw()
        undrawAll(head,body,LArm,rArm,LLeg,rLeg)
        displayBlanks.undraw()
        return win
    #end else
    
#end playHangman()

def main():
    win = GraphWin("Hangman JS", 700, 500)
    #messages
    playTextAgain = Text(Point(348,337),"Do you want to keep playing Hangman?")
    playText = Text(Point(348,337),"Do you want to to play Hangman?")
    gameOverText = Text(Point(348,337),"There are no words left! Game Over!")
    byeText = Text(Point(348,337),"BYE!")
    #[BUTTONS]
    yesButton = Rectangle(Point(206,265),Point(290,301))
    yesButton.setFill("green")
    yesButtonText = Text(Point(246,284),"YES")
    noButton = Rectangle(Point(417,265),Point(501,301))
    noButton.setFill("red")
    noButtonText = Text(Point(458,283),"NO")

    #draw gallows and fill color
    gallows = Polygon(Point(254,210),Point(368,211),Point(364,64)
                ,Point(303,61),Point(303,80),Point(284,78),Point(284,49)
                ,Point(366,42),Point(394,41),Point(389,208),Point(473,206)
                ,Point(475,227),Point(253,227))
    gallows.setFill("brown")
    gallows.draw(win)
    
    #Display Text asking if you want to play YES NO buttons to choose
    playText.draw(win)
    #Yes [BUTTON]
    yesButton.draw(win)
    yesButtonText.draw(win)
    #No [BUTTON]
    noButton.draw(win) 
    noButtonText.draw(win)

    #Variable that will turn True once a button is clicked
    clickedButton = False
    #While Button is not clicked look for a user to click on a button
    while (clickedButton == False):
        #Sees where user clicked
        catchClick = win.getMouse()
        catchX = int(catchClick.getX())
        catchY = int(catchClick.getY())
        #If they clicked Yes [BUTTON]
        if (catchX > 206)and(catchX < 290)and(catchY > 265)and(catchY < 301):
            clickedButton = True
            #undraw question and YES NO [BUTTONS]
            playText.undraw()
            yesButtonText.undraw()
            yesButton.undraw()
            noButtonText.undraw()
            noButton.undraw()
            
            #Gets list of words from .txt document
            listOfWords = wordList()
            lastGoAround = 1
            UserWantsToPlay = True
            #LOOP WHILE THERE ARE WORDS TO PLAY WITH and USER WANTS TO PLAY
            while (lastGoAround <= len(listOfWords))and(UserWantsToPlay == True):
                gameWord = randomWordPick(listOfWords)
                listOfWords.remove(gameWord)
                #>>>>>>>>>>>PLAY HANGMAN WITH ONE WORD FROM LIST<<<<<<<<<<<<<
                playHangman(gameWord, win)
#**********DISPLAY BUTTONS AND TEXT TO ASK IF THY WANT TO PLAY AGAIN***********
                yesButton.draw(win)
                yesButtonText.draw(win)
                noButton.draw(win)
                noButtonText.draw(win)
                playTextAgain.draw(win)
                clickButtonAgain = False

                #keep clicking until you hit a button
                while(clickButtonAgain == False):
                    catchClick2 = win.getMouse()
                    X2 = int(catchClick2.getX())
                    Y2 = int(catchClick2.getY())
                    #If they clicked Yes [BUTTON] play again
                    if(X2>206)and(X2<290)and(Y2>265)and(Y2<301):
                        clickButtonAgain = True
                        yesButtonText.undraw()
                        yesButton.undraw()
                        noButtonText.undraw()
                        noButton.undraw()
                        playTextAgain.undraw()
                    #end if
                    #If they clicked the NO [BUTTON] end game
                    elif(X2>417)and(X2<501)and(Y2>265)and(Y2<301):
                        clickButtonAgain = True
                        yesButtonText.undraw()
                        yesButton.undraw()
                        noButtonText.undraw()
                        noButton.undraw()
                        playTextAgain.undraw()
                        UserWantsToPlay = False
                    #end elif
#******************************************************************************
                #There are no more words to play with. Prompt them and end game
                if (len(listOfWords) == 0):
                    UserWantsToPlay == False
                    gameOverText.draw(win)
                    win.getMouse()
                    gameOverText.undraw()
                #end if     
        #If they clicked the NO [BUTTON]
        elif(catchX>417)and(catchX<501)and(catchY>265)and(catchY<301):
            clickedButton = True
        #end if
            #undraw question and YES NO [BUTTONS]
            playText.undraw()
            yesButtonText.undraw()
            yesButton.undraw()
            noButtonText.undraw()
            noButton.undraw()
    #end while
    #BYE! and end program
    byeText.draw(win)
    win.getMouse()
    win.close()
            
main()


