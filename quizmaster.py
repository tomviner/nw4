import operator
import random

import networkzero as nw0

MAX_QUESTNUM = 20

t = 'server_team_4'
a = nw0.advertise(t)

def multiply_the_Things(y,x):
    a = 0
    for i in range(x):
        a += y
    return a

operations = {
    '+' : lambda x,y:x+y,
    '-' : operator.sub,
    '*' : multiply_the_Things
}

def questionator3000():
    n1 = random.randint(0, MAX_QUESTNUM)
    n2 = random.randint(0, MAX_QUESTNUM)
    o, op = random.choice(list(operations.items()))
    return "{} {} {}".format(n1,o,n2), str(op(n1,n2))


while True:
    greeting = nw0.wait_for_message_from(a)
    print("-> {}".format(greeting))

    question, expected_answer = questionator3000()

    nw0.send_reply_to(a, question)
    print("<- {}".format(question))

    answer = nw0.wait_for_message_from(a)
    print("-> {}".format(answer))


    if answer == expected_answer:
        outcome = "correct!"
    else:
        outcome = "incorrect!"

    nw0.send_reply_to(a, outcome)
    print("<- {}, the correct answer was {}".format(outcome, expected_answer))
