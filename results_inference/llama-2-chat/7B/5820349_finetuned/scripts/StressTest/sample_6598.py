distance_premise = 35
distance_hypothesis = 15

# the hypothesis talks about the distance between Efrida and Frazer's homes, which is also mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise gives only an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the distance in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
