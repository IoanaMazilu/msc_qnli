john_age_times_mark_premise = 3
john_age_times_mark_hypothesis = 8

# the hypothesis refers to the age ratio between John and Mark, also mentioned in the premise
if john_age_times_mark_hypothesis <= john_age_times_mark_premise:
    # check if the hypothesis value contradicts the age ratio mentioned in the premise
    label = "contradiction"
elif john_age_times_mark_hypothesis != john_age_times_mark_premise:
    # if the hypothesis value does not contradict the premise one, but it's not the same either, we have a neutral situation
    label = "neutral"
else:
    # if the hypothesis value is exactly the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
