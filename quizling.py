import ast
import itertools
import sys
import time

import networkzero as nw0

t = 'server_team_4'
a = nw0.discover(t)

def get_ans(question, n):
    return input("What's the answer? ")
if len(sys.argv) > 1 and sys.argv[1] == 'hard':
    from t1000 import get_ans

for round in itertools.count():
    # print('ROUND {}'.format(round))
    question = nw0.send_message_to(a, "-> I'm ready!")

    print('<- {}'.format(question))
    ans = get_ans(question, round)
    print("-> {}".format(ans))

    n = nw0.send_message_to(a, ans)

    print('<- {}'.format(n))
    print()
