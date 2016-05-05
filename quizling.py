import ast
import itertools
import sys
import time

import networkzero as nw0

t = 'server_team_4'
a = nw0.discover(t)

def get_ans(question, n):
    if len(sys.argv) > 1 and sys.argv[1] == 'hard':
        q = question.replace('/', '//').split(':')[-1].strip()
        # print(q)
        ans = str(eval(q))
        print("What's the answer? ", end='', flush=1)
        s = 3 / (n + 1)
        time.sleep(1.2 * s)
        if not n:
            time.sleep(5)
        for ch in ans:
            print(ch, end='', flush=1)
            time.sleep(s)
        print()
        return ans
    return input("What's the answer? ")

for round in itertools.count():
    # print('ROUND {}'.format(round))
    question = nw0.send_message_to(a, "-> I'm ready!")

    print('<- {}'.format(question))
    ans = get_ans(question, round)
    print("-> {}".format(ans))

    n = nw0.send_message_to(a, ans)

    print('<- {}'.format(n))
    print()
