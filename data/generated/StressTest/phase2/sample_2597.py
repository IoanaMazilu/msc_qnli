# Premise: Rosy is 30% more efficient than Mary.
# Hypothesis: Rosy is less than 30% more efficient than Mary.
# Golden Label: contradiction

rosy_efficiency_premise = 30
rosy_efficiency_hypothesis = 30

# the hypothesis refers to Rosy's efficiency relative to Mary mentioned in the premise
if rosy_efficiency_hypothesis >= rosy_efficiency_premise:
    # check if the estimate of 'rosy_efficiency_hypothesis' contradicts the efficiency difference in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

