percentage_hypothesis = 3
percentage_premise = 7

if percentage_hypothesis >= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage
    # any percentage less than 'percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
