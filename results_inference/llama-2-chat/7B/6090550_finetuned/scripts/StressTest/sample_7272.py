y_premise = 12
y_hypothesis = 72

# the hypothesis talks about the number of trees Kyle has to cut down, which is also mentioned in the premise
if y_hypothesis <= y_premise:
    # check if the hypothesis value contradicts the number of trees in the premise
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it does not contradict it
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
