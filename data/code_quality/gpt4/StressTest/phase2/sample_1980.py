distance_premise = 40
distance_hypothesis = 60

# the hypothesis talks about the distance from Marathon to Athens, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis estimate contradicts the distance reported in the premise
    label = "contradiction"
elif distance_premise != distance_hypothesis:
    # the premise gives an exact distance, any other distance cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
