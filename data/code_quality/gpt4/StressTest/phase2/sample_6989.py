ratio_age_premise = 7/3
ratio_age_hypothesis = 1/3

# the hypothesis talks about the ratio of ages of Anil and his son, referenced also in the premise
if ratio_age_hypothesis != ratio_age_premise:
    # check if the ratio of ages in the hypothesis contradicts the ratio of ages reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
