miles_walked_premise = 4
miles_walked_hypothesis = 3

# the hypothesis refers to the distance walked by Jack, which is also mentioned in the premise
if miles_walked_premise <= miles_walked_hypothesis:
    # check if the estimate of'miles_walked_hypothesis' contradicts the distance walked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
