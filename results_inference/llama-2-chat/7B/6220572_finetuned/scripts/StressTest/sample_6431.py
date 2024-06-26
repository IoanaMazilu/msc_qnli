london_eye_height_premise = 443
london_eye_height_hypothesis = 443
high_roller_height_premise = 550
high_roller_height_hypothesis = 550

# the hypothesis refers to the height of the London Eye and High Roller mentioned in the premise
if london_eye_height_hypothesis >= london_eye_height_premise:
    # check if the hypothesis estimate contradicts the height of the London Eye in the premise
    label = "contradiction"
elif high_roller_height_hypothesis!= high_roller_height_premise:
    # check if the height of the High Roller in the hypothesis contradicts the height reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
