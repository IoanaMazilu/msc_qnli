income_percentage_premise = 40
income_percentage_hypothesis = 50

# the hypothesis refers to the income percentage of Rebecca in the combined income
if income_percentage_hypothesis <= income_percentage_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'income_percentage_premise'
    label = "contradiction"
elif income_percentage_hypothesis > income_percentage_premise:
    # the premise gives only a lower limit estimate for the income percentage
    # any percentage greater than 'income_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
