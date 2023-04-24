import random
reroll = "yes"
while reroll == "yes" or reroll == "Yes" or reroll == "YEs" or reroll == "YES" or reroll == "yEs" or reroll == "yES" or reroll == "yeS" or reroll == "YeS"  or reroll == "y" or reroll == "Y":
    none = 0
    one_in_pen = 0
    sharing = 0
    share = 0
    zookeeper_one = False
    zookeeper_sharing = False

    for i in range(100000):
        ellie = random.randint(1,6)
        ellise = random.randint(1,6)
        zookeeper = random.randint(1,6)

        
        if ellie != zookeeper and ellise != zookeeper:
            none += 1       

        elif ellie == zookeeper or ellise == zookeeper:
            one_in_pen += 1
            if ellie == ellise:
                share = ellie
                if share == zookeeper:
                    sharing += 1


    sharing = sharing/100000 * 100
    one_in_pen = one_in_pen/100000 * 100
    none = none/100000 * 100

    sharing = round(sharing, 2)
    one_in_pen = round(one_in_pen, 2)
    none = round(none, 2)

    sharing = float(sharing)
    one_in_pen = float(one_in_pen)
    none = float(none)

    if 31 < one_in_pen > 35:
        zookeeper_one = True
    if 14 < sharing > 18:
        zookeeper_sharing = True
    
    print()
    print("The zookeeper finds two elephants in a pen " + str(sharing) + "% of the time")
    print("The zookeeper finds at least one elephant in a pen " + str(one_in_pen) + "% of the time")
    print("The zookeeper finds no elephants " + str(none) + "% of the time")
    print()

    if zookeeper_one == True:
        print("The zookeeper was right about there being one elephant in the pen he checks 1/3 of the time")
    else:
        print("The zookeeper was wrong about there being one elephant in the pen he checks 1/3 of the time")
    if zookeeper_sharing == True:
        print("The zookeeper was right about there being two elephants in the pen he checks 1/6 of the time")
    else:
         print("The zookeeper was wrong about there being two elephants in the pen he checks 1/6 of the time")


    reroll = input("Run the simulation again? (yes or no): ")
    print()

print("Thanks for helping out!")
