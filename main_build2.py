print("awesome, you can start your journey in the Picklemon world")
#give user some information

print("you meet the docter and you can choose your Pickmon!!!")
#give user some information

#let user pick one picklemon
pick = input("little fire dragon and picklechu are available to you, please type in little fire dragon to start:   ")



#let the system set little fire dragon as the one player picks
def setting1():    
    if pick.upper() == "LITTLE FIRE DRAGON":
    #set the characteristics for little fire dragon
        first = "little fire dragon"
        healthfirst = 10
        print("you have three skills:\n jumping into the fire : heals 30 health\n sparkling fire: deal 30 damage to the enemy\n born in the fire: your health goes up or down to 50")
setting1()


def setting2():
#let the system set little fire dragon as the one player picks
    if pick.upper() == "PICKLECHU":
    #set the characteristics for little fire dragon
        first = "picklechu"
        healthfirst = 60
        print("you have three skills:\n One Hundred Thousand Volts: you lose half of your health and deal 50 damage to the ememy\n steel tail: heals 10 and deals 20 damage\n electrical bomb: your health goes down to 1 and deals 80 damage to the ememy")
setting2()
#set the health of the boss
healthbig = 100


#print(first)

#this funtion aims at check the picklemon the player has and then start the battle
def battle_chu(master, healthmaster):
    choice1 = input("which pickelmon you want to put into the battle? (the one you have: little fire dragon : ")
    #this line checks if the user types the correct name of the picklemon
    pickle1 = choice1
    if choice1 == first:
        print("you chose " + first)
    else: 
        print("you spelt the wrong name")
        battle_chu("big stone snake, healthbig")
    #this line make the battle starts
    print("the battle starts!!!")
    print("the master uses pickmon " + master)
    
    
    #this line set the health of 2 players for the functions below
    health1 = healthfirst
    health2 = healthmaster

    #these line inform the players the health they have
    print("the health of the master's pickmon is: ")
    print(health2)
    print("the health of your picklemon is: ")
    print(health1)
    while health1 >=0 and health2 >=0 and first == "picklechu":
      #these line aims at making the skills effective and giving players choices  
        if first == "picklechu":
            skill = input("what is the skill you want to use?(just type 1,2,3 according to the sequence the instruction of your skill)\n : ")
            if skill == "1":
                health1 = health1 /2
                health2 = health2 - 50
                skill = 0
            elif skill == "2":
                health2 = health2 - 20
                health1 = health1 + 10
                skill = 0
            elif skill == "3":
                health1 = 1
                health2 = health2 - 80
                skill = 0
            


        #these line aims at showing the damage the master's picklemon dealt
        print("the big stone name uses smash. Your picklemon lost 25 health")
        health1 = health1 - 25
        
        
        
        #these lines give the information about the recent health of the players and the masters
        print(health1)
        #give user some information
        print("Your health is:")
        #give user some information
        print(health1)
        #give user some information
        print("the health of the master is:")
        #give user some information
        print(health2)
    if health2 <= 0:
        print("you win!")
    elif health1 <= 0:
        print("you lost, game over")
        

def battle_fire(master, healthmaster):
    choice1 = input("which pickelmon you want to put into the battle? (the one you have: little fire dragon : ")
    #this line checks if the user types the correct name of the picklemon
    pickle1 = choice1
    if choice1 == first:
        print("you chose " + first)
    else: 
        print("you spelt the wrong name")
        battle_fire("big stone snake", healthbig)
    #this line make the battle starts
    print("the battle starts!!!")
    print("the master uses pickmon " + master)
    
    
    #this line set the health of 2 players for the functions below
    health1 = healthfirst
    health2 = healthmaster

    #these line inform the players the health they have
    print("the health of the master's pickmon is: ")
    #give user some information
    print(health2)
    #give user some information
    print("the health of your picklemon is: ")
    #give user some information
    print(health1)
    while health1 >=0 and health2 >=0:
      #these line aims at making the skills effective and giving players choices  
        if first == "little fire dragon":
            skill = input("what is the skill you want to use?(just type 1,2,3 according to the sequence the instruction of your skill)\n : ")
            if skill == "1":
                health1 = health1 + 30
                skill = 0
            elif skill == "2":
                health2 = health2 - 30
                skill = 0
            elif skill == "3":
                health1 = 50
                skill = 0
             


        #these line aims at showing the damage the master's picklemon dealt
        print("the big stone name uses smash. Your picklemon lost 25 health")
        health1 = health1 - 25
        
        
        
        #these lines give the information about the recent health of the players and the masters
        print(health1)
        #give user some information
        print("Your health is:")
        #give user some information
        print(health1)
        #give user some information
        print("the health of the master is:")
        #give user some information
        print(health2)
    if health2 <= 0:
        print("you win!")
    elif health1 <= 0:
        print("you lost, game over")


#call the function for battles for picklemons
battle_chu("big stone snake", healthbig)
battle_fire("big stone snake", healthbig)
