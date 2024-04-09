bottles_initial_premise = 45.0
drank_by_maria_premise = 14.0
drank_by_sister_premise = 8.0
bottles_left_hypothesis = 18.0

# the hypothesis refers to the number of bottles left, which can be calculated from the premise
# compute the number of bottles left in the premise
bottles_left_premise = bottles_initial_premise - (drank_by_maria_premise + drank_by_sister_premise)
if bottles_left_hypothesis!= bottles_left_premise:
    # check if the number of bottles left in the hypothesis contradicts the number of bottles left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
