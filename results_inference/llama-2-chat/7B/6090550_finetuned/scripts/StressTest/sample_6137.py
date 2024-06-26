hours_james_premise = 41
hours_james_hypothesis = 41

# the hypothesis refers to the number of hours James worked last week, which is also mentioned in the premise
if hours_james_hypothesis >= hours_james_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it does not contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
