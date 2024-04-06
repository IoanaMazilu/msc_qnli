# Premise: Mike picked 32.0 limes, and Alyssa ate 25.0 limes and Tom picked 12.0 plums.
# Hypothesis: 10.0 limes were left.
# Golden Label: contradiction

picked_limes_premise = 32.0
eaten_limes_premise = 25.0
left_limes_hypothesis = 10.0

# the hypothesis refers to the number of limes left, which are also mentioned in the premise
# compute the number of limes left in the premise
left_limes_premise = picked_limes_premise - eaten_limes_premise
if left_limes_hypothesis != left_limes_premise:
    # check if the number of limes left in the hypothesis contradicts the number of limes left from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

