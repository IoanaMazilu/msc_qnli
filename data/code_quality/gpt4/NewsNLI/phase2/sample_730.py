wave_height_feet_premise = 100
wave_height_feet_hypothesis = 100

# the hypothesis mentions the height of the wave in feet, which is also mentioned in the premise
if wave_height_feet_hypothesis > wave_height_feet_premise:
    # check if the height of the wave in the hypothesis contradicts the height of the wave reported in the premise
    label = "contradiction"
else:
    # if the height of the wave in the hypothesis does not contradict the height of the wave in the premise, we can infer entailment
    label = "entailment"

print(label)
