import random

def greet_with_personal_message(name, message):
    annotations = ['-', '+', '*', '#', '@']
    annotate = random.choice(annotations)

    def greeting():
        print(annotate * 50)
        print(message, name)
        print(annotate * 50)


    return greeting



greet_tiago = greet_with_personal_message('Tiago', 'Howdy!')
greet_ari = greet_with_personal_message('Ari', 'Hey!!')



greet_ari()
#greet_tiago()