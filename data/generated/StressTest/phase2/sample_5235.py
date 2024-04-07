# Premise: The distance between their homes is 52 kilometers, Sandy's walking speed is 6 km/h, and Ed's walking speed is 4 km/h.
# Hypothesis: The distance between their homes is more than 32 kilometers, Sandy's walking speed is 6 km/h, and Ed's walking speed is 4 km/h.
# Golden Label: entailment

home_distance_premise = 52
home_distance_hypothesis = 32
sandy_speed_premise = 6
sandy_speed_hypothesis = 6
ed_speed_premise = 4
ed_speed_hypothesis = 4

# the hypothesis refers to the distance between homes and the walking speeds of Sandy and Ed mentioned in the premise
if home_distance_premise <= home_distance_hypothesis:
    # check if the estimate 'home_distance_hypothesis' contradicts the distance between homes in the premise
    label = "contradiction"
elif sandy_speed_hypothesis != sandy_speed_premise:
    # check if Sandy's walking speed in the hypothesis contradicts Sandy's walking speed reported in the premise
    label = "contradiction"
elif ed_speed_hypothesis != ed_speed_premise:
    # check if Ed's walking speed in the hypothesis contradicts Ed's walking speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

