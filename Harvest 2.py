think(0)
import json
from browser import window
from library import *
set_max_nb_steps(100000)
#help(UsedRobot)
#print(color_here())
### Possible Functions: ###
### Maze(), Center(), Harvest(), Token(), Around() ###
### turn(amt), goto(x,y), fill(x,y) ###
### Help() will bring up descriptions of functions ###
### Auto() will automaticly select correct Function ###
### CALL FUNCTIONS HERE ###
#Auto()
#bettermaze(showcolor, showpath, telemetry)
#Help()

'### EXPERIMENTAL METHODS BELOW ###'
### EXPERIMENTING WITH WINDY SOLVER ###
#windyV1()
def count_here():
    amt = 0
    while object_here():
        while carries_object():
            toss()
        take()
        amt += 1
    print(str(amt))
    while carries_object():
        put()
    move()
    while object_here():
        take()
    turn(2)
    move()
        
#goto(3,3)
#turn(2)
world_str = window.JSON.stringify(RUR.get_current_world().objects)
world_list = world_str.split('"')#[1::2]
print(world_list)
world_list.remove("{")
for a in range(0,len(world_list)):
    print(world_list[a])
char = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
num = ["1","2","3","4","5","6","7","8","9","0"]
print("SEPERATION")
list2 = []
for a in range(0,len(world_list)):
    search = True
    for b in range(0,len(char)):
        if (char[b] in world_list[a]) and (search == True):
            print(world_list[a])
            list2.append(world_list[a])
            search = False
        else:
            turn(0)
       
for a in range(2,len(list2),3):
    list2[a] = list2[a][1:-2]
print("-------------------------------------")
for a in range(0,len(list2),3):
    print(list2[a+1]+" x "+list2[a+2]+ " is at "+list2[a])

################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
def Auto():
    world_str = window.JSON.stringify(RUR.world_selector.get_selected().shortname);
    #print(world_str)

    if "giant randmaze" in world_str.lower():
        bettermaze()
    elif "randmaze" in world_str.lower():
        bettermaze()
    elif "maze2" in world_str.lower():
        bettermaze()
    elif "maze" in world_str.lower():
        Maze()
    elif "tokens" in world_str.lower():
        Token()
    elif "around" in world_str.lower():
        Around()
    elif "center" in world_str.lower():
        Center()
    elif "harvest 3" in world_str.lower():
        HarvestAndFill()
    elif "harvest" in world_str.lower():
        Harvest()
    else:
        print("Unknown World - Please Manualy Select a Function")
        print("Valid Functions are as follow:\n")
        Help()



def Help(selection = "General"):
    if selection == "General":
        print("Auto() - Automaticly selects function dependant on world")
        print("bettermaze() - To be used for any Maze world without rooms")
        print("Maze() - To be used for any Maze world - Depreciated")
        print("simpleMaze() - To be used for massive/complex mazes")
        print("Center() - To be used for any Center World")
        print("Token() - To be used for any Tokens World")
        print("Harvest() - To be used for Harvest 1 or 2")
        print("HarvestAndFill() - To be used for Harvest 3")
        print("Around() - To be used of any of the Around worlds")
        print("\n --- MAZE CAN TAKE VARYING AMOUNTS OF TIME TO LOAD ---")
        print(" --- IT DEPENDS ON THE COMPLEXITY OF THE MAZE ---")
    elif selection == Maze:
        print("Maze() was my first attempt at making a maze solving program\n")
        print("It involves the robot spinning around in circles to detect where walls are")
        print("and based on that, it chooses a direction to head in\n")
        print("It is an old program and is discoraged in use\n")
        print("The only benifit that it has over my new maze program is that it can solve mazes")
        print("where rooms are present")




def turn(amount=1):
    for x in range (0,amount):
        turn_left()
        

