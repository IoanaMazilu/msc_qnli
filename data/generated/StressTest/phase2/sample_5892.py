# Premise: The distance between Delhi and Mathura is 110 kms.
# Hypothesis: The distance between Delhi and Mathura is less than 310 kms.
# Golden Label: entailment

distance_delhi_mathura_premise = 110
distance_delhi_mathura_hypothesis = 310

# the hypothesis talks about the distance between Delhi and Mathura, which is also mentioned in the premise
if distance_delhi_mathura_hypothesis < distance_delhi_mathura_premise:
    # check if the hypothesis value contradicts the exact distance mentioned in the premise
    label = "contradiction"
elif distance_delhi_mathura_hypothesis == distance_delhi_mathura_premise:
    # if the hypothesis value equals the premise value, we can infer entailment
    label = "entailment"
else:
    # any distance less than 'distance_delhi_mathura_hypothesis' is consistent with the hypothesis,
    # but cannot be explicitly entailed from the hypothesis as we only have an exact distance in the premise
    label = "neutral"

print(label)

