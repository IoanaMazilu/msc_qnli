members_premise = 59
members_hypothesis = 59

# the hypothesis refers to the number of members in the class mentioned in the premise
if members_hypothesis >= members_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
