# Premise: The distance between Delhi and Mathura is 110 kms.
# Hypothesis: The distance between Delhi and Mathura is less than 210 kms.
# Golden Label: entailment

distance_delhi_mathura_premise = 110
distance_delhi_mathura_hypothesis = 210

# the hypothesis refers to the distance between Delhi and Mathura mentioned in the premise
if distance_delhi_mathura_premise >= distance_delhi_mathura_hypothesis:
    # check if the estimate of 'distance_delhi_mathura_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif distance_delhi_mathura_premise != distance_delhi_mathura_hypothesis:
    # check if the hypothesis distance contradicts the premise distance
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

