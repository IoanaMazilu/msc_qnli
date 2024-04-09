hours_premise = 40
hours_hypothesis = 40

# the hypothesis refers to the number of hours James is paid x dollars per hour, mentioned in the premise
if hours_hypothesis >= hours_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
