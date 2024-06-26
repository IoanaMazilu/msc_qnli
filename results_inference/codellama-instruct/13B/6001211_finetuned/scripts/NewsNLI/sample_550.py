meteor_width_premise = 4
meteor_weight_premise = 4000
brightness_premise = 5
brightness_hypothesis = 5

# the hypothesis mentions the brightness of the fireball, which is also mentioned in the premise
# however, the hypothesis does not mention the width or weight of the meteor, which cannot be entailed from the premise
if brightness_hypothesis!= brightness_premise:
    # check if the brightness in the hypothesis contradicts the brightness reported in the premise
    label = "contradiction"
else:
    # if the brightness in the hypothesis does not contradict the brightness in the premise, we can infer neutrality
    label = "neutral"

print(label)
