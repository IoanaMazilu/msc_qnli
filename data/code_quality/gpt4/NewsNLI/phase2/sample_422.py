quake_distance_premise = 360
quake_distance_hypothesis = 360

# the hypothesis mentions the quake's distance from Manila, which is also mentioned in the premise
if quake_distance_hypothesis != quake_distance_premise:
    # check if the quake distance in the hypothesis contradicts the quake distance reported in the premise
    label = "contradiction"
else:
    # if the quake distance does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
