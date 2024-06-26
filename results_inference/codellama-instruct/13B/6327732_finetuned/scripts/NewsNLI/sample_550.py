width_premise = 4
weight_premise = 4000
brightness_premise = 5

width_hypothesis = None
weight_hypothesis = None
brightness_hypothesis = 5

# the hypothesis mentions the brightness of the fireball, which is also mentioned in the premise
# however, the hypothesis does not mention the width or weight of the meteor, which cannot be entailed from the premise
label = "neutral"

print(label)
