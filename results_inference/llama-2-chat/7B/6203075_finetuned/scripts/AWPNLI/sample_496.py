bananas_added_premise = 5.0
bananas_left_hypothesis = 51.0

# the hypothesis refers to the number of bananas left in the jar, which is also mentioned in the premise
# compute the total number of bananas in the premise
total_bananas_premise = bananas_added_premise + bananas_left_hypothesis
if total_bananas_premise!= bananas_left_hypothesis:
    # check if the number of bananas left in the hypothesis contradicts the number of bananas left in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
