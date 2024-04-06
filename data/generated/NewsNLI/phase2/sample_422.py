# Premise: The quake's epicenter was reported to be in Negros, about 360 miles south-southeast of Manila.
# Hypothesis: It struck in Negros, about 360 miles south-southeast of Manila.
# Golden Label: entailment

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

