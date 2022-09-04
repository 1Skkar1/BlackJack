import random
import pygame
import math
import time

# Suits:
# H -> Hearts
# D -> Diamonds
# C -> Clubs
# S -> Spades

# -----------------+
# -> C L A S S E S :
# -----------------+


class Card:
    def __init__(self):
        self.deck = []

        for x in range(1,14):
            card = x
            for y in range(4):
                if y == 0:
                    suit = 'H'
                elif y == 1:
                    suit = 'D'
                elif y == 2:
                    suit = 'C'
                elif y == 3:
                    suit = 'S'
                self.deck.append([card,suit])

        self.deck = self.deck * 4

    def getDeck(self):
        return self.deck


class Dealer:
    def __init__(self, c):
        self.curValue = 0
        self.deck = c
        self.cards = []

    def deal(self):
        rand = random.randint(0, len(self.deck) - 1)
        randCard = self.deck[rand]
        self.deck.pop(rand)
        self.cards.append(randCard)

        rand = random.randint(0, len(self.deck) - 1)
        randCard = self.deck[rand]
        self.deck.pop(rand)
        self.cards.append(randCard)

        self.mkMove()
        return self.cards

    def mkMove(self):
        value = 0
        if self.cards[0][0] == 1 and self.cards[1][0] == 1:
            value = 2
        else:
            if self.cards[0][0] == 11 or self.cards[0][0] == 12 or self.cards[0][0] == 13:
                value += 10
            else:
                value += self.cards[0][0]

            if self.cards[1][0] == 11 or self.cards[1][0] == 12 or self.cards[1][0] == 13:
                value += 10
            else:
                value += self.cards[1][0]

        self.curValue = value

        if value == 11 and (self.cards[0][0] == 1 or self.cards[1][0] == 1):
            self.curValue = 21
            return self.curValue
        elif value < 17:
            self.hit()
        else:
            return self.curValue

    def hit(self):
        value = 0
        rand = random.randint(1, len(self.deck))
        card = self.deck[rand]
        self.deck.pop(rand)
        self.cards.append(card)

        if card[0] == 11 or card[0] == 12 or card[0] == 13:
            value = 10
        elif card[0] == 1 and self.curValue == 10:
            value = 11
        elif card[0] == 1 and self.curValue < 11:
            value = 11
        elif card[0] == 1 and self.curValue == 20:
            value = 1
        else:
            value = card[0]

        self.curValue += value
        if self.curValue < 19:
            self.hit()
        else:
            return self.curValue

    def getScore(self):
        return self.curValue

    def reset(self):
        self.cards = []
        self.curValue = 0


class Player:
    def __init__(self, c):
        self.curValue = 0
        self.deck = c
        self.cards = []

    def deal(self):
        rand = random.randint(0, len(self.deck) - 1)
        randCard = self.deck[rand]
        self.deck.pop(rand)
        self.cards.append(randCard)

        rand = random.randint(0, len(self.deck) - 1)
        randCard = self.deck[rand]
        self.deck.pop(rand)
        self.cards.append(randCard)

        value = 0
        if self.cards[0][0] == 11 or self.cards[0][0] == 12 or self.cards[0][0] == 13:
            value += 10
        else:
            value += self.cards[0][0]

        if self.cards[1][0] == 11 or self.cards[1][0] == 12 or self.cards[1][0] == 13:
            value += 10
        else:
            value += self.cards[1][0]

        self.curValue = value

        if value == 11 and (self.cards[0][0] == 1 or self.cards[1][0] == 1):
            self.curValue = 21

        return self.cards

    def hit(self):
        value = 0
        rand = random.randint(1, len(self.deck))
        card = self.deck[rand]
        self.deck.pop(rand)
        self.cards.append(card)

        if card[0] == 11 or card[0] == 12 or card[0] == 13:
            value = 10
        elif card[0] == 1 and self.curValue == 10:
            value = 11
        elif card[0] == 1 and self.curValue < 11:
            value = 11
        elif card[0] == 1 and self.curValue == 20:
            value = 1
        else:
            value = card[0]

        self.curValue += value
        if self.curValue > 21 and self.cards.__contains__(1):
            if self.cards.count(1) == 1:
                if self.curValue - 10 < 22:
                    self.curValue = self.curValue - 10

        return card

    def getScore(self):
        return self.curValue


