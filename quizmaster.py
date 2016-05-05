import networkzero as nw0

t = 'server_team_4'
a = nw0.advertise(t)


question = "What is 2 + 2?"
expected_answer = "4"


greeting = nw0.wait_for_message_from(a)
print("-> {}".format(greeting))


nw0.send_reply_to(a, question)
print("<- {}".format(question))


answer = nw0.wait_for_message_from(a)
print("-> {}".format(answer))


if answer == expected_answer:
    outcome = "correct!"
else:
    outcome = "incorrect!"

nw0.send_reply_to(a, outcome)
print("<- {}".format(outcome))
