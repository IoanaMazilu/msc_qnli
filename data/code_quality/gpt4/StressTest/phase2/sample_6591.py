joyce_floor_premise = 71
joyce_floor_hypothesis = 51
joyce_rate_premise = 93
joyce_rate_hypothesis = 93

# the hypothesis talks about the floor Joyce started on and the rate at which she rides down, both also mentioned in the premise
if joyce_floor_premise < joyce_floor_hypothesis:
    # check if the number of floors Joyce started on in the premise contradicts the number in the hypothesis
    label = "contradiction"
elif joyce_rate_premise != joyce_rate_hypothesis:
    # check if the rate at which Joyce rides down in the premise contradicts the rate in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
