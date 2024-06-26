ratio_sheep_horses_premise = 7/7
ratio_sheep_horses_hypothesis = 5/7

# the hypothesis refers to the ratio of sheep to horses at the Stewart farm
if ratio_sheep_horses_hypothesis >= ratio_sheep_horses_premise:
    # check if the ratio of sheep to horses in the hypothesis contradicts the one in the premise
    label = "contradiction"
else:
    # if the ratio in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
