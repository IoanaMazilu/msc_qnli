picked_oranges_premise = 37.0
sold_oranges_premise = 10.0
left_oranges_hypothesis = 23.0

# the hypothesis refers to the number of oranges left, which can be computed from the premise
# compute the number of oranges left in the premise
left_oranges_premise = picked_oranges_premise - sold_oranges_premise
if left_oranges_hypothesis != left_oranges_premise:
    # check if the number of oranges left in the hypothesis contradicts the number of oranges left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
