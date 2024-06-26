members_premise = 59
members_hypothesis = 19

# the hypothesis refers to the number of members in Lourdes school class mentioned in the premise
if members_hypothesis >= members_premise:
    # check if the hypothesis value contradicts the number of members in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of members
    # the hypothesis specifies a lower limit, which is less than the number given in the premise
    # the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