# -----------------+
# -> M A I N :
# -----------------+

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)

width = 1200
height = 700

background = pygame.image.load('assets/background.jpg')
cardBack = pygame.image.load('assets/cardBack.png')
mainLogo = pygame.image.load('assets/mainLogo.png')
icon = pygame.image.load('assets/icon.png')
cardImg = [None]

# 2
two_clubs = pygame.image.load('assets/2_of_clubs.png')
two_diamonds = pygame.image.load('assets/2_of_diamonds.png')
two_hearts = pygame.image.load('assets/2_of_hearts.png')
two_spades = pygame.image.load('assets/2_of_spades.png')
# 3
three_clubs = pygame.image.load('assets/3_of_clubs.png')
three_diamonds = pygame.image.load('assets/3_of_diamonds.png')
three_hearts = pygame.image.load('assets/3_of_hearts.png')
three_spades = pygame.image.load('assets/3_of_spades.png')
# 4
four_clubs = pygame.image.load('assets/4_of_clubs.png')
four_diamonds = pygame.image.load('assets/4_of_diamonds.png')
four_hearts = pygame.image.load('assets/4_of_hearts.png')
four_spades = pygame.image.load('assets/4_of_spades.png')
# 5
five_clubs = pygame.image.load('assets/5_of_clubs.png')
five_diamonds = pygame.image.load('assets/5_of_diamonds.png')
five_hearts = pygame.image.load('assets/5_of_hearts.png')
five_spades = pygame.image.load('assets/5_of_spades.png')
# 6
six_clubs = pygame.image.load('assets/6_of_clubs.png')
six_diamonds = pygame.image.load('assets/6_of_diamonds.png')
six_hearts = pygame.image.load('assets/6_of_hearts.png')
six_spades = pygame.image.load('assets/6_of_spades.png')
# 7
seven_clubs = pygame.image.load('assets/7_of_clubs.png')
seven_diamonds = pygame.image.load('assets/7_of_diamonds.png')
seven_hearts = pygame.image.load('assets/7_of_hearts.png')
seven_spades = pygame.image.load('assets/7_of_spades.png')
# 8
eight_clubs = pygame.image.load('assets/8_of_clubs.png')
eight_diamonds = pygame.image.load('assets/8_of_diamonds.png')
eight_hearts = pygame.image.load('assets/8_of_hearts.png')
eight_spades = pygame.image.load('assets/8_of_spades.png')
# 9
nine_clubs = pygame.image.load('assets/9_of_clubs.png')
nine_diamonds = pygame.image.load('assets/9_of_diamonds.png')
nine_hearts = pygame.image.load('assets/9_of_hearts.png')
nine_spades = pygame.image.load('assets/9_of_spades.png')
# 10
ten_clubs = pygame.image.load('assets/10_of_clubs.png')
ten_diamonds = pygame.image.load('assets/10_of_diamonds.png')
ten_hearts = pygame.image.load('assets/10_of_hearts.png')
ten_spades = pygame.image.load('assets/10_of_spades.png')
# J
jack_clubs = pygame.image.load('assets/jack_of_clubs.png')
jack_diamonds = pygame.image.load('assets/jack_of_diamonds.png')
jack_hearts = pygame.image.load('assets/jack_of_hearts.png')
jack_spades = pygame.image.load('assets/jack_of_spades.png')
# Q
queen_clubs = pygame.image.load('assets/queen_of_clubs.png')
queen_diamonds = pygame.image.load('assets/queen_of_diamonds.png')
queen_hearts = pygame.image.load('assets/queen_of_hearts.png')
queen_spades = pygame.image.load('assets/queen_of_spades.png')
# K
king_clubs = pygame.image.load('assets/king_of_clubs.png')
king_diamonds = pygame.image.load('assets/king_of_diamonds.png')
king_hearts = pygame.image.load('assets/king_of_hearts.png')
king_spades = pygame.image.load('assets/king_of_spades.png')
# A
ace_clubs = pygame.image.load('assets/ace_of_clubs.png')
ace_diamonds = pygame.image.load('assets/ace_of_diamonds.png')
ace_hearts = pygame.image.load('assets/ace_of_hearts.png')
ace_spades = pygame.image.load('assets/ace_of_spades.png')

