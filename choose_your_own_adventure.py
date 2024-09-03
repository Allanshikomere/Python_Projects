name = input("Type yoyr name: ")

print("Welcome",  name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go either left or right")


if answer == "left":
        answer = input("You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross").lower()

        if answer == "swim":
            print("You swam accross and were eaten by an alligator.")
        elif answer == "walk":
            print("You walked for many miles, and ran out of enaergy")
        else:
            print('Not a valid option. You loose.')

elif answer == "right":
     answer = input(" You go back to the main road and lose.")
     if answer == "back":
            print("You swam accross and were eaten by an alligator.")
     elif answer == "cross":
            answer = input("You cross the bridge and meet  a stranger will you talk to them")


            if answer == "yes":
                  print("You talk to the stanger and they give you Gold. You WIN!")

            elif answer == "no":
                  print("You ignore the stanger, they get offended and you lose")

            else:
                  print("Not a valid option you lose")
else:
            print('Not a valid option. You loose.')

print("Thank you trying", name)
