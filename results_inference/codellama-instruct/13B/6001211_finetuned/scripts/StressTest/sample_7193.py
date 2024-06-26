departure_time_premise = 12
departure_time_hypothesis = 12

# the hypothesis refers to the departure time of the train mentioned in the premise
if departure_time_hypothesis >= departure_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)