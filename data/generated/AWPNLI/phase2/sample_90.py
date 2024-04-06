# Premise: Denise removes 5.0 bananas from a jar and there were originally 46.0 bananas in the jar.
# Hypothesis: 41.0 bananas are left in the jar.
# Golden Label: entailment

removed_bananas_premise = 5.0
original_bananas_premise = 46.0
bananas_left_hypothesis = 41.0

# the hypothesis refers to the number of bananas left, which are also mentioned in the premise
# compute the number of bananas left in the premise
bananas_left_premise = original_bananas_premise - removed_bananas_premise
if bananas_left_hypothesis != bananas_left_premise:
    # check if the number of bananas left in the hypothesis contradicts the number of bananas left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

