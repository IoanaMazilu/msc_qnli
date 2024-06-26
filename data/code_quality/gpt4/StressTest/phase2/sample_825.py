distance_premise = 24
distance_hypothesis = 74

# the hypothesis talks about the distance from X to Y, also mentioned in the premise
if distance_premise >= distance_hypothesis:
    # check if the distance in the premise contradicts the estimate of less than 'distance_hypothesis'
    label = "contradiction"
elif distance_premise != distance_hypothesis:
    # check if the distance in the premise is different from the 'distance_hypothesis'
    label = "neutral"
else:
    # if the distance in the hypothesis does not contradict and is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