def FindCenter( ):
    Center = False
    Distance = 0
    while not Center:
        if not wall_in_front() :
            Distance += 1
            move()
        else :
            turn(2)
            for x in range (0 , Distance//2):
                move() 
            Center = True
            break

def Center():
    goto(1,1)
    turn(3)
    FindCenter()
    turn(3)
    FindCenter()
    put()
    done()
    
def wallSearch():
    wall = ""
    #set_trace_style("invisible")

    if wall_in_front():
        wall += "1"
    turn_left()
    if wall_in_front():
        wall += "2"
    turn_left()
    if wall_in_front():
        wall += "3"
    turn_left()
    if wall_in_front():
        wall += "4"
    turn_left()
    #set_trace_style("default")
    #print(wall)

def turnAndBuild():
    #set_trace_style("invisible")
    turn(2)
    build_wall()
    turn(2)
    #set_trace_style("default")

def turnAndMove(amt):
    #set_trace_style("invisible")
    turn(amt)
    #set_trace_style("default")
    move()
    

def wallfind():
    wall = ""
    #set_trace_style("invisible")
    if wall_in_front():
        wall += "1"
    turn_left()
    if wall_in_front():
        wall += "2"
    turn_left()
    if wall_in_front():
        wall += "3"
    turn_left()
    if wall_in_front():
        wall += "4"
    turn_left()
    #set_trace_style("default")
    
    if len(wall) == 4:
        print("FUCK")
        done()
    elif len(wall) == 3:
        #print("Code")
        
        if "1" not in wall:
            #print("more code")
            turnAndMove(0)
            turnAndBuild()
            
        elif "2" not in wall:
            turnAndMove(1)
            turnAndBuild()
            
        elif "3" not in wall:
            turnAndMove(2)
            turnAndBuild()
            #print("more code")
            
        elif "4" not in wall:
            turnAndMove(3)
            turnAndBuild()
            #print("more code")
            
            
    elif len(wall) == 2:
        if "1" not in wall:
            turnAndMove(0)
        elif "2" not in wall:
            turnAndMove(1)
        elif "4" not in wall:
            turnAndMove(3)
        elif "3" not in wall:
            turnAndMove(2)
    elif len(wall) == 1:
        if "1" not in wall:
            turnAndMove(0)
        elif "2" not in wall:
            turnAndMove(1)
        elif "4" not in wall:
            turnAndMove(3)
        elif "3" not in wall:
            turnAndMove(2)
    elif len(wall) == 0:
        move()
def Maze():
    wall = ""
    #turn(1)
    #build_wall()
    try:
        while not at_goal():
            wallfind()
    except:
        while not object_here():
            wallfind()
        take()

    print("Objective Found")
    done()
    
def Token():
    while not at_goal():
        try:
            take()
            x,y = position_here()
        except:
            move()
    #print(str(x))
    turn(2)
    Objective = False
    while not Objective:
        x2,y2 = position_here()
        if x2 == x+1:
            try:
                put()
            except:
                turn(2)
                while not at_goal():
                    move()
                done()
        else:
            move()

def Harvest():
    goto(1,1)
    turn(3)
    set_trace_style("default")
    y1 = 10
    xstart = 1
    ye = 1
    xe = 1
    findX = True
    findPos = True
    turn(1)
    amt = 0
    while not wall_in_front():
        findPos,findX,y1,xe,ye,amt,xstart = row(findPos,findX,y1,xe,ye,amt,xstart)
    turn(2)
    for x in range (0,amt):
        move()
    turn(1)
    move()
    while True:
        if not wall_in_front():
            findPos = True
            turn(1)
            amt = 0
            while not wall_in_front():
                findPos,findX,y1,xe,ye,amt,xstart = row(findPos,findX,y1,xe,ye,amt,xstart)
            turn(2)
            for x in range (0,amt):
                move()
            turn(1)
            move()
        else:
            findPos = True
            turn(1)
            amt = 0
            while not wall_in_front():
                findPos,findX,y1,xe,ye,amt,xstart = row(findPos,findX,y1,xe,ye,amt,xstart)
            turn(2)
            for x in range (0,amt):
                move()
            break

    goto(1,1)
    return(xstart,y1,xe,ye)

def HarvestAndFill():
    xs,ys,xe,ye = Harvest()
    goto(xs,ys)
    fill(xe,ye)

def goto(xt,yt):
    set_trace_style("invisible")
    pos = False
    while not pos:
        while not is_facing_north():
            turn(1)

        x,y = position_here()
        if x != xt:
            if x > xt:
                turn(1)
                move()
            elif x < xt:
                turn(3)
                move()
        elif y != yt:
            if y > yt:
                turn(2)
                move()
            elif y < yt:
                move()
        else:
            pos = True
    set_trace_style("default")


def fill(xtf,ytf):
    quad = 0
    x,y = position_here()
    if xtf > x:
        if ytf > y:
            quad = 1
        elif ytf < y:
            quad = 4
    elif xtf < x:
        if ytf > y:
            quad = 2
        elif ytf < y:
            quad = 3
    else:
        print("ERROR")
        done()
        
    xfront,yfront = position_in_front()
    xhere,yhere = position_here()
    TR = True
    
    while not is_facing_north():
        turn(1)
    while xhere != xtf:
        if TR:
            while yhere != ytf:
                xhere,yhere = position_here()
                put()
                move()
                
            repeat 2:
                turn(3)
                move()
            TR = False
        else:
            while yhere != y:
                xhere,yhere = position_here()
                put()
                move()
            repeat 2:
                turn(1)
                move()
            TR = True

def row(findPos, findX, y1, xe, ye, amt, xstart):
    if object_here():
        take()
        if findPos:
            x2,y2 = position_here()
            findPos = False
            if y2 < y1:
                y1 = y2
            if findX:
                xstart = x2
                findX = False
        xe1,ye1 = position_here()
        if xe1 > xe:
            xe = xe1
        if ye1 > ye:
            ye = ye1
    else:
        move()
        amt += 1
    return(findPos, findX, y1, xe, ye, amt, xstart)

def aroundComp():
    if color_here() == 'gravel':
        if not wall_in_front():
            if not wall_in_front() and not wall_on_right():
                turn(3)
                move()
            else:
                if object_here() != "token":
                    try:
                        take()
                        move()
                    except:
                        move()
        else:
            turn(1)
    else:
        print("Off the grass")
        done()
        
def Around():
    set_trace_style('thick')
    try:
        put()
    except:
        turn(0)
    if not wall_in_front():
        move()
    else:
        while wall_in_front():
            turn(1)
        move()
    try:
        take()
    except:
        turn(0)
    try:
        while not at_goal():
            aroundComp()
    except:
        while not object_here("token"):
            aroundComp()
        take()
    set_trace_style('default')
    
def simpleMaze():
    while not at_goal():
        if right_is_clear():
            repeat 3:
                turn_left()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()


### ---===--- BETTER MAZE ---===--- ###
    
def paintwhite():
    RUR.fill_background("white")
    
def revertpaint(b4w):
    for x in range(0,len(b4w),2):
        terms = b4w[x].split(',')
        if b4w[x+1] == "#000000":
            RUR.add_colored_tile('black',int(terms[0]),int(terms[1]))
        elif b4w[x+1] == 'white':
            RUR.add_colored_tile('white',int(terms[0]),int(terms[1]))
        else:
            RUR.add_background_tile(b4w[x+1],int(terms[0]),int(terms[1]))

def dir():
    dir = window.JSON.stringify(RUR.get_current_world().robots[0]._orientation)
    return(dir)

### BIG PROGRAM ###
### Block 1

def bettermaze(showcolor=False, showpath=False, telemetry=False):
    atEnd = False
    try:
        if at_goal():
            atEnd = True
    except:
        if object_here():
            atEnd = True
            
    if atEnd == True:
        done()
        
    beforeWhite = window.JSON.stringify(RUR.get_current_world().tiles)
    b4w = beforeWhite.split('"')[1::2]
    if telemetry == True:
        print(b4w)
    white = False

    for x in range(0,len(b4w),2):
        if b4w[x+1] == 'white':
            white == True

### BLOCK 2

    world_str = RUR.get_current_world();
    if telemetry == True:
        print(window.JSON.stringify(world_str.tiles))
    robot_str = window.JSON.stringify(world_str.robots)
    if telemetry == True:
        print(robot_str)
    targetstrx = ""
    targetstry = ""

    try:

        if at_goal():
            done()
        target = "goal"
        targetstr = world_str.goal.position
        targetstrx = window.JSON.stringify(targetstr.x)
        targetstry = window.JSON.stringify(targetstr.y)
        if telemetry == True:
            print(targetstrx + " " + targetstry)
    except:
        turn(0)
        target = "object"
        targetstr = window.JSON.stringify(world_str.objects)
        target_list = targetstr.split('"')[1::2]
        xy = target_list[0].split(',')
        targetstrx = xy[0]
        targetstry = xy[1]
        if telemetry == True:
            print(xy)
            print("X: " + targetstrx)
            print("Y: " + targetstry)
            print(targetstr)

    walls_str = window.JSON.stringify(world_str.walls)
    size_y_str = window.JSON.stringify(world_str.rows)
    size_x_str = window.JSON.stringify(world_str.cols)
    if telemetry == True:
        print(size_x_str + " " + size_y_str)
    size_x_str = size_x_str + ","
    size_y_str = "," + size_y_str
    if telemetry == True:
        print(walls_str)
    walls_list = walls_str.split('"')[1::2]
    robot_list = robot_str.split('{')[1::2]
    robot_list = robot_list[0].split(',')
    robot_list = (robot_list[0]+" "+robot_list[1]).split(':')
    robot_list = (robot_list[0]+robot_list[1]+robot_list[2]).split(' ')
    robot_list = (robot_list[0]+robot_list[1]).split('"')
    if telemetry == True:
        print(robot_list)
        print(robot_list[1] + " : " + robot_list[2])
        print(robot_list[3] + " : " + robot_list[4])
        print(walls_list)
    max1 = len(walls_list)
    if telemetry == True:
        print("PRINTING MAX 1")
        print(str(max1))
    x=0
    max2 = 0

    ### Block 3


    while True:
        try:
            for x in range(0,max1-max2):
                if not "," in walls_list[x+1]:
                    if not "," in walls_list[x+2]:
                        if telemetry == True:
                            print("Converting")
                        y = x+3
                        walls_list[x+1:y] = [','.join(walls_list[x+1:y])]
                        if telemetry == True:
                            print(walls_list[x+1:y-1])
            break;
        except:
            max2 += 1

    if telemetry == True:
        print(walls_list)
        print("\n\n\n\n")

    ### Block 4

    for a in range(1,int(size_x_str[:-1])+1):
        if telemetry == True:
            print("test")
        for b in range(1,int(size_y_str[1:])+1):
            if telemetry == True:
                print(str(a)+" "+str(b))
            original = str(a)+","+str(b)
            if not original in walls_list:
                walls_list.append(original)
                walls_list.append("")
            tempo = walls_list.index(original)

    if telemetry == True:
        for x in range(0,max1-max2+2,2):
            print(walls_list[x] + " : " + walls_list[x+1])

    for x in range(0,max1-max2+2,2):
        if walls_list[x+1] == "north":
            walls_list[x+1] = "1"
        elif walls_list[x+1] == "east":
            walls_list[x+1] = "2"
        else:
            walls_list[x+1] = "12"
    if telemetry == True:
        print(walls_list)

    for a in range(1,int(size_x_str[0:1])+1):
        wcstra = str(a)+","+str(1)
        if telemetry == True:
            print(wcstra)
        if not wcstra in walls_list:
            if telemetry == True:
                print(wcstra)
            walls_list.append(wcstra)
            walls_list.append("3")

    if telemetry == True:
        print(" ---- Doing x tops ---- ")
    for a in range(1,int(size_x_str[0:1])+1):
        wcstra = str(a)+","+size_y_str[1:2]
        if telemetry == True:
            print(wcstra)
        if not wcstra in walls_list:
            if telemetry == True:
                print(wcstra)
            walls_list.append(wcstra)
            walls_list.append("1")
    if telemetry == True:
        print(" ---- X tops stopped) ---- ")

    for a in range(1,int(size_y_str[1:2])+1):
        wcstra = str(1)+","+str(a)
        if telemetry == True:
            print(wcstra)
        if not wcstra in walls_list:
            if telemetry == True:
                print(wcstra)
            walls_list.append(wcstra)
            walls_list.append("4")

    for a in range(1,int(size_y_str[1:2])+1):
        wcstra = size_x_str[0:1]+","+str(a)
        if telemetry == True:
            print(wcstra)
        if not wcstra in walls_list:
            if telemetry == True:
                print(wcstra)
            walls_list.append(wcstra)
            walls_list.append("2")

    ### Block 5

    if telemetry == True:
        print(walls_list)
    max1 = len(walls_list)
    if telemetry == True:
        print(str(max2))
    max2 = 0
    while True:
        try:
            for x in range(0,max1-max2):
                if not "," in walls_list[x+1]:
                    if not "," in walls_list[x+2]:
                        if telemetry == True:
                            print("Converting")
                        y = x+3
                        walls_list[x+1:y] = [','.join(walls_list[x+1:y])]
                        if telemetry == True:
                            print(walls_list[x+1:y-1])
            break;
        except:
            max2 += 1
    if telemetry == True:
        print(str(max2))
    max1 = len(walls_list)
    if telemetry == True:
        print("Printing max 1")
        print(str(max1))

    for x in range(0,max1-max2+2,2):
        temp = walls_list[x].split(',')
        if telemetry == True:
            print(temp[0]+" "+temp[1])
        if size_x_str[:-1] == temp[0]:
            walls_list[x+1] += "2"
        if "1" == temp[0]:
            walls_list[x+1] += "4"
        if size_y_str[1:] == temp[1]:
            walls_list[x+1] += "1"
        if "1" == temp[1]:
            walls_list[x+1] += "3"

    for x in range(0,max1-max2+2,2):
        if telemetry == True:
            print(walls_list[x+1])
        walls_list[x+1] = "".join(set(walls_list[x+1]))
        if telemetry == True:
            print(walls_list[x+1])

    max1 = len(walls_list) 
    if telemetry == True:
        print(str(max1))
    max2 = 0

    ### Block 6

    if telemetry == True:
        print(" ---- FINAL PRINT ---- ")
    amt = 0

    if telemetry == True:
        for x in range(0,max1,2):
            print(walls_list[x] + " : " + walls_list[x+1])
            amt += 1
        print(str(amt))

    amt = 0

    if telemetry == True:
        print("TESTS")

        print(size_x_str[:-1]+" "+size_y_str[1:])

    for a in range(1,int(size_x_str[:-1])+1):
        if telemetry == True:
            print("test")
        for b in range(1,int(size_y_str[1:])+1):
            if telemetry == True:
                print("Tempo Original "+walls_list[tempo+1])
                print(str(a)+" "+str(b))
            original = str(a)+","+str(b)
            if not original in walls_list:
                walls_list.append(original)
                walls_list.append("")
            tempo = walls_list.index(original)
            if a == 1 and b == 1:
                turn(0)
            elif a == 1:
                amt += 1
                original = str(a)+","+str(b)

                ym1 = str(a)+","+str(b-1)
                if ym1 in walls_list:
                    if telemetry == True:
                        print("Test y: "+original)
                    tempy = walls_list.index(ym1)
                    if telemetry == True:
                        print("Tempy "+walls_list[tempy+1])
                    if "1" in walls_list[tempy+1]:
                        walls_list[tempo+1] += "3"
                #walls_list[tempo+1] = "".join(set(walls_list[tempo+1]))
            elif b == 1:
                amt += 1
                original = str(a)+","+str(b)

                xm1 = str(a-1)+","+str(b)
                if xm1 in walls_list:
                    if telemetry == True:
                        print("Test x: "+original)
                    tempx = walls_list.index(xm1)
                    if telemetry == True:
                        print("Tempx "+walls_list[tempx+1])
                    if "2" in walls_list[tempx+1]:
                        walls_list[tempo+1] += "4"
            elif not ((a == 1) or (b == 1)):
                amt += 1
                original = str(a)+","+str(b)

                xm1 = str(a-1)+","+str(b)
                ym1 = str(a)+","+str(b-1)
                if xm1 in walls_list:
                    if telemetry == True:
                        print("Test x: "+original)
                    tempx = walls_list.index(xm1)
                    if telemetry == True:
                        print("Tempx "+walls_list[tempx+1])
                    if "2" in walls_list[tempx+1]:
                        walls_list[tempo+1] += "4"
                if ym1 in walls_list:
                    if telemetry == True:
                        print("Test y: "+original)
                    tempy = walls_list.index(ym1)
                    if telemetry == True:
                        print("Tempy "+walls_list[tempy+1])
                    if "1" in walls_list[tempy+1]:
                        walls_list[tempo+1] += "3"
            walls_list[tempo+1] = "".join(set(walls_list[tempo+1]))
            if telemetry == True:
                print("Tempo Out "+walls_list[tempo+1])            

    if telemetry == True:
        print(str(amt))

    max1 = len(walls_list) 
    if telemetry == True:
        print(str(max1))
    max2 = 0

    ### Block 7

    if telemetry == True:
        print(" ---- FINAL PRINT (FOR REAL THIS TIME) ---- ")
    amt = 0

    if telemetry == True:
        for x in range(0,max1,2):
            print(walls_list[x] + " : " + walls_list[x+1])
            amt += 1
            if len(walls_list[x+1]) == 4:
                print(" ======= IMPORTANT ======= ")
        print(str(amt))

    done = []
    blue = []
    black = []
    red = []

    if (showpath == True) or (showcolor == True):
        paintwhite()

    xyti = walls_list.index(targetstrx+","+targetstry)
    if telemetry == True:
        print(" NOT THAT IMPORTANT\n"+str(xyti)+" "+walls_list[xyti])

        if (showpath == True) or (showcolor == True):
            pause()

    ### Block 8

    for a in range(0,max1,2):
        temp = walls_list[a].split(',')
        if telemetry == True:
            print(temp[0] + " " + temp[1])
        x=int(temp[0])
        y=int(temp[1])
        if not (str(x)+","+str(y)) == (robot_list[2]+","+robot_list[4]):
            if not (str(x)+","+str(y)) == (targetstrx+","+targetstry):
                if not walls_list[a] in done:
                    if len(walls_list[a+1]) == 3:
                        if showcolor == True:
                            RUR.add_colored_tile('red',x,y)
                        red.append(str(x)+","+str(y))
                        Test = True

                        while Test == True:
                            Test = False
                            if not (str(x)+","+str(y)) == (robot_list[2]+","+robot_list[4]):
                                if not (str(x)+","+str(y)) == (targetstrx+","+targetstry):
                                    temp3 = walls_list.index(str(x)+","+str(y))
                                    if "1" not in walls_list[temp3+1]:
                                        walls_list[temp3+1] += "1"
                                        temp2 = walls_list.index(str(x)+","+str(y+1))
                                        if not (str(x)+","+str(y+1)) == (robot_list[2]+","+robot_list[4]):
                                            if not (str(x)+","+str(y+1)) == (targetstrx+","+targetstry):
                                                if len(walls_list[temp2+1]) == 2:
                                                    walls_list[temp2+1] += "3"
                                                    if showcolor == True:
                                                        RUR.add_colored_tile('black',x,y)
                                                    black.append(str(x)+","+str(y))
                                                    y += 1
                                                    if showcolor == True:
                                                        RUR.add_colored_tile('blue',x,y)
                                                    blue.append(str(x)+","+str(y))
                                                    done.append(walls_list[temp3])
                                                    Test = True
                                                else:
                                                    walls_list[temp2+1] += "3"
                                    if "2" not in walls_list[temp3+1]:
                                        temp2 = walls_list.index(str(x+1)+","+str(y))
                                        walls_list[temp3+1] += "2"
                                        if not (str(x+1)+","+str(y)) == (robot_list[2]+","+robot_list[4]):
                                            if not (str(x+1)+","+str(y)) == (targetstrx+","+targetstry):
                                                if len(walls_list[temp2+1]) == 2:
                                                    walls_list[temp2+1] += "4"
                                                    if showcolor == True:
                                                        RUR.add_colored_tile('black',x,y)
                                                    black.append(str(x)+","+str(y))
                                                    x += 1
                                                    if showcolor == True:
                                                        RUR.add_colored_tile('blue',x,y)
                                                    blue.append(str(x)+","+str(y))
                                                    done.append(walls_list[temp3])
                                                    Test = True
                                                else:
                                                    walls_list[temp2+1] += "4"
                                    if "3" not in walls_list[temp3+1]:
                                        walls_list[temp3+1] += "3"
                                        temp2 = walls_list.index(str(x)+","+str(y-1))
                                        if not (str(x)+","+str(y-1)) == (robot_list[2]+","+robot_list[4]):
                                            if not (str(x)+","+str(y-1)) == (targetstrx+","+targetstry):
                                                if len(walls_list[temp2+1]) == 2:
                                                    walls_list[temp2+1] += "1"
                                                    if showcolor == True:
                                                        RUR.add_colored_tile('black',x,y)
                                                    black.append(str(x)+","+str(y))
                                                    y -= 1
                                                    if showcolor == True:
                                                        RUR.add_colored_tile('blue',x,y)
                                                    red.append(str(x)+","+str(y))
                                                    done.append(walls_list[temp3])
                                                    Test = True
                                                else:
                                                    walls_list[temp2+1] += "1"
                                    if "4" not in walls_list[temp3+1]:
                                        walls_list[temp3+1] += "4"
                                        temp2 = walls_list.index(str(x-1)+","+str(y))
                                        if not (str(x-1)+","+str(y)) == (robot_list[2]+","+robot_list[4]):
                                            if not (str(x-1)+","+str(y)) == (targetstrx+","+targetstry):
                                                if len(walls_list[temp2+1]) == 2:
                                                    walls_list[temp2+1] += "2"
                                                    if showcolor == True:
                                                        RUR.add_colored_tile('black',x,y)
                                                    black.append(str(x)+","+str(y))
                                                    x -= 1
                                                    if showcolor == True:
                                                        RUR.add_colored_tile('blue',x,y)
                                                    red.append(str(x)+","+str(y))
                                                    done.append(walls_list[temp3])
                                                    Test = True
                                                else:
                                                    walls_list[temp2+1] += "2"

    ### Block 9

    goalPath = []

    for a in range(1,int(size_x_str[:-1])+1):
        for b in range(1,int(size_y_str[1:])+1):
            if not (str(a)+","+str(b)) in black:
                if not (str(a)+","+str(b)) in blue:
                    if not (str(a)+","+str(b)) in red:
                        goalPath.append(str(a)+","+str(b))
                        if showpath == True:
                            RUR.add_colored_tile('green',a,b)
    if telemetry == True:
        print(goalPath)
    if (showpath == True) or (showcolor == True) or (telemetry == True):
        pause()
    set_trace_style("thick")

    try:
        while not at_goal():
            x2,y2 = position_here()
            try:
                goalPath.remove(str(x2)+","+str(y2))
            except:
                turn(0)


            if at_goal():
                break;
            else:
                if not position_in_front() == {}:
                    if front_is_clear():
                        x,y = position_in_front()
                        if (str(x)+","+str(y)) in goalPath:
                            move()
                        else:
                            turn(1)
                    else:
                        turn(1)
                else: turn(1)
    except:
        while not object_here():
            x2,y2 = position_here()
            try:
                goalPath.remove(str(x2)+","+str(y2))
            except:
                turn(0)


            if object_here():
                break;
            else:
                if not position_in_front() == {}:
                    if front_is_clear():
                        x,y = position_in_front()
                        if (str(x)+","+str(y)) in goalPath:
                            move()
                        else:
                            turn(1)
                    else:
                        turn(1)
                else: turn(1)

    ### Block 10

    turn(4)
    set_trace_style("default")
    if (showpath == True) or (showcolor == True):
        if white == True:
            paintwhite()
        else:
            revertpaint(b4w)
            
def windyV1():
    area = []
    put()
    move()


    while not object_here("star"):

        while object_here():
            take()

        xh,yh = position_here()
        area.append(str(xh)+","+str(yh))

        if wall_in_front():
            turn(1)
        elif right_is_clear():
            turn(3)
            x,y = position_in_front()
            tile = str(RUR.get_background_tile(x,y)).lower()
            #print(tile)
            if tile == "none":
                xh,yh = position_here()
                area.append(str(xh)+","+str(yh))
                move()
            else:
                build_wall()
        else:
            move()
    take()

    #print(area)

    turn()
    move()

    turn(2)
    x,y = position_in_front()
    area.append(str(x)+","+str(y))
    turn(3)

    '''
    for a in range(1,RUR.MAX_X+1):
        for b in range(1,RUR.MAX_Y+1):
            if (str(a)+","+str(b)) in area:
                RUR.add_colored_tile("red",a,b)
    '''
    amt = 0
    repeat 20:
        x,y = position_in_front()
        while object_here():
            take()

        xh,yh = position_here()
        try:
            area.append(str(xh)+","+str(yh))
        except:
            turn(0)

        x,y = position_in_front()
        if str(x)+","+str(y) in area:
            turn(3)
            amt += 1
            if amt == 4:
                done()
        else:
            move()
            amt = 0