import ast
import itertools

import networkzero as nw0

t = 'server_team_4'
a = nw0.discover(t)

def get_ans(question):
    return str(ast.literal_eval(question))
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
