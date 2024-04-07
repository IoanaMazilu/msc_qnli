# Premise: The distance between Delhi and Mathura is 110 kms.
# Hypothesis: The distance between Delhi and Mathura is less than 410 kms.
# Golden Label: entailment

distance_premise = 110
distance_hypothesis = 410

# the hypothesis refers to the distance between Delhi and Mathura mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the premise value contradicts the estimate of less than 'distance_hypothesis'
    label = "contradiction"
elif distance_premise == distance_hypothesis:
    # check if the premise value equals the hypothesis value
    label = "neutral"
else:
    # if the premise value does not contradict the hypothesis value, we can infer entailment
    label = "entailment"

print(label)

