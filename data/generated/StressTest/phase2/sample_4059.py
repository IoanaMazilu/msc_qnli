# Premise: The distance between their homes is 36 kilometers, Betty's walking speed is 4 km/h, and Dave's walking speed is 3 km/h.
# Hypothesis: The distance between their homes is less than 86 kilometers, Betty's walking speed is 4 km/h, and Dave's walking speed is 3 km/h.
# Golden Label: entailment

home_distance_premise = 36
home_distance_hypothesis = 86
betty_speed_premise = 4
betty_speed_hypothesis = 4
dave_speed_premise = 3
dave_speed_hypothesis = 3

# the hypothesis refers to the distance between homes, Betty's and Dave's walking speed mentioned in the premise
if home_distance_premise > home_distance_hypothesis:
    # check if the estimation of 'home_distance_hypothesis' contradicts the distance in the premise
    label = "contradiction"
elif betty_speed_premise != betty_speed_hypothesis:
    # check if Betty's speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif dave_speed_premise != dave_speed_hypothesis:
    # check if Dave's speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

