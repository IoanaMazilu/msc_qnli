bananas_removed_premise = 5.0
initial_bananas_premise = 46.0
remaining_bananas_hypothesis = 42.0

# the hypothesis refers to the number of bananas left in the jar, which is also mentioned in the premise
# compute the remaining number of bananas in the premise
remaining_bananas_premise = initial_bananas_premise - bananas_removed_premise
if remaining_bananas_hypothesis != remaining_bananas_premise:
    # check if the number of bananas left in the hypothesis contradicts the number of bananas left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
