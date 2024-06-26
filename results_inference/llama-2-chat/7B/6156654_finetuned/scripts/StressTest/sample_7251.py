runs_premise = 8
runs_hypothesis = 5

# the hypothesis refers to the number of runs Suraj has in a certain number of innings, which is also mentioned in the premise
if runs_hypothesis <= runs_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif runs_hypothesis > runs_premise:
    # if the hypothesis value is greater than the premise value, it does not contradict the premise
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, it does not contradict the premise
    label = "neutral"

print(label)
