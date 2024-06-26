drank_bottles_premise = 14.0
sister_drank_bottles_premise = 8.0
bottles_left_hypothesis = 23.0

# the hypothesis refers to the number of bottles left, which can be computed from the premise
# compute the number of bottles left in the premise
bottles_left_premise = 45.0 - (drank_bottles_premise + sister_drank_bottles_premise)
if bottles_left_hypothesis!= bottles_left_premise:
    # check if the number of bottles left in the hypothesis contradicts the number of bottles left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
