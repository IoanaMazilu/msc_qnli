people_bacci_premise = 13
people_bacci_hypothesis = 13

# the hypothesis refers to the number of people in a BCCI meeting, mentioned in the premise
if people_bacci_hypothesis < people_bacci_premise:
    # check if the hypothesis value contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of people in a BCCI meeting
    # any number of people less than or equal to 'people_bacci_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
