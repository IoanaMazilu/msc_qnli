sisters_distance_premise = 2
sisters_distance_hypothesis = 3

# the hypothesis talks about the distance the twins ran, referenced also in the premise
if sisters_distance_hypothesis >= sisters_distance_premise:
    # check if the hypothesis value contradicts the distance the twins ran in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
