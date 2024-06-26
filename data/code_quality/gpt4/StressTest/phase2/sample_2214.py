water_jars_premise = 35
water_jars_hypothesis = 55

# the hypothesis talks about the amount of water in jars, referenced also in the premise
if water_jars_hypothesis <= water_jars_premise:
    # check if the hypothesis value contradicts the amount of water in jars in the premise
    label = "contradiction"
elif water_jars_premise >= water_jars_hypothesis:
    # check if the amount of water in jars in the premise contradicts the estimate of less than 'water_jars_hypothesis'
    label = "contradiction"
else:
    # the hypothesis value does not contradict the premise one, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
