# Premise: Rosy is 50% more efficient than Mary.
# Hypothesis: Rosy is more than 50% more efficient than Mary.
# Golden Label: contradiction

rosy_efficiency_premise = 50
rosy_efficiency_hypothesis = 50

# The hypothesis makes a claim about Rosy's efficiency compared to Mary, a topic also mentioned in the premise.
if rosy_efficiency_hypothesis <= rosy_efficiency_premise:
    # Check if the hypothesis percentage contradicts the percentage mentioned in the premise.
    label = "contradiction"
else:
    # The premise gives an exact percentage for Rosy's efficiency compared to Mary.
    # Any percentage greater than 'rosy_efficiency_premise' cannot be explicitly entailed from the premise, but doesn't contradict it either.
    label = "neutral"

print(label)

