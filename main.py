import random
from game_data import data
from art import logo, vs


print("Bine ai venit la Cine are cei mai multi urmăritori!")
scor = 0
prima_alegere = random.choice(data)

while True:
    print(logo)
    a_doua_alegere = random.choice(data)
    followers_a_doua_alegere = a_doua_alegere['follower_count']

    print(f"\nCompară: {prima_alegere['name']}, {prima_alegere['description']}, din {prima_alegere['country']}.")
    print(vs)
    print(f"\nCu: {a_doua_alegere['name']}, {a_doua_alegere['description']}, din {a_doua_alegere['country']}.")

    alegere_jucator = input("Alege 1 sau 2 pentru alegerea ta: ")

    followers_prima_alegere = prima_alegere['follower_count']
    if followers_prima_alegere > followers_a_doua_alegere and alegere_jucator == '1':
        scor += 1
        print(f"Ai ghicit! Scorul tău este acum {scor}.")
    elif followers_a_doua_alegere > followers_prima_alegere and alegere_jucator == '2':
        scor += 1
        prima_alegere = a_doua_alegere
    else:
        print(f"Ai pierdut. Scorul tău final este de {scor}.")
        break
