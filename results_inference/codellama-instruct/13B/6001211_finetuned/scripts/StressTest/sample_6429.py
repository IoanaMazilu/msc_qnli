london_eye_height_premise = 443
london_eye_height_hypothesis = 343
high_roller_height_premise = 550
high_roller_height_hypothesis = 550

# the hypothesis refers to the height of the London Eye and the High Roller mentioned in the premise
if london_eye_height_premise <= london_eye_height_hypothesis:
    # check if the estimate of 'london_eye_height_hypothesis' contradicts the height of the London Eye in the premise
    label = "contradiction"
elif high_roller_height_hypothesis!= high_roller_height_premise:
    # check if the height of the High Roller in the hypothesis contradicts the height of the High Roller reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
