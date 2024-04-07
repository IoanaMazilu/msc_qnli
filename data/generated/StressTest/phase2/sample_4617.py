# Premise: The distance from Steve's house to work is 35 Km.
# Hypothesis: The distance from Steve's house to work is less than 45 Km.
# Golden Label: entailment

distance_premise = 35
distance_hypothesis = 45

# the hypothesis refers to the same distance mentioned in the premise
if distance_premise > distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of less than 'distance_hypothesis'
    label = "contradiction"
elif distance_premise == distance_hypothesis:
    # check if the distance in the premise equals the value in the hypothesis
    label = "contradiction"
else:
    # if the premise value is less than 'distance_hypothesis' we can infer entailment
    label = "entailment"

print(label)

