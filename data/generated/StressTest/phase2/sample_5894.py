# Premise: The distance between Delhi and Mathura is 110 kms.
# Hypothesis: The distance between Delhi and Mathura is 710 kms.
# Golden Label: contradiction

distance_delhi_mathura_premise = 110
distance_delhi_mathura_hypothesis = 710

# the hypothesis talks about the same distance mentioned in the premise
if distance_delhi_mathura_hypothesis != distance_delhi_mathura_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"

print(label)
