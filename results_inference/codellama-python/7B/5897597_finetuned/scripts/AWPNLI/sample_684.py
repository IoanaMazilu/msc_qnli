bottles_premise = 45.0
drank_premise = 14.0
sister_drank_premise = 8.0
left_bottles_hypothesis = 23.0

# the hypothesis refers to the number of bottles left, which can be calculated from the premise
# compute the number of bottles left in the premise
left_bottles_premise = bottles_premise - drank_premise - sister_drank_premise
if left_bottles_hypothesis!= left_bottles_premise:
    # check if the number of bottles left in the hypothesis contradicts the number of bottles left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)