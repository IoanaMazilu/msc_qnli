percentage_premise = 2
percentage_hypothesis = 6

# the hypothesis refers to a percentage of the amount Dana gives back each month, also mentioned in the premise
if percentage_hypothesis <= percentage_premise:
    # check if the percentage in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
elif percentage_hypothesis > percentage_premise:
    # the premise gives a specific percentage for the amount Dana gives back each month
    # any percentage less than 'percentage_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
