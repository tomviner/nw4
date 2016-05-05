import networkzero as nw0

t = 'server_team_4'

a = nw0.discover(t)

question = nw0.send_message_to(a, "-> I'm ready for the quiz!")

print('<- {}'.format(question))

ans = input("What's the answer? ")
print("-> {}".format(ans))

n = nw0.send_message_to(a, ans)

print('<- {}'.format(n))
