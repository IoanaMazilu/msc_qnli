income_percentage_premise = 50
income_percentage_hypothesis = 60

# the hypothesis refers to the percentage of Rebecca's income in the combined income with Jimmy, also mentioned in the premise
if income_percentage_hypothesis <= income_percentage_premise:
    # check if the percentage given in the hypothesis contradicts the percentage mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a specific percentage for Rebecca's income in the combined one
    # any percentage higher than 'income_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
