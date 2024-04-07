# Premise: Rosy is 50% more efficient than Mary.
# Hypothesis: Rosy is more than 20% more efficient than Mary.
# Golden Label: entailment

efficiency_premise = 50
efficiency_hypothesis = 20

# The hypothesis refers to the efficiency difference between Rosy and Mary, mentioned also in the premise
if efficiency_hypothesis >= efficiency_premise:
    # check if the hypothesis value contradicts the efficiency difference mentioned in the premise
    label = "contradiction"
elif efficiency_hypothesis > efficiency_premise:
    # check if the efficiency difference in the hypothesis is greater than the one in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

