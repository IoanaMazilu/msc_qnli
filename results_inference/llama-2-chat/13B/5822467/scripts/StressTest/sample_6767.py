people_premise = 13
people_hypothesis = 12

# the hypothesis refers to the number of people in a BCCI meeting
if people_hypothesis <= people_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific number of people, while the hypothesis gives a lower number
    # any number of people less than or equal to 12 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
