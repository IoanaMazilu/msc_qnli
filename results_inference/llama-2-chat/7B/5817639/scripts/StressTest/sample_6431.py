london_eye_premise = 443
london_eye_hypothesis = 443
high_roller_premise = 550
high_roller_hypothesis = 550

# the hypothesis talks about the height of the London Eye and High Roller, referenced also in the premise
if london_eye_hypothesis <= london_eye_premise:
    # check if the hypothesis value contradicts the estimate of the height of the London Eye in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the height of the London Eye
    # any height less than or equal to the estimate in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

if high_roller_hypothesis <= high_roller_premise:
    # check if the hypothesis value contradicts the estimate of the height of High Roller in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the height of High Roller
    # any height less than or equal to the estimate in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
