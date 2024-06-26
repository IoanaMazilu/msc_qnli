london_eye_premise = 443
london_eye_hypothesis = 343
high_roller_premise = 550
high_roller_hypothesis = 550

# the hypothesis refers to the height of the London Eye and Las Vegas' High Roller
if london_eye_hypothesis <= london_eye_premise:
    # check if the estimate of 'london_eye_hypothesis' contradicts the height of the London Eye in the premise
    label = "contradiction"
elif high_roller_hypothesis!= high_roller_premise:
    # check if the height of the Las Vegas' High Roller in the hypothesis contradicts the height reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
