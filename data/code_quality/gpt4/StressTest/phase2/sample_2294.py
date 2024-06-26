# ratios for the ages of Krish and Vaibhav
krish_vaibhav_ratio_premise = 3/5
krish_vaibhav_ratio_hypothesis = 3/5

# the hypothesis refers to the ratio of the ages of Krish and Vaibhav mentioned in the premise
if krish_vaibhav_ratio_hypothesis >= krish_vaibhav_ratio_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it doesn't contradict the premise, but can't be explicitly entailed
    label = "neutral"

print(label)
