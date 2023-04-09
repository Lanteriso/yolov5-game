import time
import pydirectinput
import random
import torch

class Game:
    def __init__(self,name):
        self.name = name
        self.pathroom = ['door_up','door_right','door_up','door_up','door_right','door_boss']

        self.allmap_data = {'格兰迪':[['door_right', 'door_right', 'door_down', 'None', 'None', 'None'],
                        ['None', 'door_right', 'door_down', 'end', 'None', 'None'],
                        ['None', 'door_right', 'door_right', 'door_up', 'None', 'None'],
                        ['None', 'None', 'None', 'None', 'None', 'None'],
                        ['None', 'None', 'None', 'None', 'None', 'None'],
                        ['None', 'None', 'None', 'None', 'None', 'None']],
                        '海博伦':[['door_right', 'door_right', 'door_right', 'end', 'None', 'None'],
                         ['door_right', 'door_up', 'door_up', 'None', 'None', 'None'] ,
                         ['door_right', 'door_up', 'door_up', 'None', 'None', 'None'],
                         ['door_up', 'None', 'None', 'None', 'None', 'None']],
                        '时间广场': [['door_right', 'door_right', 'door_right', 'door_down', 'None', 'None'],
                           ['None', 'door_right', 'door_right', 'door_down', 'door_left', 'None'],
                           ['None', 'door_right', 'door_right', 'door_right', 'door_right', 'end'],
                           ['None', 'None', 'None', 'None', 'None', 'None']]
                            }
        self.map_data = self.allmap_data['格兰迪']
        self.roomindex = -1
        self.numberofdungeons = 0
        self.SeeChallengeAgain = True
        self.cannextroom = True
        self.fangdairoom = 0
        self.fangdailast= []
        self.lastinputtime = 0
        self.heroskilllist = {'鬼泣':[['t',120,0],['v',120,0],['r',120,0],['q',14,0],['w',20,0],['e',40,0],['a',4,0],['s',8,0],['d',20,0],['f',30,0],['g',45,0]],
                              '剑魂':[['r',120,0],['q',11,0],['w',33,0],['e',37,0],['a',15,0],['s',120,0],['d',45,0],['f',37,0],['g',26,0]],
                              '召唤':[['w', 120, 0,[1000,1000]],['a', 3.18, 0,[100,80]],['e', 189, 0,[100,100]],['r', 152, 0,[100,100]],['t', 120, 0,[1000,1000]],['s', 21, 0,[1000,100]],['d', 31, 0,[1000,100]],['f', 42, 0,[1000,100]],['h', 46, 0,[100,80]]],
                              '剑影': [['t',120,0],['q',19,0],['e',12,0],['w',5,0],['r',42,0],['a',38,0],['s',65,0],['d',40,0],['f',5,0],['g',15,0]],
                              '修罗': [['t',120,0,[1000,1000]],['r',45,0,[1000,1000]],['g',10,0,[100,80]],['q',20,0,[100,80]],['w',50,0,[100,80]],['e',15,0,[100,80]],['a',7.5,0,[100,80]],['s',40,0,[100,80]],['d',7,0,[100,80]],['f',70,0,[100,80]],['h',120,0,[100,80]]],
                              '省无色修罗': [['t', 120, 0, [1000, 1000]], ['r', 45, 0, [1000, 1000]], ['g', 10, 0, [100, 80]],
                                       ['a', 7.5, 0, [100, 80]], ['d', 7, 0, [100, 80]],
                                       ['f', 70, 0, [100, 80]],['s', 3, 0, [100, 80]],['q', 20, 0, [100, 80]],['w', 50, 0, [100, 80]],['e', 15, 0, [100, 80]], ['h', 120, 0, [100, 80]]],
                              '小修罗': [['t', 120, 0], ['a', 8, 0], ['d', 3, 0], ['g', 10, 0]],
                              '小剑影': [['w', 5, 0], ['f', 6, 0], ['d', 3, 0],],
                              '奶萝':[['t', 180, 0,[1000,1000]],['q', 10, 0,[100,100.]],['a', 10, 0,[100,80]],['r', 12, 0,[100,100]],['g', 60, 0,[100,100]],['w', 5, 0,[100,100]],['e', 10, 0,[100,100]],['d', 40, 0,[100,100]],['s', 18, 0,[100,100]],['f', 30, 0,[100,100]],['h', 40, 0,[100,100]]],
                              }

        self.skillindex = 0
        self.heroskill2 = self.heroskilllist['省无色修罗']
    def attacktarget(self,isbos):
        self.skillindex2 = ''
        for k,v in enumerate(self.heroskill2):
            if v[1]+v[2] <= time.time():

                v[2] = time.time()
                self.skillindex2 = v[0]
                break
        if isbos:
            pydirectinput.press('h')
        pydirectinput.press(self.skillindex2)
        pydirectinput.press('x')

    def attacktarget2(self,istrue,aretrue):
        if self.lastinputtime+.5 > time.time():
            if aretrue:
                return 'x'
            return [100,100]
        if istrue:
            for k,v in enumerate(self.heroskill2):
                if v[1]+v[2] <= time.time() :
                    if aretrue:
                        v[2] = time.time()
                        self.lastinputtime = time.time()
                        print(v[0])
                        return v[0]
                    return v[3]
        else:
            for k,v in enumerate(reversed(self.heroskill2)):
                if v[1]+v[2] <= time.time() :
                    if aretrue:
                        v[2] = time.time()
                        self.lastinputtime = time.time()
                        print(v[0])
                        return v[0]
                    return v[3]
        if aretrue:
            return 'x'
        return [100,100]

    def moveto1(self,t11,t22):
        if t11 > 0:
            xx = "left"
        else:
            xx = "right"
        if t22 > 0:
            yy = "up"
        else:
            yy = "down"

        if abs(t11) < 100 and abs(t22) < 100:
            pass
        else:
            pydirectinput.press(xx)
        pydirectinput.keyDown(xx)
        t11 = abs(t11 * random.uniform(0.0008, 0.0012))  # 修罗 0.001 0.00588 剑影 0.001 0.0028 # 0.004 0.0018
        t22 = abs(t22 * random.uniform(0.004, 0.0055))
        if t22 != 0: pydirectinput.keyDown(yy)

        if t11 > t22:
            time.sleep(t22)
            pydirectinput.keyUp(yy)
            time.sleep(t11 - t22)
            pydirectinput.keyUp(xx)
        else:
            time.sleep(t11)
            pydirectinput.keyUp(xx)
            time.sleep(t22 - t11)
            pydirectinput.keyUp(yy)
    def aiinput(self,t1,t2,att,isboss):
        if t1 == 0 and t2 == 0:return
        if self.getdemo6([t1,t2]):
            t1 = random.randint(-500,500)
            t2 = random.randint(-500,500)
        if att:
            fanwie = self.attacktarget2(not isboss,False)
            if abs(t1) < fanwie[0] and abs(t2) < fanwie[1]:
                pydirectinput.press(self.attacktarget2(not isboss,True))
                att = False
            else:
                print('moveatt', t1, t2)
                self.moveto1(t1,t2)
                pydirectinput.press(self.attacktarget2(not isboss,True))
        else:
            print('move', t1, t2)
            self.moveto1( t1, t2)




    def aiinput2(self,x,t1,y,t2,att,isboss):
        if t1 == 0 and t2 == 0:return
        if -100 < t1 < 100 and -80 < t2 < 80:
            if att:
                self.attacktarget(isboss)
                att = False
        else:
            pydirectinput.press(x)
        pydirectinput.keyDown(x)
        t1 = abs(t1*random.uniform(0.0008, 0.0012)) # 修罗 0.001 0.00588 剑影 0.001 0.0028 # 0.004 0.0018
        t2 = abs(t2*random.uniform(0.004, 0.0055))
        if t2 !=0:pydirectinput.keyDown(y)

        if t1 > t2:
            time.sleep(t2)
            pydirectinput.keyUp(y)
            time.sleep(t1 - t2)
            pydirectinput.keyUp(x)
        else:
            time.sleep(t1)
            pydirectinput.keyUp(x)
            time.sleep(t2 - t1)
            pydirectinput.keyUp(y)

        if att:
            self.attacktarget(isboss)
    def getdemo1(self,x,y):
        self.input = []
        if 20 < abs(x):
            if x>0:
                self.input = [0,580] # "left"
                return 'door_left'
            else:
                self.input = [1000,580] # "right"
                return 'door_right'
        elif 20 < abs(y):
            if y > 0:
                self.input = [random.choice([0, 1000]),325] # "up"
                return 'door_up'
            else:
                self.input = [random.choice([0, 1000]),750] # "down"
                return 'door_down'


    def getdemo2(self, x):
        if 125>x[0] and 523<x[1]<670:
            print(x,'is left')
            return 'left'
        elif 875<x[0] and 523<x[1]<670:
            print(x,'is right')
            return 'right'
        elif 638<x[1] and 125<x[0]<875:
            print(x,'is down')
            return 'down'
        elif x[1]<523 and 125<x[0]<875:
            print(x,'is up')
            return 'up'

    def getdemo3(self,a,b):
        self.min_distance = 5000
        self.min_xy = [-1,-1]
        for k in a:
            self.bestrande = round(abs(b[0]-k[0]) + abs(b[1]-k[1]))
            if self.min_distance > self.bestrande:
                self.min_distance = self.bestrande
                self.min_xy = k
        return self.min_xy
    def getdemo4(self,star,end,map_data):
        x,y = round((end[0]-star[0])/22),round((end[1]-star[1])/22)
        for i in range(len(map_data)):
            for j in range(len(map_data[i])):
                if map_data[i][j] == 'end':

                    print(i - y,j - x)
                    return map_data[i - y][j - x]
    def getdemo5(self,way):
        if way == 'door_up':
            return [500,300]
        elif way == 'door_down':
            return [500,750]
        elif way == 'door_left':
            return [0,580]
        elif way == 'door_right':
            return [1000,580]
    def getdemo6(self,fangdaixy):
        if fangdaixy == self.fangdailast:
            self.fangdairoom += 1
        else:
            self.fangdailast = fangdaixy
            self.fangdairoom = 0
        if self.fangdairoom >=5:
            return True
        else:
            return False
    def moveto(self,CharacterDic):
        self.door = {}
        self.doorindex = 0
        self.fidoor = False
        self.isdoor = False
        self.hero = []
        self.ishero = False
        self.enemy = []
        self.isenemy = False
        self.isenemy_boss = False
        self.distancex = 0
        self.distancey = 0
        self.isdistance = False
        self.inputx = ''
        self.inputy = ''
        self.minihero = []
        self.miniboss = []
        self.mininext = []
        self.mini = []
        self.minix = 0
        self.miniy = 0
        self.nextdoor = ''
        self.gold = []

        for actor in CharacterDic:
            if 'door' in actor[0]:
                if actor[0] == 'door_down':
                    actor[1][1]+=180
                self.door[actor[0]] = actor[1]
                self.isdoor = True
            elif actor[0] == 'DungeonName':
                self.attacktarget(False)
                print('DungeonName')

            elif 'herotitle' == actor[0]:
                actor[1][1] += 180
                self.hero.append(actor[1])
                self.ishero = True
            elif 'enemy' in actor[0]:
                if actor[0] == 'enemy_boos':
                    self.isenemy_boss = True
                    self.enemy = [actor[1]]
                elif not self.isenemy_boss:
                    self.enemy.append(actor[1])
                self.isenemy = True
            elif actor[0] == 'minimap_next':
                self.mininext.append(actor[1])
            elif actor[0] == 'minimaphero':
                self.minihero = actor[1]
            elif actor[0] == 'minimapboss':
                if not self.SeeChallengeAgain:
                    self.SeeChallengeAgain = True
                self.miniboss = actor[1]
            elif actor[0] == 'gold':
                self.gold.append(actor[1])
            elif actor[0] == 'esc':pydirectinput.press('esc')
            elif actor[0] == 'Gabriel':
                pydirectinput.press('esc')
            elif actor[0] == 'GameMenu':
                pydirectinput.press('esc')
            elif actor[0] == 'ChallengeAgain':
                print(self.numberofdungeons,self.SeeChallengeAgain,'---------------------')

                if self.SeeChallengeAgain:
                    self.numberofdungeons += 1
                    self.SeeChallengeAgain = False
                    print(self.numberofdungeons, '次副本')
                    if self.numberofdungeons >= 4:
                        self.numberofdungeons = 0
                if self.numberofdungeons >= 3:
                    pydirectinput.press('delete')
                    time.sleep(.9)
                    pydirectinput.press('pagedown')
                    time.sleep(.3)
                    pydirectinput.press('a')
                    time.sleep(.2)
                    pydirectinput.press('space')
                    time.sleep(.1)
                    pydirectinput.press('left')
                    time.sleep(.1)
                    pydirectinput.press('space')
                    time.sleep(.1)
                    pydirectinput.press('right')
                    time.sleep(.3)
                    pydirectinput.press('esc')
                    time.sleep(.3)
                    pydirectinput.press('x')
                    time.sleep(.3)
                else:
                    pydirectinput.press('delete')
                    time.sleep(.9)
                    pydirectinput.press('pagedown')
                    time.sleep(.3)
                for k in self.heroskill2:
                    k[2] = 0
            elif actor[0] == 'NextDungeon':
                for k in self.heroskill2:
                    k[2] = 0


        if self.hero and self.gold:
            self.bestsotrrande = self.getdemo3(self.gold,self.hero[0])
            self.distancex = self.hero[0][0] - self.bestsotrrande[0]
            self.distancey = self.hero[0][1] - self.bestsotrrande[1]
        elif self.minihero and self.miniboss:
            self.nextdoor = self.getdemo4(self.minihero, self.miniboss, self.map_data)
            if self.nextdoor:
                if self.hero and self.door:
                    self.isenemy = False
                    for k, v in self.door.items():
                        print('找到了门口', k)
                        if k == self.nextdoor:
                            self.distancex = self.hero[0][0] - v[0]
                            self.distancey = self.hero[0][1] - v[1]
                            self.fidoor = True
                            break
                    if not self.fidoor:
                        print("找到了门，但不是想进的门")
                        self.distancex = self.hero[0][0] - self.getdemo5(self.nextdoor)[0]
                        self.distancey = self.hero[0][1] - self.getdemo5(self.nextdoor)[1]

                elif self.hero:
                    print("找到了下个房间，找不到门，往下个房间方向走")
                    self.distancex = self.hero[0][0] - self.getdemo5(self.nextdoor)[0]
                    self.distancey = self.hero[0][1] - self.getdemo5(self.nextdoor)[1]
                else:
                    print("随机走走")
                    self.distancex = random.randint(-500,500)
                    self.distancey = random.randint(-500,500)




        if self.hero and self.enemy and not self.mininext:
            self.bestdistance = self.getdemo3(self.enemy, self.hero[0])
            self.distancex = self.hero[0][0] - self.bestdistance[0]
            self.distancey = self.hero[0][1] - self.bestdistance[1]


        self.aiinput(self.distancex,self.distancey,self.isenemy,self.isenemy_boss)

    def updata(self, det, names):
        self.CharacterDictionary = []
        for *xyxy, conf, cls in det:
            if float(f'{conf:.2f}')> 0.65:
                self.CharacterDictionary.append([names[int(cls)],[int((xyxy[0]+xyxy[2])/2),int(xyxy[3])]])
        self.moveto(self.CharacterDictionary)