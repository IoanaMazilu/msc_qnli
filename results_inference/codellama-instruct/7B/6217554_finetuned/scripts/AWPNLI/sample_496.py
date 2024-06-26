bananas_added_premise = 5.0
bananas_original_premise = 46.0
bananas_left_hypothesis = 51.0

# the hypothesis refers to the number of bananas left in the jar, which is also mentioned in the premise
# compute the total number of bananas left in the premise
bananas_left_premise = bananas_original_premise - bananas_added_premise
if bananas_left_hypothesis!= bananas_left_premise:
    # check if the number of bananas left in the hypothesis contradicts the number of bananas left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
