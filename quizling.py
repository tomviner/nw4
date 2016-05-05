import ast
import itertools
import sys

import networkzero as nw0

t = 'server_team_4'
a = nw0.discover(t)

def get_ans(question):
    if len(sys.arvg) > 1 and sys.argv[1] == 'easy':
        q = question.replace('/', '//').split(':')[-1].strip()
        print(repr(q))
        return str(eval(q))
    return input("What's the answer? ")

for round in itertools.count(1):
    print('ROUND {}'.format(round))
    question = nw0.send_message_to(a, "-> I'm ready!")

    print('<- {}'.format(question))
    ans = get_ans(question)
    print("-> {}".format(ans))

    n = nw0.send_message_to(a, ans)

    print('<- {}'.format(n))
    print()
