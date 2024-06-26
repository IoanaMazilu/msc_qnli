legs_premise = 6.0
sides_premise = 2.0
legs_side_hypothesis = 0.0

# the hypothesis refers to the number of legs on a side, which is also mentioned in the premise
# compute the number of legs on a side in the premise
legs_side_premise = legs_premise / sides_premise
if legs_side_hypothesis != legs_side_premise:
    # check if the number of legs on a side in the hypothesis contradicts the number of legs on a side from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
