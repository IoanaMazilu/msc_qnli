london_eye_premise = 343
london_eye_hypothesis = 443
las_vegas_high_roller_premise = 550
las_vegas_high_roller_hypothesis = 550

# the hypothesis refers to the heights of the London Eye and Las Vegas' High Roller mentioned in the premise
if london_eye_hypothesis!= london_eye_premise:
    # check if the height of the London Eye in the hypothesis contradicts the height mentioned in the premise
    label = "contradiction"
elif las_vegas_high_roller_hypothesis!= las_vegas_high_roller_premise:
    # check if the height of Las Vegas' High Roller in the hypothesis contradicts the height mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
