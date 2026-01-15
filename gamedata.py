import pygame
from sys import exit
#framerate = input ("set framerate").strip or 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)


def guigame1():
    pygame.init()
    screen = pygame.display.set_mode((800,400))
    pygame.display.set_caption('start menu')
    clock=pygame.time.Clock()
    lives=3
    placeholdertext= pygame.font.Font(None,21)
    questiontext=pygame.font.Font(None,50)
    placeholder_surface= pygame.image.load("images/startmenu.png")
    quizquestion_surface=pygame.image.load("images/Untitled.png")
    start_buttonimg=pygame.image.load("images/startbutton.png").convert_alpha()
    about_buttonimg=pygame.image.load("images/aboutbutton.png").convert_alpha()
    wrong_graphic=pygame.image.load("images/incorrect.png")
    mess=pygame.image.load("images/bigmess.png").convert_alpha()
    victoryscreen=pygame.image.load("images/winnerscreen.png")
    #answering buttons
    yes_button=pygame.image.load("images/yes.png").convert_alpha()
    no_button=pygame.image.load("images/no.png").convert_alpha()
    buttontemplate=pygame.image.load("images/answertemplate.png").convert_alpha()

    flag=True
    text_surface=placeholdertext.render('welcome to the graphical levels!,',False,'black')
    abouttext1=placeholdertext.render("created by notwebmaker",False,"black")
    abouttext2=placeholdertext.render("graphics- notwebmaker and johnny b(not real name)",False,"black")
    abouttext3=placeholdertext.render("inspired by The impossible quiz by splapp me do and other puzzle games",False,"black")

    #question1 text
    question1=questiontext.render('Is this quiz finished?',False,'black')
    #question2 text
    question2=questiontext.render("69-2 gives you?",False,'black')
    option1q2=placeholdertext.render("Brainrot",False,'black')
    option2q2=placeholdertext.render("the meme is dead ",False,"black")
    option3q2=placeholdertext.render("67",False,"black")
    #question3 text
    question3=questiontext.render("What are politicians ?",False,"black")
    option1q3=placeholdertext.render("stupid",False,'black')
    option2q3=placeholdertext.render("intellectuals ",False,"black")
    option3q3=placeholdertext.render("lots of brains",False,"black")
    option4q3=placeholdertext.render("full of hot air",False,"black")
    #question4 text
    question4=questiontext.render("How many ads on youtube ?",False,"black")
    option1q4=placeholdertext.render("it depends on the video length",False,'black')
    option2q4=placeholdertext.render("100 ",False,"black")
    option3q4=placeholdertext.render("1",False,"black")
    option4q4=placeholdertext.render("infinity",False,"black") 
    #question5 text
    question5=questiontext.render("what is this?",False,"black")
    option1q5=placeholdertext.render("cat",False,'black')
    option2q5=placeholdertext.render("dog ",False,"black")
    option3q5=placeholdertext.render("a mess",False,"black")
    option4q5=placeholdertext.render("yes what is this?",False,"black")
    #question6 text
    question6=questiontext.render("For real life?",False,"black")
    option1q6=placeholdertext.render("For real life",False,'black')
    option2q6=placeholdertext.render("yes ",False,"black")
    option3q6=placeholdertext.render("not not really",False,"black")
    option4q6=placeholdertext.render("Absolutley",False,"black")
    #question7 text
    question7=questiontext.render("Who created this game?",False,"black")
    option1q7=placeholdertext.render("notamaker",False,'black')
    option2q7=placeholdertext.render("nobody knows ",False,"black")
    option3q7=placeholdertext.render("notawebmaker",False,"black")
    option4q7=placeholdertext.render("notwebmaker",False,"black")


    class Button():
        def __init__(self,x,y,image,scale):
            width = image.get_width()
            height = image.get_height() 
            self.image = pygame.transform.scale(image, [int(width * scale), int(height * scale)])
            self.rect= self.image.get_rect()
            self.rect.topleft =(x,y)
            self.clicked=False

        def draw(self):
            screen.blit(self.image,(self.rect.x, self.rect.y))

        def isClicked(self):
            action = False
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0] == 1 and self.clicked==False:
                    self.clicked=True
                    print("button works!")
                    action = True
                if pygame.mouse.get_pressed()[0]==0:
                    self.clicked=False
                     

            return action
            
    

    showStartImage=True
    start_button = Button(650, 250, start_buttonimg,1.1)
    whomadethiscrap =Button(650, 300,about_buttonimg,0.3 )
    ques1yes=Button(100, 230, yes_button,0.5)  
    ques1no=Button(500, 230, no_button,0.5)
    youwrong=Button(10, 20, wrong_graphic,0.4 )

    brainrot=Button(100,200,buttontemplate,0.4)
    incorrect1q2=Button(500,200,buttontemplate,0.4)
    incorrect2q2=Button(500,300,buttontemplate,0.4)
    incorrect3q2=Button(100,300,buttontemplate,0.4)

    
    incorrect1q3=Button(100,200,buttontemplate,0.4)
    hotair=Button(500,200,buttontemplate,0.4)
    incorrect2q3=Button(500,300,buttontemplate,0.4)
    incorrect3q3=Button(100,300,buttontemplate,0.4)
    
    incorrect1q4=Button(100,200,buttontemplate,0.4)
    correctans=Button(500,300,buttontemplate,0.4)
    incorrect2q4=Button(500,200,buttontemplate,0.4)
    incorrect3q4=Button(100,300,buttontemplate,0.4)

    abigmess=Button(450,75,mess,0.4)
    bigmessans=Button(100,300,buttontemplate,0.4)
    incorrect1q5=Button(500,200,buttontemplate,0.4)
    incorrect2q5=Button(500,300,buttontemplate,0.4)
    incorrect3q5=Button(100,200,buttontemplate,0.4)

    reallife=Button(500,200,buttontemplate,0.4)
    incorrect1q6=Button(100,300,buttontemplate,0.4)
    incorrect2q6=Button(500,300,buttontemplate,0.4)
    incorrect3q6=Button(100,200,buttontemplate,0.4)

    notwebmaker=Button(500,200,buttontemplate,0.4)
    incorrect1q7=Button(100,300,buttontemplate,0.4)
    incorrect2q7=Button(500,300,buttontemplate,0.4)
    incorrect3q7=Button(100,200,buttontemplate,0.4)

    disableques1button=False
    disableques2button=True
    disableques3button=True
    disableques4button=True
    disableques5button=True
    disableques6button=True
    disableques7button=True

    def incorrect():
     
        print("wrong -1 life")
        #lives-=1
        youwrong.draw()


    while True:
        #put the events here!
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if showStartImage == True:
            screen.blit(placeholder_surface, (0,0))#put all graphics below this otherwise it will be overwritten!
            start_button.draw()
            whomadethiscrap.draw()
            screen.blit(text_surface, (220,370))
        if whomadethiscrap.isClicked():
            showStartImage=False
            screen.blit(quizquestion_surface,(0,0))
            start_button.draw()
            screen.blit(abouttext1,(150,100))
            screen.blit(abouttext2,(150,125))
            screen.blit(abouttext3,(150,150))
        
        if start_button.isClicked():
            pygame.display.set_caption('question 1')
            disableques1button=False

            screen.blit(quizquestion_surface, (0,0))
            screen.blit(question1, (210,100))
            ques1yes.draw()
            ques1no.draw()
        

            showStartImage=False

        if ques1no.isClicked() and disableques1button==False:#question 2
            disableques1button=True
            disableques2button=False
            screen.blit(quizquestion_surface, (0,0))
            pygame.display.set_caption('question 2')
            print("correct")
            screen.blit(question2, (210,100))
            
            brainrot.draw()
            
            
            incorrect1q2.draw()
            incorrect2q2.draw()
            incorrect3q2.draw()
            screen.blit(option1q2, (120,240))
            screen.blit(option2q2, (520,240))
            screen.blit(option3q2, (120,340))
        if brainrot.isClicked() and disableques2button ==False:#question 3
            disableques2button=True
            disableques3button=False
            screen.blit(quizquestion_surface, (0,0))
            pygame.display.set_caption('question 3')
            screen.blit(question3, (200,100))
            hotair.draw()
            print(disableques2button)
            incorrect1q3.draw()
            incorrect2q3.draw()
            incorrect3q3.draw()
            screen.blit(option1q3, (120,240))
            screen.blit(option2q3, (520,340))
            screen.blit(option3q3, (120,340))
            screen.blit(option4q3, (520,240))
        if hotair.isClicked() and disableques3button==False:#question 4
           
            disableques3button=True
            disableques4button=False
            screen.blit(quizquestion_surface, (0,0))
            pygame.display.set_caption('question 4')
            screen.blit(question4, (200,100))
            correctans.draw()
            incorrect1q4.draw()
            incorrect2q4.draw()
            incorrect3q4.draw()
            screen.blit(option1q4, (120,240))
            screen.blit(option2q4, (520,240))
            screen.blit(option3q4, (120,340))
            screen.blit(option4q4, (520,340))
        if correctans.isClicked() and disableques4button==False:#question5
            disableques4button=True
            disableques5button=False
            screen.blit(quizquestion_surface, (0,0))
            pygame.display.set_caption('question 5')
            screen.blit(question5,(190,100))
            abigmess.draw()
            bigmessans.draw()
            incorrect1q5.draw()
            incorrect2q5.draw()
            incorrect3q5.draw()
            screen.blit(option1q5, (120,240))
            screen.blit(option2q5, (520,240))
            screen.blit(option3q5, (120,340))
            screen.blit(option4q5, (520,340))
        if bigmessans.isClicked() and disableques5button==False :# question 6
            disableques5button=True
            disableques6button=False
            pygame.display.set_caption('question 5')
            screen.blit(quizquestion_surface, (0,0))
            screen.blit(question6,(200,100))
            reallife.draw()
            incorrect1q6.draw()
            incorrect2q6.draw()
            incorrect3q6.draw()
            screen.blit(option1q6, (520,240))
            screen.blit(option2q6, (120,240))
            screen.blit(option3q6, (120,340))
            screen.blit(option4q6, (520,340))
        if reallife.isClicked() and disableques6button==False:
            disableques6button==True
            disableques7button==False
            screen.blit(quizquestion_surface, (0,0))
            pygame.display.set_caption ("question 7")
            screen.blit(question7,(200,100))
            notwebmaker.draw()
            incorrect1q7.draw()
            incorrect2q7.draw()
            incorrect3q7.draw()
            screen.blit(option1q7, (120,340))
            screen.blit(option2q7, (120,240))
            screen.blit(option3q7, (520,240))
            screen.blit(option4q7, (520,340))
        if notwebmaker.isClicked() and disableques7button==False:
            disableques7button=True
            pygame.display.set_caption ("you win! (for now, more questions and puzzles coming soon)")
            screen.blit(quizquestion_surface, (0,0))
            screen.blit(victoryscreen,(0,0))

            

        
        if ques1yes.isClicked() and  disableques1button==False:
            
            incorrect()
        if (incorrect1q2.isClicked() or incorrect2q2.isClicked() or incorrect3q2.isClicked()) and disableques2button==False:
            
            incorrect()
        if (incorrect1q3.isClicked() or incorrect2q3.isClicked() or incorrect3q3.isClicked()) and disableques3button==False:
            
            incorrect()
        if (incorrect1q4.isClicked() or incorrect2q4.isClicked() or incorrect3q4.isClicked()) and disableques4button==False:
            
            incorrect()    
        if (incorrect1q5.isClicked() or incorrect2q5.isClicked() or incorrect3q5.isClicked()) and disableques5button==False:
            
            incorrect()    
        if (incorrect1q6.isClicked() or incorrect2q6.isClicked() or incorrect3q6.isClicked()) and disableques6button==False:
            
            incorrect()


        pygame.display.update()
        clock.tick(60)
#guigame1()#to do manual testing, remove the hash