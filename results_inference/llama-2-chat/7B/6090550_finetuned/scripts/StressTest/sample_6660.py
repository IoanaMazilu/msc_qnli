ys_premise = 40
ys_hypothesis = 70

# the hypothesis talks about the percentage of money given by Jones to his wife, referenced also in the premise
if ys_hypothesis <= ys_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it does not contradict the premise
    # however, it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