cardImg.append([ace_clubs, ace_diamonds, ace_hearts, ace_spades])
cardImg.append([two_clubs, two_diamonds, two_hearts, two_spades])
cardImg.append([three_clubs, three_diamonds, three_hearts, three_spades])
cardImg.append([four_clubs, four_diamonds, four_hearts, four_spades])
cardImg.append([five_clubs, five_diamonds, five_hearts, five_spades])
cardImg.append([six_clubs, six_diamonds, six_hearts, six_spades])
cardImg.append([seven_clubs, seven_diamonds, seven_hearts, seven_spades])
cardImg.append([eight_clubs, eight_diamonds, eight_hearts, eight_spades])
cardImg.append([nine_clubs, nine_diamonds, nine_hearts, nine_spades])
cardImg.append([ten_clubs, ten_diamonds, ten_hearts, ten_spades])
cardImg.append([jack_clubs, jack_diamonds, jack_hearts, jack_spades])
cardImg.append([queen_clubs, queen_diamonds, queen_hearts, queen_spades])
cardImg.append([king_clubs, king_diamonds, king_hearts, king_spades])

pygame.init()
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Black Jack Game")
pygame.display.set_icon(icon)
mainFont = pygame.font.SysFont('consolas', 20)
endFont = pygame.font.SysFont('yanmartext', 55)
clock = pygame.time.Clock()
screen.fill(WHITE)
pygame.display.flip()

c = Card()
deck = c.getDeck()
d = Dealer(deck)
p = Player(deck)
onTable = []
topCards = []


def cardImage(n, suit):
    if suit == 'C':
        return cardImg[n][0]
    elif suit == 'D':
        return cardImg[n][1]
    elif suit == 'H':
        return cardImg[n][2]
    elif suit == 'S':
        return cardImg[n][3]


def reset():
    global onTable, cardImg, topCards

    onTable = []
    topCards = []
    time.sleep(1)


def restart():
    screen.fill(GREEN)
    pygame.display.update()
    pygame.init()

    while True:
        clock.tick(200)
        # PLAYER
        dealPlayer(625, 480)
        dealPlayer(450, 480)
        # DEALER
        dealPlayer(625, 50)
        dealPlayer(450, 50)
        main()


def firstStart():
    reset()
    screen.fill(WHITE)
    label = mainFont.render('PRESS ANY BUTTON TO START', 1, BLACK)
    screen.blit(mainLogo, (350, 20))
    screen.blit(label, (465, 650))
    pygame.display.update()
    pygame.init()

    while True:
        clock.tick(200)
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            pygame.quit()
        if ev.type == pygame.KEYDOWN or ev.type == pygame.MOUSEBUTTONDOWN:
            dealPlayer(625, 480)
            dealPlayer(450, 480)
            dealPlayer(625, 50)
            dealPlayer(450, 50)
            main()


def drawCard(img, x, y):
    w = 130
    h = 181
    pygame.draw.rect(screen, WHITE, (x - 5, y - 4, w + 10, h + 8), 0)
    newCard = pygame.transform.scale(img, (w,h))
    screen.blit(newCard, (x,y))


