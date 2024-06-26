travel_time_premise = 4
travel_time_hypothesis = 7

# the hypothesis talks about the time taken by Kiran to travel from A to B and return from B to A
if travel_time_hypothesis <= travel_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'travel_time_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time taken, and the hypothesis value is consistent with it
    label = "entailment"

print(label)
