# Premise: Denise adds 5.0 bananas to a jar and there were originally 46.0 bananas in the jar.
# Hypothesis: 54.0 bananas are left in the jar.
# Golden Label: contradiction

bananas_added_premise = 5.0
bananas_original_premise = 46.0
bananas_total_hypothesis = 54.0

# the hypothesis refers to the total number of bananas, which are also calculated in the premise
# compute the total number of bananas in the premise
total_bananas_premise = bananas_added_premise + bananas_original_premise
if bananas_total_hypothesis != total_bananas_premise:
    # check if the total number of bananas in the hypothesis contradicts the total number of bananas from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

