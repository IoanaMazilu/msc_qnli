alice_leaves_city_a_premise = 30
alice_leaves_city_a_hypothesis = 60

# the hypothesis talks about the time difference between Alice and Bob's departure from City A
if alice_leaves_city_a_hypothesis <= alice_leaves_city_a_premise:
    # check if the hypothesis value contradicts the estimate of less than 'alice_leaves_city_a_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference between Alice and Bob
    # any time difference greater than 'alice_leaves_city_a_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
