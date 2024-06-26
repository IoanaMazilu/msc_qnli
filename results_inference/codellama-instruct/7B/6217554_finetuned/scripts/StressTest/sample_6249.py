boys_group_premise = 6
boys_group_hypothesis = 5

if boys_group_hypothesis >= boys_group_premise:
    # check if the hypothesis value contradicts the number of boys in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys
    # any number of boys greater than 'boys_group_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
