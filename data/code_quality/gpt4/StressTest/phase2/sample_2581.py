percentage_premise = 15
percentage_hypothesis = 55

# the hypothesis refers to the percentage of Rebecca's income increase in relation to the combined income of Rebecca and Jimmy
if percentage_hypothesis <= percentage_premise:
    # check if the percentage increase in the hypothesis contradicts the estimate of 'percentage_premise'
    label = "contradiction"
elif percentage_hypothesis > percentage_premise:
    # the premise gives only an estimate for the percentage increase
    # any percentage increase greater than 'percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
