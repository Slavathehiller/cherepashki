import random, turtle, sys

window = turtle.Screen()
window.title("Черепашьи бега")
window.bgcolor('grey')


def poka():
    sys.exit()


border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.up()
border.pensize(3)
border.color('red')
border.goto(400, 300)
border.down()
border.fillcolor('green')
border.begin_fill()
border.goto(400, -300)
border.goto(-300, -300)
border.goto(-300, 300)
border.goto(400, 300)
border.end_fill()

writer = turtle.Turtle()
writer.hideturtle()

columnx = -380
columny = 370

writer.up()
writer.goto(columnx, columny)
writer.down()
writer.write("Лидер", align="right", font=("Arial", 11, "normal"))

writer.up()
writer.goto(columnx, columny - 50)
writer.down()
writer.write("Аутсайдер", align="right", font=("Arial", 11, "normal"))

writer.up()
writer.goto(columnx + 300, -330)
writer.down()
writer.write("Пробел - повторить гонку", align="right", font=("Arial", 11, "normal"))

writer.up()
writer.goto(columnx + 500, -330)
writer.down()
writer.write("Enter - начать новую гонку", align="right", font=("Arial", 11, "normal"))

writer.up()
writer.goto(columnx + 700, -330)
writer.down()
writer.write("Escape - закончить игру", align="right", font=("Arial", 11, "normal"))

leaderwriter = turtle.Turtle()
leaderwriter.hideturtle()
leaderwriter.up()
leaderwriter.goto(columnx + 30, columny)
leaderwriter.down()
outsiderwriter = turtle.Turtle()
outsiderwriter.hideturtle()
outsiderwriter.up()
outsiderwriter.goto(columnx + 30, columny - 50)
outsiderwriter.down()

scorewriter = turtle.Turtle()
scorewriter.hideturtle()
namewriter = turtle.Turtle()
namewriter.hideturtle()

turtlenum = 2
turtleList = list()

def standby():
    y = -300
    scorewriter.clear()
    for i in range(turtlenum):
        turtleList[i].hideturtle()
    for i in range(turtlenum):
        turtlerun = turtleList[i]
        x = -250
        y = y + 50
        turtlerun.goto(-250, y)
        turtlerun.showturtle()
        turtlerun.iRun = True


def seed():
    scorewriter.clear()
    for turtly in turtleList:
        turtly.hideturtle()
    global turtlenum
    turtlenum = int(window.numinput("Количество игроков", "Введите количество черепашек:", 2, minval=2, maxval=6))
    y = -300
    namewriter.clear()
    for i in range(turtlenum):
        x = -250
        y = y + 50
        turtlerun = turtle.Turtle()
        turtlerun.hideturtle()
        turtlerun.up()
        turtlerun.shape("turtle")
        turtlerun.speed(3)
        turtlerun.iRun = True
        turtleList.append(turtlerun)
        turtlerun.name = window.textinput("Имена игроков", "Введите имя " + str(i + 1) + " черепашки:")
        namewriter.up()
        namewriter.goto(x - 60, y - 10)
        namewriter.down()
        namewriter.write(turtlerun.name, align="right", font=("Arial", 12, "normal"))
    standby()


def letsride():
    standby()
    scoreList = list()
    finishLine = 380
    AnyRun = True
    positions = list(range(turtlenum))
    leader = turtle.Turtle()
    leader.hideturtle()
    outsider = turtle.Turtle()
    outsider.hideturtle()

    while AnyRun:
        AnyRun = False
        for i in range(turtlenum):
            turtlerun = turtleList[i]
            x, y = turtlerun.position()
            if x < finishLine:
                x = x + random.randint(1, 20)
                x = min(x, finishLine)
                turtlerun.setposition(x, y)
                positions[i] = x
            else:
                turtlerun.iRun = False
                if scoreList.count(i) == 0:
                    scoreList.append(i)
            AnyRun = AnyRun or turtlerun.iRun
            if leader != turtleList[positions.index(max(positions))]:
                leader = turtleList[positions.index(max(positions))]
                leaderwriter.clear()
                leaderwriter.write(leader.name)
            if outsider != turtleList[positions.index(min(positions))]:
                outsider = turtleList[positions.index(min(positions))]
                outsiderwriter.clear()
                outsiderwriter.write(outsider.name)

    leaderwriter.clear()
    leaderwriter.write(turtleList[scoreList[0]].name)
    outsiderwriter.clear()
    outsiderwriter.write(turtleList[scoreList[turtlenum - 1]].name)

    for i in range(turtlenum):
        x, y = turtleList[scoreList[i]].position()
        scorewriter.up()
        scorewriter.goto(x + 40, y - 15)
        scorewriter.down()
        scorewriter.write(str(i + 1), font=("Arial", 16, "normal"))

def reRun():
    seed()
    letsride()
    window.listen()

reRun()
window.onkey(letsride, "space")
window.onkey(reRun, "Return")
window.onkey(poka, "Escape")
window.listen()





window.mainloop()





