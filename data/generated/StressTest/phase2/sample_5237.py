# Premise: The distance between their homes is 52 kilometers, Sandy's walking speed is 6 km/h, and Ed's walking speed is 4 km/h.
# Hypothesis: The distance between their homes is less than 52 kilometers, Sandy's walking speed is 6 km/h, and Ed's walking speed is 4 km/h.
# Golden Label: contradiction

distance_premise = 52
distance_hypothesis = 52
sandy_speed_premise = 6
sandy_speed_hypothesis = 6
ed_speed_premise = 4
ed_speed_hypothesis = 4

# hypothesis talks about the distance between homes and the walking speeds of Sandy and Ed
if distance_hypothesis >= distance_premise:
    # check if the hypothesis value contradicts the statement that the distance is less than 'distance_premise'
    label = "contradiction"
elif sandy_speed_hypothesis != sandy_speed_premise or ed_speed_hypothesis != ed_speed_premise:
    # check if the walking speeds in the hypothesis contradict the walking speeds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

