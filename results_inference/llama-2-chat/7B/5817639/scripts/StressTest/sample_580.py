alice_leaves_city_a_premise = 60
alice_leaves_city_a_hypothesis = 30

# the hypothesis refers to the time difference between Alice and Bob's departure from City A
if alice_leaves_city_a_hypothesis <= alice_leaves_city_a_premise:
    # check if the hypothesis value contradicts the estimate of less than 'alice_leaves_city_a_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference, but the hypothesis value is consistent with it
    label = "neutral"

print(label)
