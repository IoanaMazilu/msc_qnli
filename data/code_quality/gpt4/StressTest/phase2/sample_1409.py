ratio_age_hema_brother_premise = 3/2
ratio_age_hema_brother_hypothesis = 3/2

# the hypothesis refers to the ratio of ages of Hema and her brother, which is also mentioned in the premise
if ratio_age_hema_brother_hypothesis >= ratio_age_hema_brother_premise:
    # check if the ratio of ages in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
