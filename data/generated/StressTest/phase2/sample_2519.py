# Premise: The distance between Delhi and Mathura is 130 kms.
# Hypothesis: The distance between Delhi and Mathura is 630 kms.
# Golden Label: contradiction

distance_delhi_mathura_premise = 130
distance_delhi_mathura_hypothesis = 630

# The hypothesis makes a claim about the same distance mentioned in the premise
if distance_delhi_mathura_premise != distance_delhi_mathura_hypothesis:
    # Check if the distance in the hypothesis contradicts the distance given in the premise
    label = "contradiction"
else:
    # If the distances in both the premise and hypothesis are the same, we can infer entailment
    label = "entailment"

print(label)

