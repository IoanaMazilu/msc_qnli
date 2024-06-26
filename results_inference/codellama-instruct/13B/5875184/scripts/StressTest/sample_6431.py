rosy_match_premise = 443
rosy_match_hypothesis = 443
london_eye_premise = 443
london_eye_hypothesis = 443
high_roller_premise = 550
high_roller_hypothesis = 550

# the hypothesis refers to the height of the London Eye and the High Roller, both mentioned in the premise
if london_eye_hypothesis <= london_eye_premise:
    # check if the estimate of 'london_eye_hypothesis' contradicts the height of the London Eye in the premise
    label = "contradiction"
elif high_roller_hypothesis!= high_roller_premise:
    # check if the height of the High Roller in the hypothesis contradicts the height of the High Roller reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
