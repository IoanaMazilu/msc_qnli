width_premise = 4
weight_premise = 4000
brightness_premise = 5
brightness_hypothesis = 5

# the hypothesis mentions the brightness of the meteor, which is also mentioned in the premise
# however, the hypothesis does not mention the other quantities mentioned in the premise
if brightness_hypothesis!= brightness_premise:
    # check if the brightness in the hypothesis contradicts the brightness reported in the premise
    label = "contradiction"
else:
    # if the hypothesis brightness does not contradict the premise brightness, but other quantities are missing, we can infer neutrality
    label = "neutral"

print(label)
