distance_premise = 45
distance_hypothesis = 35

# the hypothesis talks about the initial distance between Fred and Sam, also mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the initial distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the initial distance
    # any initial distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the initial distance in the hypothesis equals the distance in the premise, we can infer entailment
    label = "entailment"

print(label)
