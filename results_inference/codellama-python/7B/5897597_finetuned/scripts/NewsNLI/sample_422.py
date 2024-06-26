distance_to_manila_premise = 360
distance_to_manila_hypothesis = 360

# the hypothesis mentions the distance of the quake's epicenter to Manila, which is also mentioned in the premise
if distance_to_manila_hypothesis!= distance_to_manila_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis distance does not contradict the premise distance, we can infer entailment
    label = "entailment"

print(label)
