import operator
import sys
import random

import networkzero as nw0


if len(sys.argv) > 1 and sys.argv[1] == 'easy':
    MAX_QUESTNUM = 10
else:
    MAX_QUESTNUM = 100


t = 'server_team_4'
a = nw0.advertise(t)

def multiply_the_Things(y,x):
    a = 0
    for i in range(x):
        a += y
    return a

operations = {
    '+' : lambda x,y:x+y,
    '/' : lambda x,y:x//y,
    '-' : operator.sub,
    '*' : multiply_the_Things
}

def questionator3000():
    n1 = random.randint(1, MAX_QUESTNUM)
    n2 = random.randint(1, MAX_QUESTNUM)
    o, op = random.choice(list(operations.items()))
    return "{} {} {}".format(n1,o,n2), str(op(n1,n2))


num_rounds = 0
score = 0

while True:
    greeting = nw0.wait_for_message_from(a)
    print("-> {}".format(greeting))

    question, expected_answer = questionator3000()

    reply1 = "Round #{}:\nQuestion: {}".format(num_rounds, question)
    nw0.send_reply_to(a, reply1)
    print("<- " + reply1)

    answer = nw0.wait_for_message_from(a)
    print("-> {}".format(answer))


    if answer == expected_answer:
        outcome = "correct!"
        score += 1
    else:
        outcome = "incorrect, the correct answer was {}!!!!!!!".format(expected_answer)

    reply = "{}\nthe current score is: {}".format(outcome, score)
    nw0.send_reply_to(a, reply)
    print("<-" + reply)

    num_rounds += 1
