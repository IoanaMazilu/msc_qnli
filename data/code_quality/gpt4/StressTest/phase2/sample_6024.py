percentage_return_premise = 4
percentage_return_hypothesis = 6

# the hypothesis refers to the percentage amount Dana returns to her parents, mentioned also in the premise
if percentage_return_hypothesis <= percentage_return_premise:
    # check if the hypothesis value contradicts the 'percentage_return_premise'
    label = "contradiction"
else:
    # the premise gives an exact percentage of the amount Dana returns to her parents
    # any percentage less than 'percentage_return_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
