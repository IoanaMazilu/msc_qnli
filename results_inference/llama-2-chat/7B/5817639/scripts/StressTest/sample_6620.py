people_premise = 7
people_hypothesis = 4

# the hypothesis refers to a subset of people from the premise
if people_hypothesis <= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of people, and the hypothesis provides a smaller subset
    # any subset of people smaller than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
