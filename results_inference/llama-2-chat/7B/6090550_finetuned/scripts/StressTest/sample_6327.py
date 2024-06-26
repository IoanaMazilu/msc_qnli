y_premise = 10
y_hypothesis = 20

# the hypothesis talks about the number of boxes of cigarettes Kramer can pack per minute, which is also mentioned in the premise
if y_hypothesis <= y_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
