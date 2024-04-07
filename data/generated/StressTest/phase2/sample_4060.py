# Premise: The distance between their homes is less than 86 kilometers, Betty's walking speed is 4 km/h, and Dave's walking speed is 3 km/h.
# Hypothesis: The distance between their homes is 36 kilometers, Betty's walking speed is 4 km/h, and Dave's walking speed is 3 km/h.
# Golden Label: neutral

distance_premise = 86
distance_hypothesis = 36
betty_speed_premise = 4
betty_speed_hypothesis = 4
dave_speed_premise = 3
dave_speed_hypothesis = 3

# the hypothesis refers to the distance between homes and the walking speeds of Betty and Dave mentioned in the premise
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the estimate of less than 'distance_premise'
    label = "contradiction"
elif betty_speed_hypothesis != betty_speed_premise or dave_speed_hypothesis != dave_speed_premise:
    # check if the walking speeds in the hypothesis contradict the walking speeds reported in the premise
    label = "contradiction"
elif distance_hypothesis < distance_premise:
    # the premise only gives an estimate for the distance
    # any distance less than 'distance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

