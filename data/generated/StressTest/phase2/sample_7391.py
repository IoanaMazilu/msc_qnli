# Premise: Rosy is 10% more efficient than Mary.
# Hypothesis: Rosy is less than 10% more efficient than Mary.
# Golden Label: contradiction

efficiency_difference_premise = 10
efficiency_difference_hypothesis = 10

# the hypothesis refers to the efficiency difference between Rosy and Mary, mentioned in the premise
if efficiency_difference_hypothesis >= efficiency_difference_premise:
    # check if the value stated in the hypothesis contradicts the premise's efficiency difference
    label = "contradiction"
else:
    # if the hypothesis value is less than the one in the premise, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

