# Premise: The distance between Delhi and Mathura is 150 kms.
# Hypothesis: The distance between Delhi and Mathura is less than 650 kms.
# Golden Label: entailment

distance_delhi_mathura_premise = 150
distance_delhi_mathura_hypothesis = 650

# the hypothesis refers to the distance between Delhi and Mathura mentioned in the premise
if distance_delhi_mathura_hypothesis < distance_delhi_mathura_premise:
    # check if the hypothesis value contradicts the distance mentioned in the premise
    label = "contradiction"
elif distance_delhi_mathura_hypothesis == distance_delhi_mathura_premise:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"
else:
    # the premise gives the exact distance
    # any distance less than 'distance_delhi_mathura_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

