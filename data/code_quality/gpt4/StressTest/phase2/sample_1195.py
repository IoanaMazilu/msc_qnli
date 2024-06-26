distance_premise = 65
distance_hypothesis = 55

# the hypothesis talks about the distance between Fred and Sam, referenced also in the premise
if distance_hypothesis > distance_premise:
    # check if the distance value in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
