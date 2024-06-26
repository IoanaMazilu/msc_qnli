initial_bottles_premise = 45.0
drunk_bottles_premise = 14.0
sister_drunk_bottles_premise = 8.0
remaining_bottles_hypothesis = 23.0

# the hypothesis refers to the number of bottles left, which can be computed from the premise
# compute the remaining bottles in the premise
remaining_bottles_premise = initial_bottles_premise - drunk_bottles_premise - sister_drunk_bottles_premise
if remaining_bottles_hypothesis!= remaining_bottles_premise:
    # check if the number of remaining bottles in the hypothesis contradicts the number of remaining bottles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
