london_eye_height_premise = 343
london_eye_height_hypothesis = 443
las_vegas_high_roller_height_premise = 550
las_vegas_high_roller_height_hypothesis = 550

# the hypothesis refers to the heights of the London Eye and Las Vegas' High Roller mentioned in the premise
if london_eye_height_hypothesis <= london_eye_height_premise:
    # check if the height of the London Eye in the hypothesis contradicts the height in the premise
    label = "contradiction"
elif las_vegas_high_roller_height_hypothesis!= las_vegas_high_roller_height_premise:
    # check if the height of Las Vegas' High Roller in the hypothesis contradicts the height in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the height of the London Eye
    # any height greater than 'london_eye_height_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
