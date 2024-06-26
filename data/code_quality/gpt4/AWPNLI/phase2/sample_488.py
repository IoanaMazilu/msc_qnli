initial_caps_premise = 7.0
given_caps_premise = 2.0
remaining_caps_hypothesis = 5.0

# the hypothesis refers to the number of bottle caps Jose has left, 
# which also involves the initial bottle caps and the given bottle caps in the premise
# compute the number of bottle caps Jose has left in the premise
remaining_caps_premise = initial_caps_premise - given_caps_premise
if remaining_caps_hypothesis != remaining_caps_premise:
    # check if the remaining number of bottle caps in the hypothesis contradicts the remaining number of bottle caps from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
