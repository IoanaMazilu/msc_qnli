distance_premise = 100
distance_hypothesis = 800

# hypothesis talks about the initial distance between Fred and Sam, as mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance mentioned in the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # check if the distance in hypothesis is exactly the same as in the premise
    label = "entailment"
else:
    # if the distance in the hypothesis is more than in the premise, this is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)