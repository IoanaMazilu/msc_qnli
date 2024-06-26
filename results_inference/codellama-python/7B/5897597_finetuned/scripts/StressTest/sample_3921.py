departure_time_premise = 9
departure_time_hypothesis = 4

# the hypothesis refers to the departure time of the train mentioned in the premise
if departure_time_premise <= departure_time_hypothesis:
    # check if the departure time in the premise contradicts the estimate of 'departure_time_hypothesis'
    label = "contradiction"
else:
    # if the departure time in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
