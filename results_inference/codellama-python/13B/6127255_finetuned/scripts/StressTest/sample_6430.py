#london_eye_height_premise = 343
#london_eye_height_hypothesis = 443
#high_roller_height_premise = 550
#high_roller_height_hypothesis = 550

# the hypothesis talks about the height of the London Eye and the High Roller, referenced also in the premise
# first, we check the height of the London Eye
if london_eye_height_hypothesis <= london_eye_height_premise:
    # check if the height of the London Eye in the hypothesis contradicts the estimate of more than 'london_eye_height_premise'
    label = "contradiction"
# next, we check the height of the High Roller
elif high_roller_height_hypothesis!= high_roller_height_premise:
    # check if the height of the High Roller in the hypothesis contradicts the height of the High Roller reported in the premise
    label = "contradiction"
# the premise gives only an estimate for the height of the London Eye
# any height of the London Eye greater than 'london_eye_height_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
else:
    label = "neutral"

print(label)
