import turtle 
import random

player_one = turtle.Turtle()

player_one.color("green")

player_one.shape("turtle")

player_one.penup()

player_one.goto(-200,100)

player_two = player_one.clone()

player_two.color("blue")

player_two.penup()

player_two.goto(-200,-100)

player_one.goto(300,60)

player_one.pendown()

player_one.circle(40)

player_one.penup()

player_one.goto(-200,100)

player_two.goto(300,-140)

player_two.pendown()

player_two.circle(40)

player_two.penup()

player_two.goto(-200,-100)

die = [1,2,3,4,5,6]
for i in range(20):

     if player_one.pos() >= (300,100):

             print("Jogador N°1 ganhou!")
             break

     elif player_two.pos() >= (300,-100):

             print("Jogador N°2 ganhou!")
             break
     else:

             player_one_turn = input("Aperte enter para rolar o dado, Jogador N°1!")
             die_outcome = random.choice(die)
             print("O resultado do dado é: ")
             print(die_outcome)
             print("Serão andadas este número de casas: ")
             print(20*die_outcome)
             player_one.fd(20*die_outcome)
             player_two_turn = input("Aperte enter para rolar o dado, Jogador N°2!")
             die_outcome = random.choice(die)
             print("O resultado do dado é: ")
             print(die_outcome)
             print("Serão andadas este número de casas: ")
             print(20*die_outcome)
             player_two.fd(20*die_outcome)