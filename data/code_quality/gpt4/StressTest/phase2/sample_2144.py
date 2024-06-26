alice_departure_premise = 30
alice_departure_hypothesis = 60

# the hypothesis talks about the time Alice leaves City A, also mentioned in the premise
if alice_departure_hypothesis == alice_departure_premise:
    # check if the time of Alice's departure in the hypothesis is exactly the same as the time given in the premise
    label = "contradiction"
else:
    # the premise only provides a specific departure time for Alice
    # any departure time other than 'alice_departure_premise' doesn't contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
