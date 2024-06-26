start_bottle_caps_premise = 7.0
given_bottle_caps_premise = 2.0
left_bottle_caps_hypothesis = 4.0

# the hypothesis refers to the number of bottle caps left, which are also mentioned in the premise
if left_bottle_caps_hypothesis!= (start_bottle_caps_premise - given_bottle_caps_premise):
    # check if the number of bottle caps left in the hypothesis contradicts the number of bottle caps left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
