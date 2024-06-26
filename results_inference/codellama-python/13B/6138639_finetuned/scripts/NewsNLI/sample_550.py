burn_brightness_premise = 5
burn_brightness_hypothesis = 5

# the hypothesis mentions the brightness of the fireball, which is also mentioned in the premise
if burn_brightness_hypothesis!= burn_brightness_premise:
    # check if the brightness in the hypothesis contradicts the brightness reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
