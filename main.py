import random
p1 = None
p_score = 0
c_score = 0


user_name = input("Enter your name player:").capitalize() 
while p1 != "quit":
    
    l1 = ["rock","paper","scissor"]

    random_el = random.choice(l1)

    
    p1 = input("{} Put your move:".format(user_name))


    print("{}: {}".format(user_name, p1))
    print("{}: {}".format("PC", random_el))
    

    if p1 == random_el:
        print("draw")
    elif p1 == "rock" and random_el == "scissor":
        print( "{} wins".format(user_name))
        p_score +=1
    elif p1 == "paper" and random_el == "rock":
        print( "{} wins".format(user_name))
        p_score +=1  
    elif p1 == "scissor" and random_el == "paper":
        print( "{} wins".format(user_name))
        p_score +=1     
    else:
        print("PC wins")
        c_score +=1
    print("*"*50)
print("{}:{}".format(user_name,p_score))
print("{}:{}".format("PC",p_score))
