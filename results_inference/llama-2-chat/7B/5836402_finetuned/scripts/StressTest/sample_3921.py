departure_time_premise = 9
departure_time_hypothesis = 4

# the hypothesis refers to the departure time of a train from Delhi mentioned in the premise
if departure_time_premise <= departure_time_hypothesis:
    # check if the estimate of 'departure_time_hypothesis' contradicts the departure time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
