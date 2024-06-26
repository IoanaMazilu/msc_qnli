lewis_brown_age_ratio_premise = 6/2
lewis_brown_age_ratio_hypothesis = 1/2

# the hypothesis refers to the ratio of the present ages of Lewis and Brown mentioned in the premise
if lewis_brown_age_ratio_hypothesis!= lewis_brown_age_ratio_premise:
    # check if the ratio of the ages in the hypothesis contradicts the ratio of ages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