def dealPlayer(x,y):
    posX = x
    posY = y
    moveX = 0
    moveY = 0
    h = math.sqrt(posX**2 + posY**2)

    for i in range(int(round(h / 10))):
        screen.fill(GREEN)
        moveX += posX / (h / 10)
        moveY += posY / (h / 10)
        drawCard(cardBack, moveX, moveY)
        for d in range(len(onTable)):
            drawCard(onTable[d][0], onTable[d][1], onTable[d][2])

        clock.tick(120)
        drawCard(cardBack, 15, 15)
        pygame.display.update()

    onTable.append([cardBack, x, y])


def dealPlayerHit(hit, x , y):
    posX = x
    posY = y
    moveX = 0
    moveY = 0
    h = math.sqrt(posX**2 + posY**2)

    for i in range(int(round(h / 10))):
        screen.fill(GREEN)
        moveX += posX / (h / 10)
        moveY += posY / (h / 10)
        drawCard(cardBack, moveX, moveY)
        for d in range(len(onTable)):
            drawCard(onTable[d][0], onTable[d][1], onTable[d][2])

        clock.tick(120)
        drawCard(cardBack, 15, 15)
        pygame.display.update()

    onTable.append([hit, x, y])


def updateScore(turn=False):
    dScore = d.getScore()
    pScore = p.getScore()
    score1 = mainFont.render(str(dScore), 1, WHITE)
    score2 = mainFont.render(str(pScore), 1, WHITE)
    screen.blit(score2, (1150,500))
    if turn:
        screen.blit(score1, (1150,50))


