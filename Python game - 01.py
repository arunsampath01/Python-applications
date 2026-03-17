import time as t
def part_I():
    A="WELCOME TO THE GAME"
    print(A.center(70))
    t.sleep(2)
    print("In the early cold shivering morning, the maid of the house having a cup of coffe in hand\nwalked to hand it over to the owner of the house. when she opened the door, she was shocked, dropped\nthe cup of coffee which shattered in to the pieces all over the floor. slipped by means of the coffee and\nfell down on the floor, trying to pick herself up from the floor along with some courage\nshe ran towards her madem's room.\n\tKNOCK. . .\n\t\tKNOCK. . .\n\t\t\tKNOCK. . .")
    print("soon the onwer's wife rushed to the door and opened and asked,what is it maid?.sweating all over her face she answered in terror,\n MASTER has been KILLED!!!" )
    t.sleep(1)
    name=str(input("\nENTER YOUR NAME TO PARTICIPATE: "))
    a=str(input("choose do you like to participate in the crime( type Detective): "))

    if(a=="Dective"):
        print("are you STRONG enough to solve the case?")
        b=str(input("conform your choice to take the leap(yes or no): "))
        if(b=="yes"):
            print("*****************************************************************************************************************")
            print("good, let us begin. . .")
            print("as soon as Madam heard she rushed to the room, turned on the lights and finally found her husband laying dead.\nlater the maid called the police and the dective for the investigation\n.")
            print("soon the police and",name,"reached the house.",name,"inspected the body thoroughly and finalised that the owner was stabbed by means of sharp objects.\nlater", name ,"enquired began to everyone\n")
            print("who would you like to investigate:")
            print("1.maid")
            print("2.chef")
            print("3.gardener")
            print("4.wife")
            for i in range(4):
                c=int(input("(1--4):  "))
                if(c==1):
                    t.sleep(1)
                    print(name,": you were the one who found him first right?")
                    print("maid: yes sir, i was the one who saw him first")
                    print(name,": why did you go into his room that early morning?")
                    print("maid: to give him coffee. since he was getting ready for a travel to canada")
                    print(name,": you may go...did you scream?")
                    print("she suddenly turned with terror and answered no. . . no sir")
                    print("\nEnter to investigate other")
                elif(c==2):
                    t.sleep(1)
                    print(name,": what did you do when the maid screamed?")
                    print("chef:after making the coffee and slept for a while since it was early morning. suddenly due to the screaming of the maid\n i woke up from the sleep and rushed towards where the sound came from")
                    print("hearing the chef",name,"stared at him and said, you may go")
                    print("\nEnter to investigate other")
                elif(c==3):
                    t.sleep(1)
                    print(name,": how did you come to know about that your owner has been killed?")
                    print("gardener: by means of the chef")
                    print(name,": why didn't wake for the maid's screem?")
                    print("gardener:sir the maid never screamed")
                    print(name,": you may go")
                    print("\nEnter to investigate other")
                elif(c==4):
                    t.sleep(1)
                    print("dective: i am sorry to enquire you at this stage but it is essential. hope you understand.")
                    print("wife: no it's fine. i am completly alright\n Detective got a doubt by the attitude of the wife")
                    print(name,":what were you doing when your husband was killed?")
                    print("wife: i was in my room, having a sleep\nlater maid called me and i went and switched on the lights found he was lying dead.")
                    print(name,":why didn't you help your husband to pack his things for his travel?")
                    print("keepin her eye contact away from",name,"wife answered: that is not essential and. . .i never know where is going to travel")
                    print("with a great doubt on wife",name,"further asked\n",name,":do you think is there anyone who have conflict with your husband?")
                    print("wife:jake\n",name)
                    print("\nEnter to investigate other")
                else:
                    print("invalid format")
                input("\nEnter to continue. . .")

            print("as soon as the enquire is done",name,"stepped towards wife's room and stood before her room")
            d=str(input("\nenter wife's room or go away\ndecide: "))
            if(d=="enter wife's room"):
                print("he entered the room and searched around the cupboards. finally he found a knife of blood stains,\nsecrectly he took that weapon proff")
            elif(d=="go away"):
                print("after greetings",name,"left the home and began his travel towards JAKE's HOUSE")
            else:
                print("after greetings", name, "left the home and began his travel towards JAKE's HOUSE")
            print("\n\t\t\t\t\t\tJAKE'S HOUSE\n")
            print("\n\tKNOCK. . .\n\t\tKNOCK. . .\n\t\t\tKNOCK. . .\nJake opened the door",name,"introduced himself")
            print(name,": mr.jake hope you know your partner is dead")
            print("jake: yes, i do")
            print(name,": recently i came to know that you and your partner has some disputes")
            print("jake: do you think i killed him")
            print(name,": i never said he was killed")
            print("jake: mr. i am getting late for flight to canada")
            print(name,": how come you dont care for your partner's death")
            print("jake: look it's almost 5 years ago i never seen my partner since he moved to another company.")
            print("as they were arguing jake's son entered the scene. he left the place with a smile in face and\n also jake began to move out of the house without listing to",name)
            print("both son and father took their car and moved in different path")
            print("decide\n--> follow jake's car\n--> follow jake son's car")
            e=str(input("\nyour decision:"))
            if(e=="follow jake's car"):
                print("finally with the help of police",name,"nabbed jake and took him under custody")
                print("jake: you guys are wasting my time. it's almost 5 years ago i never seen my partner since he moved to another company.\ni swear i never done anything to him\nit is true i had disputes with him in earlier days like almost 3 years  ago.")
                print(name,"do you suspect on any other?")
                print("jake: no. . .i getting late")
                t.sleep(5)
                print("\n\n\n*******************************************************************          MISSION FAILED          *******************************************************************\n\n\n")
                print("PLAY AGAIN. . .?")
                d=str(input("(yes or no): "))
                if(d=="yes"):
                    part_I()
                elif(d=="no"):
                    print("quit game")
                else:
                    print("invalid response")
            elif(e=="follow jake son's car"):
                print(name,"chased his car and finally caught him and took him for an enquire")
                print(name,":why do you have to run from us, when you have nothing  to hide from us?")
                print("jake's son: my father will hear about this!!!")
                print(name,":he's not that close enough to hear you. might now he would have been flying")
                print("he began to show his attitude there by the police began to strike him\nduring the time",name,"secretly took his phone")
                print("it was locked")
                def password():
                    print("SOLVE THE RIDDLES TO EXPLORE THE PHONE\nThere are 3 riddle to be solved\n** only 3 attempts are left for each riddle** ")
                    print("if you fail, the phone will be permanently locked")
                    t.sleep(2)
                    for j in range(3):
                        RIDDLE_1 = str(input("I am an odd number.\ntake away a letter and I become even\nWhat am I?\nANSWER: "))
                        if RIDDLE_1.lower() == "seven":
                            print("Riddle 1 is correct")
                            break
                        else:
                            print("Incorrect")

                    else:
                        print("This phone has been locked")
                        print("\n\n\n*******************************************************************          MISSION FAILED          *******************************************************************\n\n\n")
                        print("PLAY AGAIN. . .?")
                        d = str(input("(yes or no): "))
                        if(d=="yes"):
                            part_I()
                        elif(d=="no"):
                            print("Quit game")
                        else:
                            print("Invalid response")
                    for k in range(3):
                        RIDDLE_2 = str(input("I have hands but I cannot clap to make sound\nwho am i?\nANSWER:"))
                        if (RIDDLE_2 == "clock"):
                            print("riddle 2 is correct")
                            break
                        else:
                            print("Incorrect")


                    else:
                        print("This phone has been locked")
                        print("\n\n\n*******************************************************************          MISSION FAILED          *******************************************************************\n\n\n")
                        print("PLAY AGAIN. . .?")
                        d = str(input("(yes or no): "))
                        if (d == "yes"):
                            part_I()
                        elif (d == "no"):
                            print("Quit game")
                        else:
                            print("Invalid response")

                    for l in range(3):
                        RIDDLE_3 = str(input("I sleeps through out the day and cries through out the night.\nthe more I cries, the more I lights\nwho am i?\nANSWER:"))
                        if (RIDDLE_3 == "candle"):
                            print("riddele 3 is correct")
                            break
                        else:
                            print("Incorrect")

                    else:
                        print("This phone has been locked")
                        print("\n\n\n*******************************************************************          MISSION FAILED          *******************************************************************\n\n\n")
                        print("PLAY AGAIN. . .?")
                        d = str(input("(yes or no): "))
                        if (d == "yes"):
                            part_I()
                        elif (d == "no"):
                            print("Quit game")
                        else:
                            print("Invalid response")
                password()
            else:
                print("invalid input")
            print("")
            print("later",name,"unlocked the phone and began to search inside\nsoon after then he found that there was a huge money transsication between jake's son and chef of the partner's house")
            print("for a moment",name,"was baffled in confusion and was unable to understand what happened")
            print(name,"rushed inside and asked jake's son.")
            print(name,":why did you send money to chef?")
            print("jake's son: to kill the partner because he did not give me a share of the company even though i was in the same position in the same company")
            print(name,":ok, if you ordered to kill. then who killed the partner")
            print("jake's son: it might be the chef...by this time they might hve escaped from the partner's house")
            print(name,": they? who are the people other than the chef...TELL ME.\n but jake's son did not answer")
            print("------------------------------------------------------------------------------------------------------------------------------------------")

            print("TO GO REACH THE PARTNER'S HOUSE\nThere are 3 ways (!!! (the TIME was 1.00 pm) !!!)\n  1.HIGHWYAS(takes 45min)\n  2.CITY WAYS(takes 60min)\n  3.RAILWAY TRACK CROSSING\n   *it takes about 30min for a train to cross\n   *the crossover closed before 10 min of train's arrival\n   *it takes about 30 min to reach railway track from jake's house ")
            print("")
            f=str(input("decide:" ))
            if(f=="highways"):
                print(name,"reached the partner's house ")
            elif(f=="city ways"):
                print("\n\n\n*******************************************************************          MISSION FAILED          *******************************************************************\n\n\n")
                print("PLAY AGAIN. . .?")
                d = str(input("(yes or no): "))
                if (d == "yes"):
                    part_I()
                elif (d == "no"):
                    print("Quit game")
                else:
                    print("Invalid response")
            elif(f=="railway track crossing"):
                print("\n\n\n*******************************************************************          MISSION FAILED          *******************************************************************\n\n\n")
                print("PLAY AGAIN. . .?")
                d = str(input("(yes or no): "))
                if (d == "yes"):
                    part_I()
                elif (d == "no"):
                    print("Quit game")
                else:
                    print("Invalid response")
            else:
                print("invalid response")

            t.sleep(3)
            print(name,"rushed into the house and caught the chef and asked. . .")
            print(name,": why did you kill him? soon he noticed that there were CCTV cameras all around the house.")
            print("wife: did chef kill him?,",name)
            print(name,": i hope not. and he asked the for the wife to have a look on the cameras\n\n")
            print(name,"do you want to look,\n  *look the camera of partner's room\n  *look all the camera of the house\n")
            for m in range(2):
                g=int(input("which camera do you want to look?\n1.look the camera of partner's room\n2.look all the camera of the house\nDECIDE(1 or 2): "))
                if(g==1):
                    print("\n\n\n*******************************************************************          MISSION FAILED          *******************************************************************\n\n\n")
                    print("PLAY AGAIN. . .?")
                    d = str(input("(yes or no): "))
                    if (d == "yes"):
                        part_I()
                        break
                    elif (d == "no"):
                        print("Quit game")
                        print("THANK YOU FOR PLAYING THE GAME")
                        break
                    else:
                        print("Invalid response")

                elif(g==2):
                    print("proced to check the camera")
                    break
                else:
                    print("invalid response")
                input("\nEnter to continue...")
            print("")
            print("whem",name,"opned the camera videos folder.there were some viedos missing")
            print("wife:",name,"some of our cameras near my husband's room are damaged and\nthe camera in the pathway to my husband's room are also damaged")
            print("while",name,"was scrolling the videos. he found that\n *Gardener was sleeping the garage\n *chef and maid were making coffee in the kitchen\n *wife was sleeping in room")
            print("further he noticed, a nearby coconut tree reflected light from the owner's room when the light was kept on in his room")
            print("after noticing it,",name,"played the video when maid ran to inform about the death later chef came in and walked away from the owner's room with a file and that too with in 1 min.")
            print("at that time he noticed the TREE DID NOT REFLECT ANY LIGHT.\n\n\n")

            print("*****",name.upper(),":THE CASE IS CLOSED*****")
            print("")

            print("WHO IS THE KILLER?\n---> CHEF\n--->MAID\n--->GARDENER\n--->WIFE\n")
            n=str(input("WHO IS THE KILLER?: "))
            if(n == "maid"):
                print("GAME OVER")
                print("arun,your are great dective")
            else:
                print("mission failed")
            print(name,": the killer is maid,\nSINCE WHEN SHE ENTERS THE ROOM THERE WAS NO REFLECTION OF THE TREE(means-->the light was not on)\nand wife mentioned she switched light first")
            print(name,": then why can't chef be the killer?\n because a person cannot kill someone in just 1 min")
            print("then the maid and chef confessed that it was the jake's son who hired them to do such things for money and the file that chef took was\nregarding COMPANY'S SHARE INFO that were to be given to jake's son")
            print("\n\n\n")
            print("the police arrested the killer\n\n.")
            print(name,"approched wife with a curious dobut\n",name,": why dint you like your husband?")
            print("the wife did not answer anything, she just gave a look at",name)
            Z="THANK YOU"
            print(Z.center(100))
    else:
        print("Please Type Detective")
        part_I()

part_I()