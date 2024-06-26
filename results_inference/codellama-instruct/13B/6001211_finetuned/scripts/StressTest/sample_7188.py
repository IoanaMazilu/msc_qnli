departure_time_premise = 12
departure_time_hypothesis = 42

# the hypothesis refers to the train departure time mentioned in the premise
if departure_time_hypothesis < departure_time_premise:
    # check if the 'departure_time_hypothesis' contradicts the departure time in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
