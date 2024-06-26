width_premise = 4
weight_premise = 4000
brightness_premise = 5
brightness_hypothesis = 5

# the hypothesis refers to the brightness of the fireball, which is also mentioned in the premise
if brightness_hypothesis!= brightness_premise:
    # check if the brightness in the hypothesis contradicts the brightness reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