def main():
    global d, p

    c = Card()
    deck = c.getDeck()
    d = Dealer(deck)
    p = Player(deck)
    dealerCards = d.deal()
    playerCards = p.deal()
    allowHit = False
    playerReveal = False
    playerTurn = True
    playerStay = False
    onTable[2] = [cardImage(dealerCards[0][0], dealerCards[0][1]), 625, 50]
    onTable[3] = [cardBack, 450, 50]

    while True:
        pygame.display.update()
        clock.tick(120)

        # -> PLAYER
        if not playerReveal:
            drawCard(cardBack, 625, 480)
            drawCard(cardBack, 450, 480)
            label = mainFont.render('Press space to reveal your cards', 1, WHITE)
            screen.blit(label, (430,350))
            ev = pygame.event.poll()

            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    playerReveal = True
                    allowHit = True
                    drawCard(cardImage(playerCards[0][0], playerCards[0][1]), 625, 480)
                    drawCard(cardImage(playerCards[1][0], playerCards[1][1]), 450, 480)
                    onTable[0] = [cardImage(playerCards[0][0], playerCards[0][1]), 625, 480]
                    onTable[1] = [cardImage(playerCards[1][0], playerCards[1][1]), 450, 480]
                    pygame.draw.rect(screen, GREEN, (429, 299, 500, 100))
            pygame.display.update()

        else:
            label = mainFont.render('Press space to hit or tab to stay', 1, WHITE)
            screen.blit(label, (430, 350))
            updateScore()
            pygame.display.update()
            ev = pygame.event.poll()

            if ev.type == pygame.QUIT:
                pygame.quit()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_SPACE:
                    if allowHit:
                        hitCard = p.hit()
                        if len(p.cards) == 3:
                            dealPlayerHit(cardImage(hitCard[0], hitCard[1]), 275, 480)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 275, 480)
                            updateScore()
                        elif len(p.cards) == 4:
                            dealPlayerHit(cardImage(hitCard[0], hitCard[1]), 800, 480)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 800, 480)
                            updateScore()
                        elif len(p.cards) == 5:
                            dealPlayerHit(cardImage(hitCard[0], hitCard[1]), 100, 480)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 100, 480)
                            updateScore()
                        elif len(p.cards) == 6:
                            dealPlayerHit(cardImage(hitCard[0], hitCard[1]), 975, 480)
                            drawCard(cardImage(hitCard[0], hitCard[1]), 975, 480)
                            updateScore()
                    allowHit = True
                    pygame.display.update()

                if ev.key == pygame.K_TAB:
                    playerStay = True
                    updateScore(True)

                if ev.key == pygame.K_ESCAPE:
                    pygame.quit()

            if p.getScore() > 21:
                label = endFont.render('BUST', 1, WHITE)
                screen.blit(label, (510, 330))
                allowHit = False
                pygame.display.update()
                break

            elif p.getScore() == 21 and len(p.cards) == 2:
                allowHit = False
                label = endFont.render('BLACK JACK', 1, WHITE)
                pygame.draw.rect(screen, GREEN, (429, 299, 500, 100))
                screen.blit(label, (510, 330))
                pygame.display.update()
                time.sleep(1)
                break

            elif playerStay:
                playerTurn = False
                allowHit = False
                updateScore()
                pygame.display.update()

        # -> DEALER
        if not playerTurn:
            drawCard(cardImage(dealerCards[1][0], dealerCards[1][1]), 450, 50)
            try:
                idx = onTable.index([cardBack, 450, 50])
                onTable[idx] = [cardImage(dealerCards[1][0], dealerCards[1][1]), 450, 50]
            except:
                pass

            updateScore()
            if len(d.cards) > 2:
                dealPlayerHit(cardImage(dealerCards[2][0], dealerCards[2][1]), 275, 50)
                drawCard(cardImage(dealerCards[2][0], dealerCards[2][1]), 275, 50)
                pygame.display.update()
                time.sleep(0.5)
            elif len(d.cards) > 3:
                dealPlayerHit(cardImage(dealerCards[3][0], dealerCards[3][1]), 800, 50)
                drawCard(cardImage(dealerCards[3][0], dealerCards[3][1]), 800, 50)
                pygame.display.update()
                time.sleep(0.5)
            elif len(d.cards) > 4:
                dealPlayerHit(cardImage(dealerCards[4][0], dealerCards[4][1]), 100, 50)
                drawCard(cardImage(dealerCards[4][0], dealerCards[4][1]), 100, 50)
                pygame.display.update()
                time.sleep(0.5)
            elif len(d.cards) > 5:
                dealPlayerHit(cardImage(dealerCards[5][0], dealerCards[5][1]), 975, 50)
                drawCard(cardImage(dealerCards[5][0], dealerCards[5][1]), 975, 50)
                pygame.display.update()
                time.sleep(0.5)
            updateScore(True)

            if d.getScore() > p.getScore():
                if d.getScore() < 22:
                    label = endFont.render('YOU LOST', 1, WHITE)
                    pygame.draw.rect(screen, GREEN, (429, 299, 500, 100))
                    screen.blit(label, (510, 330))
                    pygame.display.update()
                    break
                else:
                    label = endFont.render('YOU WON', 1, WHITE)
                    label2 = mainFont.render('dealer bust', 1, WHITE)
                    pygame.draw.rect(screen, GREEN, (429, 299, 500, 100))
                    screen.blit(label, (510, 330))
                    screen.blit(label2, (540, 375))
                    pygame.display.update()
                    break

            elif d.getScore() < p.getScore():
                label = endFont.render('YOU WON', 1, WHITE)
                pygame.draw.rect(screen, GREEN, (429, 299, 500, 100))
                screen.blit(label, (510, 330))
                pygame.display.update()
                break
            else:
                label = endFont.render('TIE', 1, WHITE)
                pygame.draw.rect(screen, GREEN, (429, 299, 500, 100))
                screen.blit(label, (530, 330))
                pygame.display.update()
                break

        else:
            drawCard(cardImage(dealerCards[0][0], dealerCards[0][1]), 625, 50)
            drawCard(cardBack, 450, 50)

    time.sleep(1.5)
    reset()
    restart()


firstStart()