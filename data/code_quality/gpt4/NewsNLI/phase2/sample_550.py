meteor_width_premise = 4
meteor_weight_premise = 4000
brightness_factor_premise = 5

brightness_factor_hypothesis = 5

# the hypothesis only mentions the brightness factor of the meteor, which is also mentioned in the premise
if brightness_factor_hypothesis != brightness_factor_premise:
    # check if the brightness factor in the hypothesis contradicts the brightness factor reported in the premise
    label = "contradiction"
else:
    # if the brightness factor from the hypothesis does not contradict the brightness factor in the premise, we can infer entailment
    label = "entailment"

print(label)
