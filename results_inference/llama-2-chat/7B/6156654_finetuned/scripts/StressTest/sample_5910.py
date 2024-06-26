# the premise and hypothesis are the same, except for the ratio between sheep and horses
ratio_premise = 1/7
ratio_hypothesis = 6/7

# the hypothesis talks about the ratio between sheep and horses, which is also mentioned in the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it does not contradict it
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
