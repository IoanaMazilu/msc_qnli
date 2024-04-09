rosy_eye_premise = 443
rosy_eye_hypothesis = 343
high_roller_premise = 550

# the hypothesis refers to the heights of the London Eye and the High Roller mentioned in the premise
if rosey_eye_hypothesis > rosey_eye_premise and high_roller_premise == high_roller_hypothesis:
    # check if the hypothesis values for both the London Eye and the High Roller contradict the premise values
    label = "contradiction"
elif rosey_eye_hypothesis <= rosey_eye_premise and high_roller_hypothesis == high_roller_premise:
    # check if the hypothesis values for either the London Eye or the High Roller contradict the premise values
    label = "neutral"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
