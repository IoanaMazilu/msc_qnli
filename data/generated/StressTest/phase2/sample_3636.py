# Premise: A train leaves Delhi at 9 a.
# Hypothesis: A train leaves Delhi at more than 6 a.
# Golden Label: entailment

departure_time_premise = 9
departure_time_hypothesis = 6

# the hypothesis refers to the departure time of the train mentioned in the premise
if departure_time_premise <= departure_time_hypothesis:
    # check if the 'departure_time_premise' contradicts the estimate of more than 'departure_time_hypothesis'
    label = "contradiction"
else:
    # if the departure time in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)

