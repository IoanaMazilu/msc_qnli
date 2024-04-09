ratio_premise = 1/7
ratio_hypothesis = 6/7

# the hypothesis talks about a different ratio than the premise
if ratio_hypothesis <= ratio_premise:
    # check if the hypothesis value contradicts the estimate of the ratio in the premise
    label = "contradiction"
else:
    # the premise gives a specific ratio, any other ratio than the one in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

# calculate the number of sheep in the farm using the ratio in the hypothesis
sheep_number = (12880 // 230) * (7 // ratio_hypothesis)

# print the label
print(label)

# print the estimated number of sheep in the farm
print(sheep_number)
