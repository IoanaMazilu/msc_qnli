london_eye_height_premise = 443
london_eye_height_hypothesis = 343
high_roller_height_premise = 550
high_roller_height_hypothesis = 550

# the hypothesis talks about the heights of London Eye and High Roller mentioned in the premise
if london_eye_height_hypothesis!= london_eye_height_premise:
    # check if the estimate of 'london_eye_height_hypothesis' contradicts the height of London Eye in the premise
    label = "contradiction"
elif high_roller_height_hypothesis!= high_roller_height_premise:
    # check if the estimate of 'high_roller_height_hypothesis' contradicts the height of High Roller in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)