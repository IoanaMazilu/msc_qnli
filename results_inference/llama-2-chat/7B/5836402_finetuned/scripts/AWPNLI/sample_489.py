start_caps_premise = 7.0
given_caps_premise = 2.0
left_caps_hypothesis = 4.0

# the hypothesis refers to the number of bottle caps, which are also mentioned in the premise
# compute the number of bottle caps left in the premise
left_caps_premise = start_caps_premise - given_caps_premise
if left_caps_hypothesis!= left_caps_premise:
    # check if the number of bottle caps left in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)