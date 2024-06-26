london_eye_height_premise = 443
london_eye_height_hypothesis = 343
las_vegas_roller_height_premise = 550
las_vegas_roller_height_hypothesis = 550

# the hypothesis talks about the heights of the London Eye and the Las Vegas’High Roller, both mentioned in the premise
if london_eye_height_hypothesis >= london_eye_height_premise:
    # check if the estimate of 'london_eye_height_hypothesis' contradicts the height of the London Eye in the premise
    label = "contradiction"
elif las_vegas_roller_height_hypothesis != las_vegas_roller_height_premise:
    # check if the height of the Las Vegas’High Roller in the hypothesis contradicts the height reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
