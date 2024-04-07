# Premise: The distance between Delhi and Mathura is 150 kms.
# Hypothesis: The distance between Delhi and Mathura is 450 kms.
# Golden Label: contradiction

distance_delhi_mathura_premise = 150
distance_delhi_mathura_hypothesis = 450

# the hypothesis refers to the same distance mentioned in the premise
if distance_delhi_mathura_hypothesis != distance_delhi_mathura_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # the distance provided in the premise exactly matches the distance in the hypothesis
    label = "entailment"

print(label)

